import pytest

@pytest.fixture(scope="session", autouse=True)
def inject_journey_testsuite_data(record_testsuite_property):
    record_testsuite_property("suite_test_category", "ECP Functionality")
