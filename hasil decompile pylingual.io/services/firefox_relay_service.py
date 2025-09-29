"""
Firefox Relay service untuk membuat email temporary
"""
import requests
import json
import time
from typing import Dict, List, Optional
import logging

logger = logging.getLogger(__name__)

class FirefoxRelayService:
    """Service untuk mengelola Firefox Relay email masks"""

    def __init__(self, api_key: str = None):
        """
        Initialize Firefox Relay service
        
        Args:
            api_key: Firefox Relay API key
        """
        if not api_key:
            raise ValueError("API key is required for Firefox Relay service")
        
        self.api_key = api_key.strip()
        self.base_url = 'https://relay.firefox.com'
        self.session = requests.Session()
        
        # Set up headers
        self.session.headers.update({
            'Authorization': f'Token {self.api_key}',
            'Content-Type': 'application/json',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        })

    def test_connection(self) -> Dict:
        """
        Test connection dengan berbagai format auth
        
        Returns:
            Dict dengan hasil test connection
        """
        auth_formats = [
            f'Token {self.api_key}',
            f'Bearer {self.api_key}',
            self.api_key
        ]
        
        urls = [
            f'{self.base_url}/api/v1/relayaddresses/',
            f'{self.base_url}/api/v1/masks/',
        ]
        
        for url in urls:
            for auth_format in auth_formats:
                try:
                    headers = {
                        'Authorization': auth_format,
                        'Content-Type': 'application/json',
                        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
                    }
                    
                    response = requests.get(url, headers=headers, timeout=10)
                    
                    if response.status_code == 200:
                        data = response.json()
                        masks_count = len(data) if isinstance(data, list) else data.get('count', 0)
                        
                        # Update session headers with working format
                        self.session.headers.update({'Authorization': auth_format})
                        
                        return {
                            'success': True,
                            'working_url': url,
                            'auth_format': auth_format,
                            'masks_count': masks_count,
                            'response_data': data
                        }
                        
                except Exception as e:
                    logger.debug(f'Failed auth format {auth_format} for {url}: {e}')
                    continue
                    
        return {
            'success': False,
            'error': 'Could not authenticate with any format',
            'auth_format': None,
            'working_url': None,
            'masks_count': 0
        }

    def get_masks(self) -> List[Dict]:
        """
        Ambil semua email masks yang tersedia
        
        Returns:
            List email masks
        """
        try:
            # Try different endpoints
            endpoints = [
                '/api/v1/relayaddresses/',
                '/api/v1/masks/',
            ]
            
            for endpoint in endpoints:
                try:
                    response = self.session.get(f'{self.base_url}{endpoint}', timeout=10)
                    if response.status_code == 200:
                        data = response.json()
                        if isinstance(data, list):
                            return data
                        elif isinstance(data, dict) and 'results' in data:
                            return data['results']
                except Exception:
                    continue
                    
            return []
            
        except Exception as e:
            logger.error(f'Error getting masks: {e}')
            return []

    def create_relay_mask(self, description: str = None) -> Optional[Dict]:
        """
        Buat email mask baru
        
        Args:
            description: Deskripsi untuk mask
            
        Returns:
            Dict dengan informasi mask baru atau None jika gagal
        """
        try:
            payload = {}
            if description:
                payload['description'] = description
                
            # Try different endpoints for creating masks
            endpoints = [
                '/api/v1/relayaddresses/',
                '/api/v1/masks/',
            ]
            
            for endpoint in endpoints:
                try:
                    response = self.session.post(
                        f'{self.base_url}{endpoint}',
                        json=payload,
                        timeout=10
                    )
                    
                    if response.status_code in [200, 201]:
                        mask_data = response.json()
                        
                        # Normalize response format
                        if 'full_address' not in mask_data:
                            # Try to construct full address from available fields
                            address = mask_data.get('address') or mask_data.get('mask') or mask_data.get('email')
                            domain = mask_data.get('domain', 'mozmail.com')
                            if address and '@' not in address:
                                mask_data['full_address'] = f'{address}@{domain}'
                            elif address:
                                mask_data['full_address'] = address
                                
                        logger.info(f'Created mask: {mask_data.get("full_address", "Unknown")}')
                        return mask_data
                        
                except Exception as e:
                    logger.debug(f'Failed to create mask with endpoint {endpoint}: {e}')
                    continue
                    
            return None
            
        except Exception as e:
            logger.error(f'Error creating relay mask: {e}')
            return None

    def delete_mask(self, mask_id: str) -> bool:
        """
        Hapus email mask
        
        Args:
            mask_id: ID mask yang akan dihapus
            
        Returns:
            True jika berhasil dihapus
        """
        try:
            endpoints = [
                f'/api/v1/relayaddresses/{mask_id}/',
                f'/api/v1/masks/{mask_id}/',
            ]
            
            for endpoint in endpoints:
                try:
                    response = self.session.delete(f'{self.base_url}{endpoint}', timeout=10)
                    if response.status_code in [200, 204]:
                        logger.info(f'Deleted mask: {mask_id}')
                        return True
                except Exception:
                    continue
                    
            return False
            
        except Exception as e:
            logger.error(f'Error deleting mask {mask_id}: {e}')
            return False

    def delete_all_masks(self) -> Dict:
        """
        Hapus semua email masks
        
        Returns:
            Dict dengan statistik penghapusan
        """
        try:
            masks = self.get_masks()
            if not masks:
                return {'requested': 0, 'deleted': 0, 'failed_ids': []}
                
            deleted = 0
            failed_ids = []
            
            for mask in masks:
                mask_id = mask.get('id') or mask.get('mask_id')
                if not mask_id:
                    continue
                    
                if self.delete_mask(str(mask_id)):
                    deleted += 1
                else:
                    failed_ids.append(str(mask_id))
                    
                # Small delay to avoid rate limiting
                time.sleep(0.1)
                
            return {
                'requested': len(masks),
                'deleted': deleted,
                'failed_ids': failed_ids
            }
            
        except Exception as e:
            logger.error(f'Error deleting all masks: {e}')
            return {'requested': 0, 'deleted': 0, 'failed_ids': []}

    def auto_purge_if_limit_reached(self, limit: int = 5) -> Dict:
        """
        Auto purge masks jika mencapai limit tertentu
        
        Args:
            limit: Batas maksimal masks sebelum auto purge
            
        Returns:
            Dict dengan hasil purge
        """
        try:
            masks = self.get_masks()
            current_count = len(masks)
            
            if current_count < limit:
                return {'purged': False, 'count': current_count}
                
            # Purge oldest masks
            result = self.delete_all_masks()
            result['purged'] = True
            result['count'] = current_count
            
            return result
            
        except Exception as e:
            logger.error(f'Error in auto purge: {e}')
            return {'purged': False, 'count': 0}

if __name__ == '__main__':
    # Test code
    try:
        service = FirefoxRelayService('your-api-key-here')
        result = service.test_connection()
        print(f'Connection test: {result}')
        
        if result['success']:
            masks = service.get_masks()
            print(f'Current masks: {len(masks)}')
            
            # Create test mask
            new_mask = service.create_relay_mask('Test mask')
            if new_mask:
                print(f'Created mask: {new_mask.get("full_address")}')
            
    except Exception as e:
        print(f'Test error: {e}')