import re
import time
import os
import json
import logging
import requests
import pytest

from collections import OrderedDict
from MobileApps.libs.ma_misc import ma_misc

class LocaleUtilities:
    
    def __init__(self, max_cache_size=100):
        """Initialize with LRU cache that has size limits."""
        self._max_cache_size = max_cache_size
        self._mfe_locale_cache = OrderedDict()

    def _add_to_cache(self, cache_key, data):
        """Add to cache with LRU eviction."""
        if cache_key in self._mfe_locale_cache:
            # Move to end (most recently used)
            self._mfe_locale_cache.move_to_end(cache_key)
        else:
            self._mfe_locale_cache[cache_key] = data
            # Remove oldest items if cache is full
            while len(self._mfe_locale_cache) > self._max_cache_size:
                self._mfe_locale_cache.popitem(last=False)

    def _get_from_cache(self, cache_key):
        """Get data from cache with LRU access tracking."""
        if cache_key in self._mfe_locale_cache:
            # Move to end (most recently used)
            self._mfe_locale_cache.move_to_end(cache_key)
            return self._mfe_locale_cache[cache_key]
        return None
    
    def fetch_mfe_locale(self, mfe_repo_name, language, branch="main", org=None):
        """
        Fetch locale files from MFE GitHub repositories at runtime.
        
        Args:
            mfe_repo_name (str): The full repository name (e.g., "react-pc-pencontrol-mfe")
            language (str): The language code (e.g., "en-US", "fr-FR")
            branch (str): The branch name (default: "main")
            org (str, optional): GitHub organization name (default: "pc-hw-enablers")
            
        Returns:
            dict: The parsed JSON content as a Python dictionary
            
        Raises:
            pytest.fail: If locale file cannot be fetched after trying fallbacks
        """
        # Create cache key including org for uniqueness
        org = org or self._get_default_mfe_org()
        cache_key = f"{org}:{mfe_repo_name}:{language}:{branch}"

        # Return cached result if available
        if cache_key in self._mfe_locale_cache:
            logging.info(f"Using cached locale data for {cache_key}")
            return self._mfe_locale_cache[cache_key]
        
        cached_data = self._get_from_cache(cache_key)
        if cached_data is not None:
            logging.info(f"Using cached locale data for {cache_key}")
            return cached_data

        # GitHub Enterprise base configuration
        base_url = self._get_github_base_url()

        logging.info(f"Fetching from organization: {org}")

        # Get GitHub token from system config or environment
        github_token = self._get_github_token()
        headers = {}
        if github_token:
            headers['Authorization'] = f'token {github_token}'

        # Convert language format from hyphen to underscore (e.g., "en-US" -> "en_US")
        language_filename = language.replace('-', '_')

        # Try to fetch the exact language file first
        url = f"{base_url}/{org}/{mfe_repo_name}/{branch}/src/assets/locale/{language_filename}.json"

        try:
            logging.info(f"Fetching locale file from: {url}")
            response = requests.get(url, headers=headers, timeout=30)

            if response.status_code == 200:
                locale_data = response.json()
                self._mfe_locale_cache[cache_key] = locale_data
                self._add_to_cache(cache_key, locale_data)
                logging.info(f"Successfully fetched locale data for {language} from {mfe_repo_name}")
                return locale_data
            elif response.status_code == 404:
                # Try fallback to short language code (e.g., "en" instead of "en-US")
                short_language = language.split('-')[0] if '-' in language else None
                if short_language and short_language != language:
                    fallback_url = f"{base_url}/{org}/{mfe_repo_name}/{branch}/src/assets/locale/{short_language}.json"
                    logging.info(f"Primary language file not found, trying fallback: {fallback_url}")

                    fallback_response = requests.get(fallback_url, headers=headers, timeout=30)
                    if fallback_response.status_code == 200:
                        locale_data = fallback_response.json()
                        # Cache with original key for future requests
                        self._mfe_locale_cache[cache_key] = locale_data
                        self._add_to_cache(cache_key, locale_data)
                        logging.info(f"Successfully fetched fallback locale data for {short_language} from {mfe_repo_name}")
                        return locale_data
                    elif fallback_response.status_code == 404:
                        pytest.fail(f"Locale file not found for both {language} and {short_language} in {mfe_repo_name}. "
                                   f"Checked URLs: {url} and {fallback_url}")
                    else:
                        pytest.fail(f"Failed to fetch fallback locale file from {fallback_url}. "
                                   f"Status: {fallback_response.status_code}, Response: {fallback_response.text}")
                else:
                    pytest.fail(f"Locale file not found for {language} in {mfe_repo_name}. "
                               f"URL: {url}. No fallback available for single-part language code.")
            elif response.status_code == 401:
                pytest.fail(f"Authentication failed when accessing {url}. "
                           f"Please check your GITHUB_TOKEN environment variable.")
            elif response.status_code == 403:
                pytest.fail(f"Access forbidden when accessing {url}. "
                           f"Please check your GitHub permissions and token scope.")
            else:
                pytest.fail(f"Failed to fetch locale file from {url}. "
                           f"Status: {response.status_code}, Response: {response.text}")

        except requests.exceptions.Timeout:
            pytest.fail(f"Timeout occurred while fetching locale file from {url}. "
                       f"Please check your network connection.")
        except requests.exceptions.ConnectionError:
            pytest.fail(f"Connection error occurred while fetching locale file from {url}. "
                       f"Please check your network connection and VPN status.")
        except requests.exceptions.RequestException as e:
            pytest.fail(f"Network error occurred while fetching locale file from {url}: {str(e)}")
        except json.JSONDecodeError as e:
            pytest.fail(f"Invalid JSON format in locale file from {url}: {str(e)}")
        except Exception as e:
            pytest.fail(f"Unexpected error occurred while fetching locale file from {url}: {str(e)}")

    def _get_default_mfe_org(self):
        """
        Get the default MFE organization from system config or fallback to default.
        
        Returns:
            str: Default organization name
        """
        try:
            # Try to get from system config first
            sys_config = ma_misc.load_system_config_file()
            mfe_config = sys_config.get("mfe_config", {})
            return mfe_config.get("default_organization", "pc-hw-enablers")
        except Exception:
            # Fallback to default if config loading fails
            return "pc-hw-enablers"

    def _get_github_base_url(self):
        """
        Get GitHub Enterprise base URL from system config or use default.
        
        Returns:
            str: GitHub Enterprise base URL
        """
        try:
            sys_config = ma_misc.load_system_config_file()
            mfe_config = sys_config.get("mfe_config", {})
            return mfe_config.get("github_base_url", "https://raw.github.azc.ext.hp.com")
        except Exception:
            return "https://raw.github.azc.ext.hp.com"

    def _get_github_token(self):
        """
        Get GitHub token from system config or environment variable.
        
        Returns:
            str or None: GitHub token if available
        """
        try:
            # First try system config
            sys_config = ma_misc.load_system_config_file()
            token = sys_config.get("github_enterprise_token")
            if token:
                return token
        except Exception:
            pass

        # Fallback to environment variable
        return os.getenv('GITHUB_TOKEN')

    def clear_mfe_locale_cache(self):
        """
        Clear the MFE locale cache. Useful for clearing cache between test runs.
        """
        self._mfe_locale_cache.clear()
        logging.info("MFE locale cache cleared")
