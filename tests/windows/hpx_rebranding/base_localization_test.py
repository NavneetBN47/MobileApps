import logging

class BaseLocalizationTest:
    """Base class for localization tests that need to manage system language"""
    
    @classmethod
    def setup_class(cls):
        """Store original system language for cleanup"""
        try:
            result = cls.fc.driver.ssh.send_command("(Get-UICulture).Name")
            cls.original_language = result['stdout'].strip()
            logging.info(f"Original system language: {cls.original_language}")
        except Exception as e:
            logging.warning(f"Could not determine original language: {e}")
            cls.original_language = "en-US"  # Default fallback

    @classmethod
    def teardown_class(cls):
        """Restore original system language"""
        try:
            logging.info(f"Restoring original language: {cls.original_language}")
            cls.fc.change_remote_tv_language(cls.original_language)
            cls.fc.restart_myHP()
            logging.info("Language restored successfully")
        except Exception as e:
            logging.error(f"Failed to restore original language: {e}")