"""
Random User Service untuk generate data user acak
"""
import requests
import random
import string
from typing import Dict, Optional, List
import logging

logger = logging.getLogger(__name__)

class RandomUserService:
    """Service untuk generate data user acak menggunakan randomuser.me API"""

    def __init__(self):
        self.api_url = 'https://randomuser.me/api/'

    def get_random_user(self, gender: str = 'female', nationalities: str = 'gb,us,es') -> Optional[Dict]:
        """
        Ambil data user acak dari API
        
        Args:
            gender: Gender yang diinginkan (male/female)
            nationalities: Nationalities yang diinginkan (comma separated)
            
        Returns:
            Dict dengan data user atau None jika error
        """
        try:
            params = {
                'gender': gender,
                'nat': nationalities,
                'inc': 'name,email,login'
            }
            
            response = requests.get(self.api_url, params=params, timeout=10)
            response.raise_for_status()
            
            data = response.json()
            results = data.get('results', [])
            
            if not results:
                return None
            
            user = results[0]
            name = user.get('name', {})
            login = user.get('login', {})
            
            return {
                'first_name': name.get('first', ''),
                'last_name': name.get('last', ''),
                'email': user.get('email', ''),
                'username': login.get('username', ''),
                'password': login.get('password', '')
            }
            
        except Exception as e:
            logger.error(f'Error getting random user: {e}')
            return None

    def generate_company_name(self) -> str:
        """Generate nama perusahaan acak"""
        prefixes = ['Tech', 'Digital', 'Cloud', 'Data', 'AI', 'Smart', 'Future', 'Next']
        suffixes = ['Corp', 'Inc', 'Ltd', 'Solutions', 'Systems', 'Technologies', 'Group', 'Enterprises']
        
        prefix = random.choice(prefixes)
        suffix = random.choice(suffixes)
        
        return f"{prefix} {suffix}"

    def generate_password(self, length: int = 12) -> str:
        """Generate password acak"""
        characters = string.ascii_letters + string.digits + "!@#$%^&*"
        password = ''.join(random.choice(characters) for _ in range(length))
        return password

    def generate_email(self, first_name: str, last_name: str) -> str:
        """Generate email berdasarkan nama"""
        domains = ['gmail.com', 'yahoo.com', 'hotmail.com', 'outlook.com']
        domain = random.choice(domains)
        
        # Various email formats
        formats = [
            f"{first_name.lower()}.{last_name.lower()}@{domain}",
            f"{first_name.lower()}{last_name.lower()}@{domain}",
            f"{first_name.lower()}{random.randint(1, 999)}@{domain}",
            f"{first_name.lower()}.{last_name.lower()}{random.randint(1, 99)}@{domain}"
        ]
        
        return random.choice(formats)