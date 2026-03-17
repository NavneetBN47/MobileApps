import pytest

from SAF.misc.ssh_utils import SSH
import MobileApps.libs.ma_misc.conftest_misc as c_misc
from MobileApps.libs.flows.windows.jweb_event_service.flow_container import FlowContainer

@pytest.fixture(scope="session")
def jweb_event_service_test_setup(windows_test_setup):
    driver = windows_test_setup
    fc = FlowContainer(driver)
    return driver, fc