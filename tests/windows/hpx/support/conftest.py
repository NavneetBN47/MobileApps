import pytest
from SAF.misc.ssh_utils import SSH

def pytest_addoption(parser):
    test_option = parser.getgroup('Windows HPX Support Test Parameters')
    test_option.addoption("--test-RN", action="store_true", default=False, help="Which feature to run the test on")
    test_option.addoption("--test-priority", action="store", default=None, help="which priority the test case you want to run")

def pytest_runtest_setup(item):
    priority = item.config.getoption("--test-priority")
    
    priority_mark = [mark.args[0] for mark in item.iter_markers(name="require_priority")]

    if (priority and priority not in priority_mark[0]):
        pytest.skip(f"Test does not run on priority: {priority}")