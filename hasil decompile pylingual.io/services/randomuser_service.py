"""
Service untuk mengambil data random user dari api.randomuser.me
"""
import requests
import random
import string
from typing import Dict, Optional
import logging

logger = logging.getLogger(__name__)

class RandomUserService:
    """Service untuk generate data user random dari API randomuser.me"""

    def __init__(self):
        self.base_url = 'https://randomuser.me/api/'
        self.session = requests.Session()

    def get_random_user(self, gender: str = 'female', nationalities: str = 'gb,us,es') -> Optional[Dict]:
        """
        Mengambil data user random dari API
        
        Args:
            gender: Jenis kelamin (male/female)  
            nationalities: Kewarganegaraan yang diinginkan (gb,us,es)
            
        Returns:
            Dict berisi data user atau None jika error
        """
        try:
            params = {
                'gender': gender, 
                'nat': nationalities, 
                'results': 1
            }
            response = self.session.get(self.base_url, params=params, timeout=10)
            response.raise_for_status()
            
            data = response.json()
            if data.get('results'):
                user_data = data['results'][0]
                return self._extract_user_info(user_data)
            return None
            
        except requests.RequestException as e:
            logger.error(f'Error fetching random user: {e}')
            return None
        except Exception as e:
            logger.error(f'Unexpected error: {e}')
            return None

    def _extract_user_info(self, user_data: Dict) -> Dict:
        """
        Ekstrak informasi user yang dibutuhkan
        
        Args:
            user_data: Raw data dari API
            
        Returns:
            Dict dengan informasi user yang sudah diformat
        """
        try:
            name = user_data.get('name', {})
            location = user_data.get('location', {})
            
            return {
                'first_name': name.get('first', '').title(),
                'last_name': name.get('last', '').title(),
                'email': user_data.get('email', ''),
                'gender': user_data.get('gender', ''),
                'country': location.get('country', ''),
                'city': location.get('city', ''),
                'phone': user_data.get('phone', ''),
                'picture': user_data.get('picture', {}).get('large', '')
            }
        except Exception as e:
            logger.error(f'Error extracting user info: {e}')
            return {}

    def generate_password(self, length: int = 12) -> str:
        """
        Generate password random dengan kombinasi karakter
        
        Args:
            length: Panjang password (default 12)
            
        Returns:
            String password random
        """
        characters = string.ascii_letters + string.digits + '!@#$%^&*'
        
        # Ensure password has at least one of each type
        password = [
            random.choice(string.ascii_uppercase),
            random.choice(string.ascii_lowercase),
            random.choice(string.digits),
            random.choice('!@#$%^&*')
        ]
        
        # Fill the rest with random characters
        for _ in range(length - 4):
            password.append(random.choice(characters))
            
        random.shuffle(password)
        return ''.join(password)

    def generate_company_name(self) -> str:
        """
        Generate nama company random
        
        Returns:
            String nama company
        """
        companies = [
            'TechCorp', 'InnovateInc', 'DataSoft', 'CloudTech', 'NextGen', 
            'DigitalWorks', 'SmartSolutions', 'FutureTech', 'GlobalSoft', 
            'TechVision', 'DataFlow', 'CloudBase', 'TechHub', 'InnovateLab', 
            'CyberEdge', 'AIWorks', 'QuantumSoft', 'NeoSystems', 'PixelLogic', 
            'CodeForge', 'NetSphere', 'VisionaryTech', 'ByteCraft', 'CloudNova'
        ]
        
        suffixes = ['Solutions', 'Technologies', 'Systems', 'Corp', 'Inc', 'Ltd']
        
        if random.choice([True, False]):
            return random.choice(companies)
            
        base = random.choice(['Tech', 'Data', 'Cloud', 'Smart', 'Digital'])
        suffix = random.choice(suffixes)
        return f'{base}{suffix}'

if __name__ == '__main__':
    service = RandomUserService()
    user = service.get_random_user()
    if user:
        print('Generated User Data:')
        print(f"Name: {user['first_name']} {user['last_name']}")
        print(f"Email: {user['email']}")
        print(f"Country: {user['country']}")
        print(f'Password: {service.generate_password()}')
        print(f'Company: {service.generate_company_name()}')