import logging
import pytest
import json
from MobileApps.libs.flows.windows.jweb_configuration_service_winui.flow_container import FlowContainer
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.tests.conftest import clean_up_utility_method

pytest.app_info = "JWEB_CONFIGURATION_SERVICE_WINUI"

@pytest.fixture(scope="session")
def jweb_configuration_service_test_setup(windows_test_setup):
    fc = FlowContainer(windows_test_setup)
    return windows_test_setup, fc

@pytest.fixture(scope="class", autouse=True)
def configuration_service_test_data(request):
	"""
	This fixture loads the test data for the configuration service tests from a JSON file and 
	sets it as class variables for the test classes
	"""
	stack = request.config.getoption("stack")

	with open(ma_misc.get_abs_path("resources/test_data/jweb/configuration_service_test_data.json"),encoding="utf-8") as fp:
		config_data = json.load(fp)[stack]

	request.cls.provider_name = config_data["provider_name"]
	request.cls.sdk_key = config_data["sdk_key"]
	request.cls.context_key = config_data["context_key"]

@pytest.fixture(scope="function")
def initialize_without_bootstrap_file(request):
	"""
	Fixture to initialize the configuration service with the provider, SDK key, and context key before each test
	"""
	cls = request.cls
	fc = getattr(cls, "fc", None)
	if fc:
		fc.initialize_configuration_service_without_bootstrap_file(cls.provider_name, cls.sdk_key, cls.context_key)

@pytest.fixture(scope="function", autouse=True)
def clean_up(request):
	"""
	Fixture to clean up after each test execution
	"""
	yield
	try:
		clean_up_utility_method(request)
		cls = request.cls
		driver = getattr(cls, "driver", None)
		if driver:
			driver.restart_app()
	except Exception as e:
		logging.exception("Cleanup failed during teardown")