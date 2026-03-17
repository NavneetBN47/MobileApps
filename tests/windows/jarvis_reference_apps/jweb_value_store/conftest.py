import pytest
import time

from SAF.misc.ssh_utils import SSH
import MobileApps.libs.ma_misc.conftest_misc as c_misc
from MobileApps.libs.flows.windows.jweb_value_store.flow_container import FlowContainer

@pytest.fixture(scope="session")
def jweb_value_store_test_setup(windows_test_setup):
    driver = windows_test_setup
    fc = FlowContainer(driver)
    return driver, fc