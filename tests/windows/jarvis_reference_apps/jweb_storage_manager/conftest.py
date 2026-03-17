import pytest
from MobileApps.libs.flows.windows.jweb_storage_manager.flow_container import FlowContainer

pytest.app_info = "JWEB_STORAGE_MANAGER"
 
@pytest.fixture(scope="session")
def jweb_storage_manager_test_setup(windows_test_setup):
    return windows_test_setup, FlowContainer(windows_test_setup)


@pytest.fixture(scope="class")
def common_class_setup(request, jweb_storage_manager_test_setup):
    cls = request.cls
    if not cls:
        return

    cls.driver, cls.fc = jweb_storage_manager_test_setup
    cls.home, cls.storage_plugin = cls.fc.fd["home"], cls.fc.fd["storage_plugin"]
    cls.stack = request.config.getoption("--stack")
    cls.home.click_maximize()


@pytest.fixture(scope="function", autouse=True)
def navigate_to_storage_plugin(request):
    cls = getattr(request, "cls", None)
    if cls:
        cls.fc.navigate_to_storage_plugin()
        try:
            if not cls.home.verify_window_visual_state_maximized():
                cls.home.click_maximize()
        except Exception:
            pass
    yield