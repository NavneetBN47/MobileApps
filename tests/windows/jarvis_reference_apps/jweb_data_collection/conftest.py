import json
import pytest

from MobileApps.libs.flows.windows.jweb_data_collection.flow_container import FlowContainer
from MobileApps.libs.ma_misc import ma_misc

# Pytest app identifier
pytest.app_info = "JWEB_DATA_COLLECTION"


# Small helper functions
def _set_attrs(obj, src, keys):
    for key in keys:
        value = src.get(key) if isinstance(src, dict) else src[key]
        setattr(obj, key, value)

def _read_text(path):
    with open(path) as f:
        return f.read()

def _read_json(path):
    with open(path) as f:
        return json.load(f)


# Test data files (copied to Downloads)
def _upload_test_files(driver):
    test_files = [
        ("validcdmtree.json", "validcdmtree.json"),
        ("validcdmtree.json", "second_validcdmtree.json"),
        ("invalidcdmtree.json", "invalidcdmtree.json"),
        ("validledm.xml", "validledm.xml"),
        ("validledm.xml", "second_validledm.xml"),
        ("invalidledm.xml", "invalidledm.xml"),
        ("filteredNotificationObject.txt", "filteredNotificationObject.txt"),
        ("second_filteredNotificationObject.txt", "second_filteredNotificationObject.txt"),
        ("partialFiltered.txt", "partialFiltered.txt"),
        ("second_partialFiltered.txt", "second_partialFiltered.txt"),
    ]

    for src_name, dst_name in test_files:
        driver.ssh.send_file(
            ma_misc.get_abs_path(f"resources/test_data/jweb/{src_name}"),
            f"/Users/exec/Downloads/{dst_name}",
        )

def _cleanup_downloads(driver):
    for suffix in (".json", ".xml", ".txt"):
        driver.ssh.remove_file_with_suffix("/Users/exec/Downloads/", suffix)


# Session setup (driver + flow container)
@pytest.fixture(scope="session")
def jweb_data_collection_test_setup(windows_test_setup):
    driver = windows_test_setup
    return driver, FlowContainer(driver)


# Class setup (common attributes + test data + file uploads)
@pytest.fixture(scope="class", autouse=True)
def common_class_setup(request, jweb_data_collection_test_setup):
    cls = request.cls
    cls.driver, cls.fc = jweb_data_collection_test_setup
    cls.stack = request.config.getoption("--stack")

    for name, flow in cls.fc.fd.items():
        setattr(cls, name, flow)

    test_data = cls.fc.get_data_collection_test_data(cls.stack)
    cls.data_collection_test_data = test_data
    _set_attrs(
        cls,
        test_data,
        [
            "account_login_id","app_instance_id",
            "asset_type","device_id","stratus_user_id",
            "tenant_id","us_region_app_instance_id",
            "model_number","batching_max_event_notification",
            "batching_min_event_notification","batching_max_event_age","batching_evaluation_frequency",
        ],
    )
    cls.us_region_app_instance_id_1 = test_data.get("us_region_app_instance_id_1", cls.us_region_app_instance_id)
    cls.us_region_app_instance_id_2 = test_data.get("us_region_app_instance_id_2", cls.us_region_app_instance_id)
    cls.us_region_device_id = test_data.get("us_region_device_id", cls.device_id)
    cls.valid_cdm_tree = _read_json(ma_misc.get_abs_path("resources/test_data/jweb/validcdmtree.json"))
    cls.valid_ledm_tree = _read_text(ma_misc.get_abs_path("resources/test_data/jweb/validledm.xml"))

    _upload_test_files(cls.driver)
    cls.home.click_maximize()
    yield
    _cleanup_downloads(cls.driver)
    

# Per-test setup (restart app and re-select stack)
@pytest.fixture(scope="function", autouse=True)
def restart_app(request):
    cls = getattr(request, "cls", None)
    if cls is not None:
        cls.driver.restart_app()
        cls.fc.select_stack(cls.stack)
    yield

# Per-test default navigation (start on Weblet unless opted out)
@pytest.fixture(scope="function", autouse=True)
def default_start_on_weblet(request, restart_app):
    cls = getattr(request, "cls", None)
    if cls is not None and request.node.get_closest_marker("start_on_settings") is None:
        cls.home.select_top_nav_button("weblet_page_nav_btn")
    yield