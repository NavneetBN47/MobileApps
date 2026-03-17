import pytest
import time
import traceback
from MobileApps.libs.flows.web.instant_ink import value_proposition
from MobileApps.libs.flows.web.ows import live_ui_1_0

pytest.app_info = "OWS"

class Test_06_timeout_liveui_page(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(self, ows_test_setup):
        self = self.__class__
        self.driver, self.emu_platform, self.ows_printer, self.fc, self.yeti_fc, self.status_and_login_info = ows_test_setup
        self.request = self.driver.session_data['request']
        self.load_ink = self.fc.flow["load_ink"]
        self.country_config = self.fc.flow["country_language"]
        self.calibration = self.fc.flow["calibration"]
        self.value_prop = value_proposition.ValueProposition(self.driver)
        self.ui_1 = live_ui_1_0.LiveUI_1_0(self.driver, self.ows_printer)

    def test_01_verify_timeout_ink_step(self, request):
        """ 
        Description:
        
        Currently this test case only for Taccola, taiji, paleromo, verona, infinity and vasari printers 
        Test case under Automation/LiveUI1.0/Extended Regression
        1. Wait 180s for skip btn to appear on Country and language screen only for palermo and verona
        2. Load paper for palermo, verona, taiji and taccola.
        3. Click on skip btn only for Infinity and vasari.
        4. Wait 180s for palermo, verona, taiji and taccola and then Click on skip btn on install ink screen
           no wait time for infinity and vasari.
        5. Verify enroll in install ink offer page after clicking on skip install ink btn.
        """

        if self.request.config.getoption("--emu-printer") in ["palermo", "verona"]:
            self.__skip_btn_flow_palermo_verona(request)
        if self.request.config.getoption("--emu-printer") == "taccola":
            self.__skip_btn_flow_taccola()
        if self.request.config.getoption("--emu-printer") == "taiji":
            self.__skip_btn_flow_taiji()
        if self.request.config.getoption("--emu-printer") in ["infinity", "vasari"]:
            self.__skip_btn_flow_infinity_vasari()
            
            
    ################## Private Function ##########################

    def __skip_btn_flow_infinity_vasari(self):
        self.fc.navigate_ows(self.ows_printer, stop_at="loadMainTray")
        # to skip load paper page
        self.load_ink.skip_installing_btn()
        # Second time to skip install ink page
        self.load_ink.skip_installing_btn()
        self.value_prop.verify_enroll_instant_ink_page()

    def __skip_btn_flow_taiji(self):
        self.load_ink.skip_installing_btn()
        self.ui_1.navigate_load_paper()
        self.value_prop.verify_enroll_instant_ink_page()

    def __skip_btn_flow_taccola(self):
        self.ui_1.navigate_load_paper()
        self.load_ink.skip_installing_btn()
        self.value_prop.verify_enroll_instant_ink_page()

    def __skip_btn_flow_palermo_verona(self, request):
        self.country_config.click_set_this_later_btn()
        self.load_ink.skip_installing_btn()
        self.ui_1.navigate_load_paper()
        self.calibration.skip_calibration()
        if request.config.getoption("--emu-printer") == "palermo":
            self.value_prop.verify_enroll_instant_ink_page()