"""
Random User Service for Auto Cloud Skill Registration application.

Professional implementation of random user data generation service
using the randomuser.me API with proper error handling and data validation.
"""

import requests
import random
import string
import secrets
from typing import Dict, Optional, List
import logging
from datetime import datetime, timedelta

from config.constants import RANDOMUSER_API_URL, DEFAULT_GENDER, DEFAULT_NATIONALITIES, DEFAULT_PASSWORD_LENGTH
from utils.logger import log_service_call
from utils.validators import validate_email, validate_name, ValidationError

logger = logging.getLogger(__name__)

class RandomUserService:
    """
    Service for generating random user data using the randomuser.me API.

    This service provides clean, validated user data for account registration
    purposes with proper error handling and retry logic.
    """

    def __init__(self):
        """Initialize the Random User Service."""
        self.base_url = RANDOMUSER_API_URL
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Auto-Cloud-Skill/1.2.0',
            'Accept': 'application/json'
        })

    def get_random_user(self,
                       gender: Optional[str] = None,
                       nationalities: Optional[str] = None,
                       password_length: Optional[int] = None) -> Optional[Dict]:
        """
        Generate random user data from randomuser.me API.

        Args:
            gender: Gender preference ('male', 'female', or None for random)
            nationalities: Comma-separated nationality codes (e.g., 'gb,us,es')
            password_length: Length of generated password

        Returns:
            Dict: User data dictionary or None if failed
        """
        start_time = datetime.now()

        try:
            # Use defaults if not provided
            gender = gender or DEFAULT_GENDER
            nationalities = nationalities or DEFAULT_NATIONALITIES
            password_length = password_length or DEFAULT_PASSWORD_LENGTH

            # Prepare API parameters
            params = {
                'gender': gender,
                'nat': nationalities,
                'results': 1,
                'inc': 'gender,name,email,dob,phone,picture,nat'
            }

            # Make API request with timeout
            response = self.session.get(
                self.base_url,
                params=params,
                timeout=10
            )
            response.raise_for_status()

            # Parse response
            data = response.json()
            if not data.get('results'):
                raise ValueError("No user data returned from API")

            user_data = data['results'][0]
            extracted_data = self._extract_user_info(user_data, password_length)

            # Log successful service call
            response_time = (datetime.now() - start_time).total_seconds()
            log_service_call('RandomUser', 'get_random_user', 'SUCCESS', response_time)

            return extracted_data

        except requests.RequestException as e:
            logger.error(f"API request failed: {e}")
            log_service_call('RandomUser', 'get_random_user', 'FAILED')
            return None

        except Exception as e:
            logger.error(f"Unexpected error generating user data: {e}")
            log_service_call('RandomUser', 'get_random_user', 'ERROR')
            return None

    def _extract_user_info(self, user_data: Dict, password_length: int) -> Dict:
        """
        Extract and clean user information from API response.

        Args:
            user_data: Raw user data from randomuser.me API
            password_length: Length of password to generate

        Returns:
            Dict: Cleaned and validated user data
        """
        try:
            # Extract basic info
            name = user_data.get('name', {})
            first_name = name.get('first', '').strip()
            last_name = name.get('last', '').strip()
            email = user_data.get('email', '').strip()
            gender = user_data.get('gender', '').strip()
            phone = user_data.get('phone', '').strip()
            nationality = user_data.get('nat', '').strip()

            # Validate and clean names
            try:
                first_name = validate_name(first_name)
                last_name = validate_name(last_name)
            except ValidationError as e:
                logger.warning(f"Name validation failed, using fallback: {e}")
                first_name = self._generate_fallback_name()
                last_name = self._generate_fallback_name()

            # Validate email
            try:
                validate_email(email)
            except ValidationError as e:
                logger.warning(f"Email validation failed: {e}")
                # Generate fallback email
                email = self._generate_fallback_email(first_name, last_name)

            # Generate secure password
            password = self._generate_secure_password(password_length)

            # Generate company name
            company = self._generate_company_name()

            # Build user data dictionary
            user_info = {
                'first_name': first_name,
                'last_name': last_name,
                'email': email,
                'password': password,
                'gender': gender,
                'phone': phone,
                'nationality': nationality,
                'company': company,
                'full_name': f"{first_name} {last_name}",
                'generated_at': datetime.now().isoformat()
            }

            logger.info(f"Generated user data for: {user_info['full_name']}")
            return user_info

        except Exception as e:
            logger.error(f"Error extracting user info: {e}")
            # Return minimal fallback data
            return self._generate_fallback_user(password_length)

    def _generate_secure_password(self, length: int) -> str:
        """
        Generate a cryptographically secure password.

        Args:
            length: Password length

        Returns:
            str: Secure password
        """
        if length < 8:
            length = 8

        # Define character sets
        lowercase = string.ascii_lowercase
        uppercase = string.ascii_uppercase
        digits = string.digits
        symbols = "!@#$%^&*"

        # Ensure at least one character from each set
        password = [
            secrets.choice(lowercase),
            secrets.choice(uppercase),
            secrets.choice(digits),
            secrets.choice(symbols)
        ]

        # Fill remaining length with random characters
        all_chars = lowercase + uppercase + digits + symbols
        for _ in range(length - 4):
            password.append(secrets.choice(all_chars))

        # Shuffle the password
        secrets.SystemRandom().shuffle(password)
        return ''.join(password)

    def _generate_company_name(self) -> str:
        """Generate a random company name."""
        prefixes = ['Innovative', 'Global', 'Tech', 'Digital', 'Smart', 'Advanced', 'Future']
        suffixes = ['Solutions', 'Systems', 'Technologies', 'Labs', 'Corp', 'Ltd', 'Inc']

        prefix = secrets.choice(prefixes)
        suffix = secrets.choice(suffixes)
        return f"{prefix} {suffix}"

    def _generate_fallback_name(self) -> str:
        """Generate a fallback name if API data is invalid."""
        names = [
            'Alex', 'Jordan', 'Casey', 'Riley', 'Taylor', 'Morgan',
            'Avery', 'Quinn', 'Blake', 'Cameron', 'Drew', 'Sage'
        ]
        return secrets.choice(names)

    def _generate_fallback_email(self, first_name: str, last_name: str) -> str:
        """Generate a fallback email address."""
        domains = ['example.com', 'test.org', 'sample.net']
        domain = secrets.choice(domains)
        username = f"{first_name.lower()}.{last_name.lower()}"
        random_num = secrets.randbelow(1000)
        return f"{username}{random_num}@{domain}"

    def _generate_fallback_user(self, password_length: int) -> Dict:
        """Generate complete fallback user data if all else fails."""
        first_name = self._generate_fallback_name()
        last_name = self._generate_fallback_name()
        email = self._generate_fallback_email(first_name, last_name)
        password = self._generate_secure_password(password_length)

        return {
            'first_name': first_name,
            'last_name': last_name,
            'email': email,
            'password': password,
            'gender': 'female',
            'phone': '+1-555-0123',
            'nationality': 'US',
            'company': self._generate_company_name(),
            'full_name': f"{first_name} {last_name}",
            'generated_at': datetime.now().isoformat(),
            'fallback': True
        }

    def test_connection(self) -> bool:
        """
        Test connection to the randomuser.me API.

        Returns:
            bool: True if API is accessible
        """
        try:
            response = self.session.get(
                self.base_url,
                params={'results': 1},
                timeout=5
            )
            response.raise_for_status()
            return True

        except Exception as e:
            logger.error(f"API connection test failed: {e}")
            return False