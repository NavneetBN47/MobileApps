import pytest
import logging

@pytest.fixture(scope="function", autouse=False)
def clean_up(request):

    def _clean_up(home_url):
        driver = request.cls.driver

        # close emulator window
        driver.close_window("OWSEmuPrinter")
        # back to main emulator window
        driver.navigate(home_url)
        
        try:
            request.cls.ows_emulator.dismiss_banner(raise_e=False)
        except NameError:
            logging.warn("you need to have ows_emulator object created to run dismiss_banner()")

    return _clean_up