from MobileApps.libs.flows.windows.hpx.flow_container import FlowContainer
from MobileApps.libs.flows.windows.hpx.utility.soft_assert import SoftAssert
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.tests.windows.hpx.ui_validation.ui_validation_helpers import *
from applitools.images import Eyes, BatchInfo

import pytest
import time

# ----------------      FUNCTION     ---------------------------
@pytest.fixture(name="eyes", scope="function")
def eyes_setup():
    """
    Basic Eyes setup. It'll abort test if it wasn't closed properly.
    """
    eyes = Eyes()
    # NOTE: Comment section and uncomment the next one to run the test locally. Secrets are stored in the CI/CD pipeline. 
    # PSCORE only = pscore_applitools_eyes_api_token
    # Load the system configuration and set Applitools API Key
    # applitools_api_token  = ma_misc.load_system_config_file()["applitools_api_key"]["pscore_applitools_eyes_api_token"]

    # if not applitools_api_token:
    #     raise EnvironmentError("Applitools API token is not set in the system configuration.") 
    
    # eyes.api_key = applitools_api_token

    # NOTE: Uncomment the following line to run the test locally.
    eyes.api_key = "n2tR08Lj4HHSIQfdgJINDVnZZGb49f4ZFb7bUq0uyiQ110"
    
    # Configure URL to the Eyes server
    eyes.server_url = "https://hpeyes.applitools.com/"
    eyes.configure.batch = BatchInfo("myHP UI Validation")
    yield eyes

    # If the test was aborted before eyes.close was called, ends the test as aborted.
    eyes.abort()


@pytest.fixture(scope="class", autouse=True)
def class_setup(request, windows_test_setup):
    """
    Setup code that initializes the driver and flow container.
    """
    
    cls = request.cls
    cls.driver = windows_test_setup
    cls.fc = FlowContainer(cls.driver)
    
    if request.config.getoption("--ota-test") is not None:
        time.sleep(10)
        cls.fc.fd["home"].click_to_install_signed_build()
        time.sleep(60)
        cls.fc.launch_myHP()
        time.sleep(5)
        cls.fc.ota_app_after_update()
    else:
        cls.fc.launch_myHP()
        time.sleep(3)

    yield

    if request.config.getoption("--ota-test") is not None:
        cls.fc.exit_hp_app_and_msstore()

    time.sleep(2)