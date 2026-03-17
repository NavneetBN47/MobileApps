import os
import logging
import pytest
from SAF.misc.ssh_utils import SSH
import MobileApps.libs.ma_misc.conftest_misc as c_misc
from MobileApps.libs.flows.windows.jweb_auth.flow_container import FlowContainer

def pytest_addoption(parser):
    auth_group = parser.getgroup('JWEB Auth Test Parameters')
    auth_group.addoption(
        "--auth-cleanup",
        action="store_true",
        default=False,
        help="Flag to enable Auth plugin cleanup on test failure",
    )

@pytest.fixture(scope="session")
def jweb_auth_plugin_test_setup(request, windows_test_setup):
    driver = windows_test_setup
    fc = FlowContainer(driver)

    def session_cleanup():
        """
        Session-level cleanup to leave Auth plugin in a clean state and close the app.
        Runs regardless of test outcomes.
        """
        try:
            logging.info("Performing session-level Auth cleanup...")
            reset_auth_state(fc)
            if hasattr(driver, "close_app"):
                driver.close_app()
                logging.info("Auth app closed successfully.")
        except Exception as e:
            logging.warning(f"Session cleanup failed: {e}")

    request.addfinalizer(session_cleanup)
    return driver, fc

def reset_auth_state(fc):
    """
    Reset Auth plugin to a clean state: ensure Stratus option, restart, open plugin, logout, and prime subscriber.
    This prevents cross-test leakage of login/session state.
    """
    try:
        logging.info("Resetting Auth plugin state for clean test environment...")
        home = fc.fd["home"]
        auth = fc.fd["auth_plugin"]

        home.select_top_nav_button("options_nav_btn")
        home.select_stratus_using_browser_option()
        fc.driver.restart_app()
        home.select_top_nav_button("tests_nav_btn")
        try:
            auth.select_logout_btn()
            logging.info("Logged out of Auth plugin during reset.")
        except Exception as e:
            logging.debug(f"No logout needed during reset: {e}")

        home.select_top_nav_button("jweb_nav_btn")
        home.select_reference_btn()
        home.select_plugins_tab_from_menu()
        home.select_plugin_from_home("Auth")

        try:
            auth.select_set_subscriber_btn()
        except Exception as e:
            logging.debug(f"Unable to prime subscriber state: {e}")

        logging.info("Auth plugin state reset completed successfully.")
    except Exception as e:
        logging.warning(f"Failed to reset Auth plugin state: {e}")

def capture_auth_failure_state(fc, attachment_path, test_name):
    """
    Capture screenshot and page source for debugging failed Auth tests.
    """
    try:
        logging.info("Capturing Auth failure state for debugging...")
        screenshot_path = os.path.join(attachment_path, f"auth_failure_{test_name}.png")
        fc.driver.save_screenshot(screenshot_path)

        source_path = os.path.join(attachment_path, f"auth_source_{test_name}.html")
        with open(source_path, "w") as f:
            f.write(fc.driver.page_source)

        logging.info("Auth failure state captured successfully.")
    except Exception as e:
        logging.warning(f"Failed to capture Auth failure state: {e}")

@pytest.fixture(scope="function", autouse=True)
def auth_cleanup(request):
    """
    Auto-cleanup for Auth tests. On failure (and when --auth-cleanup is enabled):
    - Capture failure artifacts
    - Reset Auth plugin state
    - Restart app for a clean next test
    """

    def perform_cleanup():
        if request.session.testsfailed and request.config.getoption("--auth-cleanup"):
            logging.info(f"Auth test failed: {request.node.name}")
            logging.error("Auth test failure detected. Starting cleanup procedure...")
            try:
                fc = request.cls.fc
                attachment_root_path = pytest.test_result_folder + "attachment/"
                if not os.path.isdir(attachment_root_path):
                    os.makedirs(attachment_root_path)

                capture_auth_failure_state(fc, attachment_root_path, request.node.name)
                reset_auth_state(fc)
                request.cls.driver.restart_app()
                logging.info("Auth app restarted for clean state.")
            except Exception as e:
                logging.warning(f"Auth cleanup failed: {e}")
        else:
            logging.debug("No Auth cleanup needed - test passed or cleanup not enabled.")

    request.addfinalizer(perform_cleanup)
    yield

@pytest.fixture(scope="class", autouse=True)
def class_setup(request, jweb_auth_plugin_test_setup, utility_web_session):
    """
    Common class-level setup for all Auth test suites.
    Sets up driver, flow container, and page objects.
    """
    cls = request.cls
    cls.driver, cls.fc = jweb_auth_plugin_test_setup
    cls.web_driver = utility_web_session
    cls.home = cls.fc.fd["home"]
    cls.auth_plugin = cls.fc.fd["auth_plugin"]
    cls.hpid = cls.fc.fd["hpid"]
    cls.stack = request.config.getoption("--stack")
    cls.home.click_maximize()
    
    # Load test accounts if needed
    test_account = cls.fc.get_jweb_login_event_test_data(cls.stack)
    cls.username = test_account["account_01"]["username"]
    cls.password = test_account["account_01"]["password"]
    cls.tenant_id = test_account["account_01"]["tenant_id"]
    cls.username_1 = test_account["account_02"]["username"]
    cls.password_1 = test_account["account_02"]["password"]
    cls.tenant_id_1 = test_account["account_02"]["tenant_id"]
    
    # Expected tenant IDs for validation
    cls.expected_tenant_ids = ["2f4981da-9fc2-4dab-8f05-3dfba5b154af", 
                                "91547a10-4a36-45b7-b423-8b2baac97976", 
                                "66e7a414-cef9-41df-bd26-ca943b4330d4",
                                "8b524804-059f-4f99-a7e4-e003de93b1eb"]

@pytest.fixture(scope="function", autouse=True)
def navigate_to_auth_plugin(request):
    """
    Common function-level fixture to navigate to Auth Plugin with Stratus option.
    Runs before each test to ensure clean state.
    """
    cls = request.cls
    logging.info("Navigating to Auth Plugin")
    cls.home.select_top_nav_button("options_nav_btn")
    cls.home.select_stratus_using_browser_option()
    cls.driver.restart_app()
    cls.home.select_top_nav_button("tests_nav_btn")
    cls.auth_plugin.select_logout_btn()
    cls.home.select_top_nav_button("jweb_nav_btn")
    cls.home.select_reference_btn()
    cls.home.select_plugins_tab_from_menu()
    cls.home.select_plugin_from_home("Auth")
    cls.auth_plugin.select_set_subscriber_btn()

def navigate_to_auth_plugin_with_option(cls, browser_option_method, set_subscriber=False):
    """
    Helper function to navigate to Auth Plugin with specified browser option.
    """
    logging.info("Navigating to Auth Plugin")
    cls.home.select_top_nav_button("options_nav_btn")
    browser_option_method()
    cls.driver.restart_app()
    cls.home.select_top_nav_button("tests_nav_btn")
    cls.auth_plugin.select_logout_btn()
    cls.home.select_top_nav_button("jweb_nav_btn")
    cls.home.select_reference_btn()
    cls.home.select_plugins_tab_from_menu()
    cls.home.select_plugin_from_home("Auth")
    if set_subscriber:
        cls.auth_plugin.select_set_subscriber_btn()

@pytest.fixture(scope="function")
def navigate_to_auth_plugin_stratus(request):
    """
    Navigate to Auth Plugin with Stratus option (non-autouse version).
    Use this fixture explicitly when needed.
    """
    cls = request.cls
    navigate_to_auth_plugin_with_option(cls, cls.home.select_stratus_using_browser_option, set_subscriber=True)


@pytest.fixture(scope="function")
def navigate_to_auth_plugin_one_cloud(request):
    """
    Navigate to Auth Plugin with One Cloud option.
    """
    cls = request.cls
    navigate_to_auth_plugin_with_option(cls, cls.home.select_one_cloud_using_browser_option, set_subscriber=False)

def login_to_hpid(cls, tenant_id, log_message):
    """
    Helper function to login to HPID with specified tenant ID.
    """
    logging.info(log_message)
    cls.auth_plugin.control_auth_token_switches([False, True, True, False, False])
    cls.auth_plugin.send_text_to_tenant_id_textbox(tenant_id)
    cls.auth_plugin.select_auth_get_token_test()
    cls.fc.verify_with_pop_up_along_with_token_value(cls.username_1, cls.password_1, cls.web_driver)

@pytest.fixture()
def login_to_hpid_with_valid_tenant_id(request):
    """
    Login to HPID with valid tenant ID.
    """
    cls = request.cls
    login_to_hpid(cls, cls.tenant_id_1, "Precondition to Logging into hp with valid tenant_id")

@pytest.fixture()
def login_to_hpid_with_blank_tenant_id(request):
    """
    Login to HPID with blank tenant ID.
    """
    cls = request.cls
    login_to_hpid(cls, "", "Precondition to Logging into hp with blank tenant_id")

@pytest.fixture()
def logout_from_hpid(request):
    """
    Logout from HPID - verifies logged out state first.
    """
    cls = request.cls
    cls.auth_plugin.select_auth_logged_in_test()
    auth_logged_in_result = cls.auth_plugin.get_auth_is_logged_in_result_false()
    assert auth_logged_in_result["value"] == False
    cls.auth_plugin.select_auth_logout_test()