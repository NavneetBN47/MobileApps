def pytest_addoption(parser):
    test_option = parser.getgroup('Windows HPAI Test Parameters')
    test_option.addoption("--app-type", action="store", default="debug", help="The app version you would like to run")