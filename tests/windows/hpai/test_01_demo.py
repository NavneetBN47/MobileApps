import time
import pytest
from SAF.misc import saf_misc
from MobileApps.libs.ma_misc import ma_misc
import MobileApps.resources.const.windows.const as w_const


pytest.app_info = "HPAI"
class Test_Suite_01_Home_NavBar(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, windows_test_setup):
        cls = cls.__class__
        cls.driver = windows_test_setup

    def test_01_demo(self): 
        time.sleep(5)
        self.driver.wdvr.find_element("xpath", "//*[@AutomationId='btnManageChoices']").click()
        time.sleep(3)
        self.driver.wdvr.find_element("xpath", "//*[@AutomationId='btnBack']").click()
        time.sleep(2)
        self.driver.wdvr.find_element("xpath", "//*[@AutomationId='btnAcceptAll']").click()
        time.sleep(2)
