import pytest
import logging
from MobileApps.libs.flows.windows.jweb_service_routing.flow_container import FlowContainer

pytest.app_info = "JWEB_SERVICE_ROUTING"

@pytest.fixture(scope="session")
def jweb_service_routing_test_setup(request, windows_test_setup):
    fc = FlowContainer(windows_test_setup)
    
    def session_cleanup():
        """
        Session-level cleanup to ensure Service Routing is properly closed.
        Runs automatically at end of test session regardless of test outcomes.
        """
        try:
            logging.info("Performing session-level Service Routing cleanup...")
            fc.reset_service_routing_state()
            if hasattr(windows_test_setup, 'close_app'):
                windows_test_setup.close_app()
                logging.info("Service Routing app closed successfully.")
        except Exception as e:
            logging.warning(f"Session cleanup failed: {e}")
    
    request.addfinalizer(session_cleanup)
    return windows_test_setup, fc

@pytest.fixture(scope="class", autouse=True)
def service_routing_class_setup(request, jweb_service_routing_test_setup):
    """Common class setup fixture for all service routing test suites"""
    cls = request.cls
    cls.driver, cls.fc = jweb_service_routing_test_setup
    cls.home = cls.fc.fd["home"]
    cls.service_routing = cls.fc.fd["service_routing"]
    cls.weblet_home = cls.fc.fd["weblet_home"]

@pytest.fixture(scope="function", autouse=True)
def service_routing_function_setup(request):
    """Common function setup fixture for all service routing test suites"""
    cls = request.cls
    cls.driver.restart_app()
    cls.home.select_webview_engine("webview2_chromium_engine")
    cls.home.select_settings_btn()
    cls.home.change_stack('Mock')
    cls.home.select_weblet_btn(raise_e=False)

@pytest.fixture(scope="function", autouse=True)
def service_routing_cleanup(request):
    """
    Auto-cleanup fixture for JWEB Service Routing tests.
    Runs after each test to ensure clean state for next test.
    """
    # Test execution happens here (yield allows test to run)
    yield
    
    # Cleanup runs after test completes
    try:
        logging.info("Performing function-level cleanup after test completion...")
        fc = request.cls.fc
        
        # Reset Service Routing to clean state
        fc.reset_service_routing_state()
        
        # Restart app to ensure completely clean state
        request.cls.driver.restart_app()
        logging.info("Service Routing app restarted for clean state.")
            
    except Exception as e:
        logging.warning(f"Service Routing cleanup failed: {e}")