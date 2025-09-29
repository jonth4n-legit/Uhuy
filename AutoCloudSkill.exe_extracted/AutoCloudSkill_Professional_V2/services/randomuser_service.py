"""
Professional RandomUser service for AutoCloudSkill.

This module provides comprehensive random user data generation:
- Integration with randomuser.me API
- Customizable user data generation
- Data validation and sanitization
- Fallback user generation
- Professional data structures

Author: Professional Rewrite by Claude Opus 4.1
Version: 2.0.0
"""

import random
import string
import logging
from typing import Dict, List, Optional, Any, Union
from dataclasses import dataclass
from datetime import datetime
from enum import Enum

import requests

from utils.logger import setup_application_logging, log_automation_step, performance_monitor
from utils.validators import validate_email, validate_name, sanitize_input
from config.settings import settings

logger = setup_application_logging('RandomUserService')

class Gender(Enum):
    """Gender options for user generation."""
    MALE = "male"
    FEMALE = "female"
    RANDOM = "random"

@dataclass
class UserData:
    """Comprehensive user data structure."""
    # Personal Information
    first_name: str
    last_name: str
    full_name: str
    gender: str

    # Contact Information
    email: str
    phone: str
    cell: str

    # Address Information
    street_number: str
    street_name: str
    city: str
    state: str
    country: str
    postcode: str

    # Additional Information
    date_of_birth: str
    age: int
    nationality: str
    picture_large: str
    picture_medium: str
    picture_thumbnail: str

    # Generated Information
    username: str
    password: str

    # Metadata
    generated_at: str
    source: str

    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary representation."""
        return {
            'first_name': self.first_name,
            'last_name': self.last_name,
            'full_name': self.full_name,
            'gender': self.gender,
            'email': self.email,
            'phone': self.phone,
            'cell': self.cell,
            'street_number': self.street_number,
            'street_name': self.street_name,
            'city': self.city,
            'state': self.state,
            'country': self.country,
            'postcode': self.postcode,
            'date_of_birth': self.date_of_birth,
            'age': self.age,
            'nationality': self.nationality,
            'picture_large': self.picture_large,
            'picture_medium': self.picture_medium,
            'picture_thumbnail': self.picture_thumbnail,
            'username': self.username,
            'password': self.password,
            'generated_at': self.generated_at,
            'source': self.source
        }

    def get_formatted_address(self) -> str:
        """Get formatted full address."""
        return f"{self.street_number} {self.street_name}, {self.city}, {self.state} {self.postcode}, {self.country}"

    def get_display_name(self) -> str:
        """Get display name for UI."""
        return f"{self.first_name} {self.last_name}"

class RandomUserService:
    """Professional random user data generation service."""

    def __init__(
        self,
        api_url: Optional[str] = None,
        timeout: int = 10,
        max_retries: int = 3
    ):
        """
        Initialize RandomUser service.

        Args:
            api_url: Custom API URL (default from settings)
            timeout: Request timeout in seconds
            max_retries: Maximum retry attempts
        """
        self.api_url = api_url or settings.randomuser_api_url
        self.timeout = timeout
        self.max_retries = max_retries

        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': f'AutoCloudSkill/{settings.version}',
            'Accept': 'application/json'
        })

        # Fallback data for offline generation
        self._fallback_names = self._load_fallback_names()
        self._fallback_domains = [
            'gmail.com', 'yahoo.com', 'hotmail.com', 'outlook.com',
            'protonmail.com', 'icloud.com'
        ]

        logger.info("RandomUser service initialized")

    def _load_fallback_names(self) -> Dict[str, List[str]]:
        """Load fallback name lists for offline generation."""
        return {
            'first_names_male': [
                'James', 'John', 'Robert', 'Michael', 'William', 'David', 'Richard', 'Charles',
                'Joseph', 'Thomas', 'Christopher', 'Daniel', 'Paul', 'Mark', 'Donald', 'Steven',
                'Kenneth', 'Joshua', 'Kevin', 'Brian', 'George', 'Timothy', 'Ronald', 'Jason'
            ],
            'first_names_female': [
                'Mary', 'Patricia', 'Jennifer', 'Linda', 'Elizabeth', 'Barbara', 'Susan', 'Jessica',
                'Sarah', 'Karen', 'Lisa', 'Nancy', 'Betty', 'Helen', 'Sandra', 'Donna',
                'Carol', 'Ruth', 'Sharon', 'Michelle', 'Laura', 'Sarah', 'Kimberly', 'Deborah'
            ],
            'last_names': [
                'Smith', 'Johnson', 'Williams', 'Brown', 'Jones', 'Garcia', 'Miller', 'Davis',
                'Rodriguez', 'Martinez', 'Hernandez', 'Lopez', 'Gonzalez', 'Wilson', 'Anderson',
                'Thomas', 'Taylor', 'Moore', 'Jackson', 'Martin', 'Lee', 'Perez', 'Thompson'
            ],
            'cities': [
                'New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix', 'Philadelphia',
                'San Antonio', 'San Diego', 'Dallas', 'San Jose', 'Austin', 'Jacksonville',
                'Fort Worth', 'Columbus', 'Charlotte', 'Indianapolis', 'San Francisco'
            ],
            'states': [
                'California', 'Texas', 'Florida', 'New York', 'Pennsylvania', 'Illinois',
                'Ohio', 'Georgia', 'North Carolina', 'Michigan', 'New Jersey', 'Virginia'
            ]
        }

    @performance_monitor("get_random_user")
    def get_random_user(
        self,
        gender: Union[Gender, str] = Gender.FEMALE,
        nationalities: Optional[List[str]] = None,
        password_length: Optional[int] = None
    ) -> Optional[UserData]:
        """
        Generate random user data.

        Args:
            gender: User gender preference
            nationalities: List of nationality codes (e.g., ['gb', 'us', 'es'])
            password_length: Custom password length

        Returns:
            UserData object or None if generation failed
        """
        # Convert string gender to enum
        if isinstance(gender, str):
            try:
                gender = Gender(gender.lower())
            except ValueError:
                gender = Gender.RANDOM

        # Use default nationalities from settings
        if nationalities is None:
            nationalities = settings.get_nationalities_list()

        # Use default password length from settings
        if password_length is None:
            password_length = settings.default_password_length

        log_automation_step(
            logger,
            "generate_random_user",
            "START",
            {
                "gender": gender.value,
                "nationalities": nationalities,
                "password_length": password_length
            }
        )

        # Try API first
        user_data = self._get_user_from_api(gender, nationalities, password_length)

        if user_data:
            log_automation_step(
                logger,
                "generate_random_user",
                "SUCCESS",
                {
                    "source": "api",
                    "name": user_data.full_name,
                    "email": user_data.email
                }
            )
            return user_data

        # Fallback to local generation
        logger.warning("API failed, using fallback generation")
        user_data = self._generate_fallback_user(gender, nationalities, password_length)

        if user_data:
            log_automation_step(
                logger,
                "generate_random_user",
                "SUCCESS",
                {
                    "source": "fallback",
                    "name": user_data.full_name,
                    "email": user_data.email
                }
            )
        else:
            log_automation_step(
                logger,
                "generate_random_user",
                "ERROR",
                {"error": "Both API and fallback generation failed"}
            )

        return user_data

    def _get_user_from_api(
        self,
        gender: Gender,
        nationalities: List[str],
        password_length: int
    ) -> Optional[UserData]:
        """
        Get user data from randomuser.me API.

        Args:
            gender: User gender
            nationalities: Nationality codes
            password_length: Password length

        Returns:
            UserData from API or None if failed
        """
        try:
            # Prepare parameters
            params = {
                'results': 1,
                'nat': ','.join(nationalities) if nationalities else 'gb,us,es',
                'inc': 'name,location,email,phone,cell,dob,picture,login'
            }

            if gender != Gender.RANDOM:
                params['gender'] = gender.value

            # Make request with retries
            for attempt in range(self.max_retries):
                try:
                    response = self.session.get(
                        self.api_url,
                        params=params,
                        timeout=self.timeout
                    )
                    response.raise_for_status()
                    break

                except requests.RequestException as e:
                    if attempt == self.max_retries - 1:
                        logger.error(f"API request failed after {self.max_retries} attempts: {e}")
                        return None
                    else:
                        logger.warning(f"API request attempt {attempt + 1} failed: {e}")

            # Parse response
            data = response.json()
            if not data.get('results'):
                logger.error("No results in API response")
                return None

            user_raw = data['results'][0]
            return self._parse_api_user(user_raw, password_length)

        except Exception as e:
            logger.error(f"Failed to get user from API: {e}")
            return None

    def _parse_api_user(self, user_raw: Dict[str, Any], password_length: int) -> UserData:
        """
        Parse raw API response into UserData object.

        Args:
            user_raw: Raw user data from API
            password_length: Desired password length

        Returns:
            Parsed UserData object
        """
        name = user_raw.get('name', {})
        location = user_raw.get('location', {})
        dob = user_raw.get('dob', {})
        picture = user_raw.get('picture', {})
        login = user_raw.get('login', {})

        # Extract name information
        first_name = sanitize_input(name.get('first', '').title())
        last_name = sanitize_input(name.get('last', '').title())
        full_name = f"{first_name} {last_name}"

        # Generate username and password
        username = self._generate_username(first_name, last_name)
        password = self._generate_password(password_length)

        # Extract location information
        street = location.get('street', {})
        street_number = str(street.get('number', ''))
        street_name = sanitize_input(street.get('name', ''))

        return UserData(
            first_name=first_name,
            last_name=last_name,
            full_name=full_name,
            gender=user_raw.get('gender', ''),
            email=user_raw.get('email', ''),
            phone=user_raw.get('phone', ''),
            cell=user_raw.get('cell', ''),
            street_number=street_number,
            street_name=street_name,
            city=sanitize_input(location.get('city', '')),
            state=sanitize_input(location.get('state', '')),
            country=sanitize_input(location.get('country', '')),
            postcode=str(location.get('postcode', '')),
            date_of_birth=dob.get('date', ''),
            age=dob.get('age', 0),
            nationality=user_raw.get('nat', ''),
            picture_large=picture.get('large', ''),
            picture_medium=picture.get('medium', ''),
            picture_thumbnail=picture.get('thumbnail', ''),
            username=username,
            password=password,
            generated_at=datetime.now().isoformat(),
            source='randomuser_api'
        )

    def _generate_fallback_user(
        self,
        gender: Gender,
        nationalities: List[str],
        password_length: int
    ) -> Optional[UserData]:
        """
        Generate user data using fallback method.

        Args:
            gender: User gender
            nationalities: Nationality codes
            password_length: Password length

        Returns:
            Generated UserData or None if failed
        """
        try:
            # Determine gender
            if gender == Gender.RANDOM:
                selected_gender = random.choice([Gender.MALE, Gender.FEMALE])
            else:
                selected_gender = gender

            # Generate name
            if selected_gender == Gender.MALE:
                first_name = random.choice(self._fallback_names['first_names_male'])
            else:
                first_name = random.choice(self._fallback_names['first_names_female'])

            last_name = random.choice(self._fallback_names['last_names'])
            full_name = f"{first_name} {last_name}"

            # Generate email
            username_base = f"{first_name.lower()}.{last_name.lower()}"
            domain = random.choice(self._fallback_domains)
            email = f"{username_base}@{domain}"

            # Generate address
            city = random.choice(self._fallback_names['cities'])
            state = random.choice(self._fallback_names['states'])
            street_number = str(random.randint(1, 9999))
            street_name = f"{random.choice(['Oak', 'Elm', 'Main', 'Park', 'First', 'Second'])} Street"

            # Generate other data
            username = self._generate_username(first_name, last_name)
            password = self._generate_password(password_length)
            age = random.randint(18, 65)
            nationality = random.choice(nationalities) if nationalities else 'us'

            return UserData(
                first_name=first_name,
                last_name=last_name,
                full_name=full_name,
                gender=selected_gender.value,
                email=email,
                phone=self._generate_phone(),
                cell=self._generate_phone(),
                street_number=street_number,
                street_name=street_name,
                city=city,
                state=state,
                country="United States",
                postcode=str(random.randint(10000, 99999)),
                date_of_birth=self._generate_birth_date(age),
                age=age,
                nationality=nationality,
                picture_large="",
                picture_medium="",
                picture_thumbnail="",
                username=username,
                password=password,
                generated_at=datetime.now().isoformat(),
                source='fallback_generator'
            )

        except Exception as e:
            logger.error(f"Failed to generate fallback user: {e}")
            return None

    def _generate_username(self, first_name: str, last_name: str) -> str:
        """Generate username from name."""
        base = f"{first_name.lower()}{last_name.lower()}"
        suffix = random.randint(10, 999)
        return f"{base}{suffix}"

    def _generate_password(self, length: int) -> str:
        """Generate secure password."""
        # Ensure password meets complexity requirements
        lowercase = string.ascii_lowercase
        uppercase = string.ascii_uppercase
        digits = string.digits
        special = "!@#$%^&*"

        # Ensure at least one character from each category
        password = [
            random.choice(uppercase),
            random.choice(lowercase),
            random.choice(digits),
            random.choice(special)
        ]

        # Fill remaining length
        all_chars = lowercase + uppercase + digits + special
        for _ in range(length - 4):
            password.append(random.choice(all_chars))

        # Shuffle the password
        random.shuffle(password)
        return ''.join(password)

    def _generate_phone(self) -> str:
        """Generate phone number."""
        area_code = random.randint(200, 999)
        exchange = random.randint(200, 999)
        number = random.randint(1000, 9999)
        return f"({area_code}) {exchange}-{number}"

    def _generate_birth_date(self, age: int) -> str:
        """Generate birth date based on age."""
        from datetime import datetime, timedelta

        birth_year = datetime.now().year - age
        birth_month = random.randint(1, 12)
        birth_day = random.randint(1, 28)  # Safe day for all months

        birth_date = datetime(birth_year, birth_month, birth_day)
        return birth_date.isoformat()

    def get_multiple_users(
        self,
        count: int,
        gender: Union[Gender, str] = Gender.RANDOM,
        nationalities: Optional[List[str]] = None
    ) -> List[UserData]:
        """
        Generate multiple random users.

        Args:
            count: Number of users to generate
            gender: Gender preference
            nationalities: Nationality codes

        Returns:
            List of UserData objects
        """
        users = []
        for i in range(count):
            user = self.get_random_user(gender, nationalities)
            if user:
                users.append(user)
            else:
                logger.warning(f"Failed to generate user {i + 1}/{count}")

        logger.info(f"Generated {len(users)}/{count} users")
        return users

    # Backward compatibility methods
    def get_random_user_dict(
        self,
        gender: str = 'female',
        nationalities: str = 'gb,us,es'
    ) -> Optional[Dict]:
        """
        Get random user as dictionary (backward compatibility).

        Args:
            gender: Gender string
            nationalities: Comma-separated nationality codes

        Returns:
            User data dictionary or None
        """
        nationality_list = [nat.strip() for nat in nationalities.split(',') if nat.strip()]
        user = self.get_random_user(gender, nationality_list)
        return user.to_dict() if user else None

# Export commonly used items
__all__ = [
    'Gender',
    'UserData',
    'RandomUserService'
]