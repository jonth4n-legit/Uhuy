# Decompiled with PyLingual (https://pylingual.io)
# Internal filename: services\firefox_relay_service.py
# Bytecode version: 3.11a7e (3495)
# Source timestamp: 1970-01-01 00:00:00 UTC (0)

"""
Service untuk mengelola email relay menggunakan Firefox Relay API
"""
import requests
from typing import Dict, Optional, List, Any
import logging
from config.constants import FIREFOX_RELAY_API_KEY, FIREFOX_RELAY_BASE_URL
logger = logging.getLogger(__name__)

class FirefoxRelayService:
    """Service untuk membuat dan mengelola email relay dari Firefox"""

    def __init__(self, api_key: Optional[str]=None, base_url: Optional[str]=None):
        """
        Initialize Firefox Relay service
        
        Args:
            api_key: API key untuk Firefox Relay
            base_url: Base URL untuk API (default dari env)
        """
        self.api_key = api_key or FIREFOX_RELAY_API_KEY
        self.base_url = base_url or FIREFOX_RELAY_BASE_URL
        if not self.api_key:
            raise ValueError('Firefox Relay API key diperlukan')
        self.session = requests.Session()
        self.session.headers.update({'Authorization': f'Bearer {self.api_key}', 'Content-Type': 'application/json', 'Accept': 'application/json'})

    def create_relay_mask(self, description: str=None) -> Optional[Dict]:
        """
        Buat email mask/relay baru
        
        Args:
            description: Deskripsi untuk mask email
            
        Returns:
            Dict dengan informasi mask atau None jika error
        """
        logger.info(f'Creating relay mask with description: {description}')
        try:
            url = f'{self.base_url}/api/v1/relayaddresses/'
            logger.info(f'Request URL: {url}')
            data = {}
            if description:
                data['description'] = description
            logger.info(f'Request data: {data}')
            logger.info(f'Request headers: {dict(self.session.headers)}')
            response = self.session.post(url, json=data, timeout=10)
            logger.info(f'Response status: {response.status_code}')
            logger.info(f'Response headers: {dict(response.headers)}')
            if response.status_code == 401:
                auth_formats = [f'Token {self.api_key}', f'Bearer {self.api_key}', f'API-Key {self.api_key}', self.api_key]
                for auth_format in auth_formats:
                    logger.info(f'Trying auth format: {auth_format[:20]}...')
                    test_session = requests.Session()
                    test_session.headers.update({'Authorization': auth_format, 'Content-Type': 'application/json', 'Accept': 'application/json'})
                    test_response = test_session.post(url, json=data, timeout=10)
                    logger.info(f'Test response status: {test_response.status_code}')
                    if test_response.status_code != 401:
                        logger.info(f'Success with auth format: {auth_format[:20]}...')
                        self.session.headers.update({'Authorization': auth_format})
                        response = test_response
                        break
                else:
                    logger.error('All authentication formats failed')
                    response.raise_for_status()
            response.raise_for_status()
            mask_data = response.json()
            logger.info(f'Created mask successfully: {mask_data}')
            return {'id': mask_data.get('id'), 'address': mask_data.get('address'), 'domain': mask_data.get('domain'), 'full_address': mask_data.get('full_address'), 'description': mask_data.get('description'), 'enabled': mask_data.get('enabled', True), 'created_at': mask_data.get('created_at')}
        except requests.RequestException as e:
            logger.error(f'Error creating relay mask: {e}')
            if hasattr(e, 'response') and e.response is not None:
                logger.error(f'Response text: {e.response.text}')
            return None
        except Exception as e:
            logger.error(f'Unexpected error: {e}')
            return None

    def list_relay_masks(self) -> List[Dict]:
        """
        Ambil daftar semua email mask yang sudah dibuat
        
        Returns:
            List berisi dict informasi mask
        """
        logger.info('Listing relay masks...')
        try:
            url = f'{self.base_url}/api/v1/relayaddresses/'
            logger.info(f'Request URL: {url}')
            response = self.session.get(url, timeout=10)
            logger.info(f'Response status: {response.status_code}')
            if response.status_code == 401:
                auth_formats = [f'Token {self.api_key}', f'Bearer {self.api_key}', f'API-Key {self.api_key}', self.api_key]
                for auth_format in auth_formats:
                    logger.info(f'Trying auth format: {auth_format[:20]}...')
                    test_session = requests.Session()
                    test_session.headers.update({'Authorization': auth_format, 'Content-Type': 'application/json', 'Accept': 'application/json'})
                    test_response = test_session.get(url, timeout=10)
                    logger.info(f'Test response status: {test_response.status_code}')
                    if test_response.status_code != 401:
                        logger.info(f'Success with auth format: {auth_format[:20]}...')
                        self.session.headers.update({'Authorization': auth_format})
                        response = test_response
                        break
                else:
                    logger.error('All authentication formats failed for list')
                    response.raise_for_status()
            response.raise_for_status()
            data = response.json()
            logger.info(f'API response data: {data}')
            masks = []
            mask_list = data.get('results', data) if isinstance(data, dict) else data
            if not isinstance(mask_list, list):
                mask_list = [mask_list] if mask_list else []
            for mask in mask_list:
                masks.append({'id': mask.get('id'), 'address': mask.get('address'), 'domain': mask.get('domain'), 'full_address': mask.get('full_address'), 'description': mask.get('description'), 'enabled': mask.get('enabled', True), 'created_at': mask.get('created_at'), 'num_forwarded': mask.get('num_forwarded', 0), 'num_blocked': mask.get('num_blocked', 0)})
            logger.info(f'Found {len(masks)} masks')
            return masks
        except requests.RequestException as e:
            logger.error(f'Error listing relay masks: {e}')
            if hasattr(e, 'response') and e.response is not None:
                logger.error(f'Response text: {e.response.text}')
            return []
        except Exception as e:
            logger.error(f'Unexpected error: {e}')
            return []

    def test_connection(self) -> Dict[str, any]:
        """
        Test koneksi ke Firefox Relay API dengan berbagai auth format dan URL
        
        Returns:
            Dict dengan hasil test
        """
        results = {'success': False, 'auth_format': None, 'error': None, 'masks_count': 0, 'working_url': None}
        logger.info('Testing Firefox Relay API connection...')
        base_urls = [('Production', 'https://relay.firefox.com'), ('Development', 'https://dev.fxprivaterelay.nonprod.cloudops.mozgcp.net')]
        endpoints = ['/api/v1/relayaddresses/', '/api/v1/', '/accounts/profile/']
        for env_name, base_url in base_urls:
            logger.info(f'Testing {env_name} environment: {base_url}')
            for endpoint in endpoints:
                url = f'{base_url}{endpoint}'
                logger.info(f'Testing endpoint: {endpoint}')
                auth_formats = [('Token', f'Token {self.api_key}'), ('Bearer', f'Bearer {self.api_key}'), ('API-Key', f'API-Key {self.api_key}'), ('X-API-Key', 'X-API-Key'), ('Raw', self.api_key)]
                for format_name, auth_format in auth_formats:
                    logger.info(f'Testing {format_name} format...')
                    try:
                        test_session = requests.Session()
                        headers = {'Content-Type': 'application/json', 'Accept': 'application/json', 'User-Agent': 'AutoCloudSkill/1.0'}
                        if format_name == 'X-API-Key':
                            headers['X-API-Key'] = self.api_key
                        else:
                            headers['Authorization'] = auth_format
                        test_session.headers.update(headers)
                        response = test_session.get(url, timeout=10)
                        logger.info(f'Response status: {response.status_code}')
                        if response.status_code == 200:
                            data = response.json()
                            mask_list = data.get('results', data) if isinstance(data, dict) else data
                            if not isinstance(mask_list, list):
                                mask_list = [mask_list] if mask_list else []
                            results['success'] = True
                            results['auth_format'] = f"{format_name}: {(auth_format if format_name != 'X-API-Key' else 'X-API-Key header')}"
                            results['masks_count'] = len(mask_list)
                            results['working_url'] = base_url
                            self.base_url = base_url
                            if format_name == 'X-API-Key':
                                self.session.headers.update({'X-API-Key': self.api_key})
                                if 'Authorization' in self.session.headers:
                                    del self.session.headers['Authorization']
                            else:
                                self.session.headers.update({'Authorization': auth_format})
                                if 'X-API-Key' in self.session.headers:
                                    del self.session.headers['X-API-Key']
                            logger.info(f'Connection test successful: {env_name} - {format_name}')
                            return results
                    except requests.RequestException as e:
                        logger.warning(f'{format_name} failed: {e}')
        else:
            results['error'] = 'All authentication formats and URLs failed'
            logger.error('All authentication formats and URLs failed')
            return results

    def delete_relay_mask(self, mask_id: str) -> bool:
        """
        Hapus email mask
        
        Args:
            mask_id: ID dari mask yang akan dihapus
            
        Returns:
            True jika berhasil, False jika error
        """
        try:
            url = f'{self.base_url}/api/v1/relayaddresses/{mask_id}/'
            response = self.session.delete(url, timeout=10)
            response.raise_for_status()
            return True
        except requests.RequestException as e:
            logger.error(f'Error deleting relay mask: {e}')
            return False
        except Exception as e:
            logger.error(f'Unexpected error: {e}')
            return False

    def delete_all_masks(self) -> Dict[str, any]:
        """
        Hapus semua email mask yang ada pada akun saat ini.
        Returns ringkasan hasil: requested, deleted, failed_ids
        """
        try:
            masks = self.list_relay_masks()
            total = len(masks)
            deleted = 0
            failed_ids = []
            for m in masks:
                mid = m.get('id')
                if not mid:
                    continue
                ok = self.delete_relay_mask(mid)
                if ok:
                    deleted = deleted + 1
                else:
                    failed_ids.append(mid)
            return {'requested': total, 'deleted': deleted, 'failed_ids': failed_ids}
        except Exception as e:
            logger.error(f'Error deleting all masks: {e}')
            return {'requested': 0, 'deleted': 0, 'failed_ids': [], 'error': str(e)}

    def auto_purge_if_limit_reached(self, limit: int=5) -> Dict[str, Any]:
        """Jika jumlah email masks sudah mencapai/melewati `limit`, hapus semua secara otomatis.

        Returns:
            Dict summary:
              - purged: bool
              - count: int (jumlah sebelum purge, jika tidak purge)
              - requested, deleted, failed_ids (jika purge dilakukan)
        """
        try:
            masks = self.list_relay_masks()
            count = len(masks)
            if count >= int(limit):
                res = self.delete_all_masks()
                out = {'purged': True}
                out.update(res)
                return out
            return {'purged': False, 'count': count}
        except Exception as e:
            logger.error(f'auto_purge_if_limit_reached error: {e}')
            return {'purged': False, 'error': str(e)}
    pass
    pass

    def update_relay_mask(self, mask_id: str, enabled: bool=None, description: str=None) -> Optional[Dict]:
        """
        Update pengaturan email mask
        
        Args:
            mask_id: ID dari mask
            enabled: Enable/disable mask
            description: Update deskripsi
            
        Returns:
            Dict dengan informasi mask yang diupdate atau None jika error
        """
        try:
            url = f'{self.base_url}/api/v1/relayaddresses/{mask_id}/'
            data = {}
            if enabled is not None:
                data['enabled'] = enabled
            if description is not None:
                data['description'] = description
            if not data:
                return
            response = self.session.patch(url, json=data, timeout=10)
            response.raise_for_status()
            mask_data = response.json()
            return {'id': mask_data.get('id'), 'address': mask_data.get('address'), 'domain': mask_data.get('domain'), 'full_address': mask_data.get('full_address'), 'description': mask_data.get('description'), 'enabled': mask_data.get('enabled', True), 'created_at': mask_data.get('created_at')}
        except requests.RequestException as e:
            logger.error(f'Error updating relay mask: {e}')
        except Exception as e:
            logger.error(f'Unexpected error: {e}')

    def get_relay_mask_details(self, mask_id: str) -> Optional[Dict]:
        """
        Ambil detail email mask berdasarkan ID
        
        Args:
            mask_id: ID dari mask
            
        Returns:
            Dict dengan detail mask atau None jika error
        """
        try:
            url = f'{self.base_url}/api/v1/relayaddresses/{mask_id}/'
            response = self.session.get(url, timeout=10)
            response.raise_for_status()
            mask_data = response.json()
            return {'id': mask_data.get('id'), 'address': mask_data.get('address'), 'domain': mask_data.get('domain'), 'full_address': mask_data.get('full_address'), 'description': mask_data.get('description'), 'enabled': mask_data.get('enabled', True), 'created_at': mask_data.get('created_at'), 'num_forwarded': mask_data.get('num_forwarded', 0), 'num_blocked': mask_data.get('num_blocked', 0)}
        except requests.RequestException as e:
            logger.error(f'Error getting relay mask details: {e}')
        except Exception as e:
            logger.error(f'Unexpected error: {e}')
if __name__ == '__main__':
    try:
        service = FirefoxRelayService()
        mask = service.create_relay_mask('Auto registration mask')
        if mask:
            print('Created new email mask:')
            print(f"Address: {mask['full_address']}")
            print(f"ID: {mask['id']}")
            print(f"Description: {mask['description']}")
        else:
            print('Failed to create email mask')
    except Exception as e:
        print(f'Error: {e}')
        print('Pastikan API key sudah diset di file .env')