# Decompiled with PyLingual (https://pylingual.io)
# Internal filename: config\licensing.py
# Bytecode version: 3.11a7e (3495)
# Source timestamp: 1970-01-01 00:00:00 UTC (0)

import requests
import hashlib
from typing import Any, Dict, Optional
from config.constants import VERSION, BASE_URL, PRODUCT_CODE

def get_machine_id() -> str:
    """Ambil Machine ID dari py-machineid.
    Raises: ImportError/Exception jika gagal.
    """
    import machineid
    return machineid.id()

def get_hashed_machine_id() -> str:
    """Ambil Machine ID dan kembalikan SHA-256 hexdigest-nya."""
    raw = get_machine_id()
    return hashlib.sha256(raw.encode('utf-8')).hexdigest()

def _post(path: str, payload: Dict[str, Any], timeout: int=20) -> requests.Response:
    url = f'{BASE_URL}{path}'
    return requests.post(url, json=payload, timeout=timeout)

def check_license(key: str, product_code: str, *, device_id: Optional[str]=None, version: Optional[str]=None) -> Dict[str, Any]:
    """Panggil /api/licenses/check sesuai OpenAPI.
    Wajib: key, product_code. Opsional: device_id, version.
    Return dict normalized: {valid, plan, status, expiresAt, reason, http_status, ok, raw}
    """
    payload = {'key': key, 'product_code': product_code}
    if device_id:
        payload['device_id'] = device_id
    if version:
        payload['version'] = version
    resp = _post('/api/licenses/check', payload)
    try:
        data = resp.json()
    except Exception:
        data = {}
    valid = bool(data.get('valid')) if isinstance(data, dict) else False
    plan = data.get('plan') if isinstance(data, dict) else None
    status = data.get('status') if isinstance(data, dict) else None
    expires_at = data.get('expiresAt') if isinstance(data, dict) else None
    reason = data.get('reason') if isinstance(data, dict) else None
    return {'ok': resp.ok, 'http_status': resp.status_code, 'valid': valid, 'plan': plan, 'status': status, 'expiresAt': expires_at, 'reason': reason, 'raw': data}

def provision_trial(product_code: str, *, device_id: Optional[str]=None) -> Dict[str, Any]:
    """Panggil /api/licenses/provision dengan plan trial.
    API bersifat idempotent (200 bila existing, 201 bila created).
    Return dict normalized: {ok, key, plan, expiresAt, http_status, raw}
    """
    payload = {'product_code': product_code, 'plan': 'trial'}
    if device_id:
        payload['device_id'] = device_id
    resp = _post('/api/licenses/provision', payload)
    try:
        data = resp.json()
    except Exception:
        data = {}
    key = data.get('key') if isinstance(data, dict) else None
    plan = data.get('plan') if isinstance(data, dict) else 'trial'
    expires_at = data.get('expires_at') or data.get('expiresAt') if isinstance(data, dict) else None
    ok = bool(data.get('ok')) if isinstance(data, dict) else resp.status_code in (200, 201)
    return {'ok': ok, 'http_status': resp.status_code, 'key': key, 'plan': plan, 'expiresAt': expires_at, 'raw': data}

def ensure_license(*, product_code: str=PRODUCT_CODE, version: Optional[str]=VERSION) -> Dict[str, Any]:
    """Pastikan lisensi valid dengan kebijakan:
    - key = sha256(machine_id) (tidak disimpan lokal)
    - check; jika invalid/tidak ditemukan, auto-provision trial (device_id=machine_id), lalu re-check
    - is_allowed = valid and plan != 'free' and status != 'suspended'
    Return dict: {is_allowed, valid, plan, status, expiresAt, reason, check}
    """
    try:
        mid = get_hashed_machine_id()
    except Exception as e:
        return {'is_allowed': False, 'valid': False, 'plan': None, 'status': 'error', 'expiresAt': None, 'reason': f'Machine ID error: {e}', 'check': None}
    key = mid
    device_id = mid
    try:
        chk = check_license(key, product_code, device_id=device_id, version=version)
    except Exception as e:
        return {'is_allowed': False, 'valid': False, 'plan': None, 'status': 'error', 'expiresAt': None, 'reason': f'API error: {e}', 'check': None}
    if not chk.get('valid'):
        try:
            provision_trial(product_code, device_id=device_id)
        except Exception as e:
            return {'is_allowed': False, 'valid': False, 'plan': None, 'status': 'error', 'expiresAt': None, 'reason': f'Provision error: {e}', 'check': chk}
        try:
            chk = check_license(key, product_code, device_id=device_id, version=version)
        except Exception as e:
            return {'is_allowed': False, 'valid': False, 'plan': None, 'status': 'error', 'expiresAt': None, 'reason': f'Recheck error: {e}', 'check': None}
    valid = bool(chk.get('valid'))
    plan_val = chk.get('plan')
    plan = plan_val.lower() if isinstance(plan_val, str) else plan_val
    status_val = chk.get('status')
    status = status_val.lower() if isinstance(status_val, str) else status_val
    is_allowed = valid and plan not in ['free'] and (status != 'suspended')
    return {'is_allowed': is_allowed, 'valid': valid, 'plan': plan, 'status': status, 'expiresAt': chk.get('expiresAt'), 'reason': chk.get('reason'), 'check': chk}