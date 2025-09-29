# Decompiled with PyLingual (https://pylingual.io)
# Internal filename: utils\validators.py
# Bytecode version: 3.11a7e (3495)
# Source timestamp: 1970-01-01 00:00:00 UTC (0)

"""
Utility untuk validasi data
"""
import re
from typing import Dict, List, Optional

def validate_email(email: str) -> bool:
    """
    Validasi format email
    
    Args:
        email: String email yang akan divalidasi
        
    Returns:
        True jika format valid, False jika tidak
    """
    pattern = '^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))

def validate_password_strength(password: str) -> Dict[str, bool]:
    """
    Validasi kekuatan password
    
    Args:
        password: Password yang akan divalidasi
        
    Returns:
        Dict dengan hasil validasi berbagai kriteria
    """
    return {'min_length': len(password) >= 8, 'has_uppercase': bool(re.search('[A-Z]', password)), 'has_lowercase': bool(re.search('[a-z]', password)), 'has_digit': bool(re.search('\\d', password)), 'has_special': bool(re.search('[!@#$%^&*(),.?":{}|<>]', password)), 'no_spaces': ' ' not in password}

def is_password_strong(password: str) -> bool:
    """
    Cek apakah password sudah kuat
    
    Args:
        password: Password yang akan dicek
        
    Returns:
        True jika password kuat, False jika tidak
    """
    validations = validate_password_strength(password)
    return all(validations.values())

def validate_name(name: str) -> bool:
    """
    Validasi nama (hanya huruf dan spasi)
    
    Args:
        name: Nama yang akan divalidasi
        
    Returns:
        True jika valid, False jika tidak
    """
    if not name or not name.strip():
        return False
    pattern = "^[a-zA-Z\\s\\-']+$"
    return bool(re.match(pattern, name.strip()))

def validate_company_name(company: str) -> bool:
    """
    Validasi nama company
    
    Args:
        company: Nama company yang akan divalidasi
        
    Returns:
        True jika valid, False jika tidak
    """
    if not company or not company.strip():
        return False
    pattern = '^[a-zA-Z0-9\\s\\-&.,()]+$'
    return bool(re.match(pattern, company.strip()))

def sanitize_input(text: str, max_length: int=None) -> str:
    """
    Bersihkan input dari karakter yang tidak diinginkan
    
    Args:
        text: Text yang akan dibersihkan
        max_length: Panjang maksimal (optional)
        
    Returns:
        Text yang sudah dibersihkan
    """
    if not text:
        return ''
    text = text.strip()
    if max_length and len(text) > max_length:
        text = text[:max_length]
    return text

def validate_user_data(user_data: Dict) -> List[str]:
    """
    Validasi data user yang lengkap
    
    Args:
        user_data: Dict berisi data user
        
    Returns:
        List berisi error messages (kosong jika valid)
    """
    errors = []
    first_name = user_data.get('first_name', '')
    if not validate_name(first_name):
        errors.append('First name tidak valid')
    last_name = user_data.get('last_name', '')
    if not validate_name(last_name):
        errors.append('Last name tidak valid')
    email = user_data.get('email', '')
    if not validate_email(email):
        errors.append('Format email tidak valid')
    password = user_data.get('password', '')
    if not is_password_strong(password):
        errors.append('Password tidak memenuhi kriteria keamanan')
    company = user_data.get('company', '')
    if company and (not validate_company_name(company)):
        errors.append('Nama company tidak valid')
    return errors

def format_phone_number(phone: str) -> str:
    """
    Format nomor telepon untuk konsistensi
    
    Args:
        phone: Nomor telepon
        
    Returns:
        Nomor telepon yang sudah diformat
    """
    if not phone:
        return ''
    cleaned = re.sub('[^\\d+]', '', phone)
    if cleaned.startswith('+'):
        return cleaned
    if cleaned.startswith('0'):
        return f'+44' + cleaned[1:]
    return cleaned
if __name__ == '__main__':
    test_data = {'first_name': 'John', 'last_name': 'Doe', 'email': 'john.doe@example.com', 'password': 'SecurePass123!', 'company': 'TechCorp Ltd'}
    errors = validate_user_data(test_data)
    if errors:
        print('Validation errors:')
        for error in errors:
            print(f'  - {error}')
    else:
        print('All validations passed!')
    password_tests = ['weak', 'StrongPass123!', 'noUpper123!', 'NOLOWER123!']
    for pwd in password_tests:
        print(f"Password '{pwd}' is strong: {is_password_strong(pwd)}")