import pytest
import logging
pytest.app_info = "POOBE"

class Test_poobe_Flow(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(self, olex_123_psw_test_setup, request):
        self = self.__class__
        self.driver, self.fc, self.printer_profile, self.hpid, self.ssh_client = olex_123_psw_test_setup
        self.stack = request.config.getoption("--stack")
        self.printer_type = request.config.getoption("--printer-operation")
        self.browser = request.config.getoption("--browser-type")
        self.traffic_director = self.fc.fd["traffic_director"]
        
        self.marconi_skus = ['403V9B', '403W0C', '403W1B', '403W8B', '403X0A', '403X1A', '403X2A', '403X3A', '403X5B', 
                             '403X7B', '403X8B', '403Y0B', '403Y1B', '403Y3B', '404K5C', '404K6C', '404K9C', '404L0C', 
                             '404L1B', '404L5C', '404L6C', '404L7C', '404L8B', '404M0A', '404M5B', '404M6B', '404N0B', 
                             '4V2L9A', '4V2M9C', '4V2N5C', '4V2N6C', '4V2N7C']
        self.moreto_skus = ['405U5A', '405W1C', '405W2C', '405W3C', '405W4B', '405W0C', '405U4B', '405U3B', '405U7B', 
                            '405T6A', '405U8B', '68K80B', '68K75B', '68K75C', '40Q48B', '40Q45B','40Q49B','40Q35A',
                            '40Q47B','40Q50A','40Q51A']
        self.kebin_skus = ["537P5B", "537P5C", "537P6A", "537P6B", "53N94B", "53N94C", "53N95B"]
        self.victoria_skus = ['714B5A', '714B6A', '714D5A', '714D6A', '714D7A', '714D8A', '714D9A', '714F0A', '714N5A', 
                              '714N7A', '714N8A', '714N9B', '714P2A', '714G5A', '714G6A', '714J5A', '714J6A', '714J7A', 
                              '714J8A', '714L5A', '714L7A', '714L8B', '714M1A', '714N0A']
        """
        This is an Automation Only test. TO validate that every traffic director SKU re-directs user to correct page.
        For Marconi, Kebin, Moreto, Victoria
        """
    def test_01_traffic_director_sku_landing_page_tests(self):
        if self.printer_profile.startswith(("cherry", "lotus")):
            pytest.skip("Skipping test - only cherry/lotus specific tests should run on cherry/lotus profiles")
        if self.stack == "prod":
            pytest.skip("Skipping this test for PROD stack")
        sku_list = self.get_skus_based_on_printer()
        if False in self.validate_given_sku_re_direction(sku_list):
            pytest.fail("Check log one or more SKU did not re-direct to coreect Printer Setup Website")

    ############################# Private Function #######################################

    def validate_given_sku_re_direction(self, sku_list):
        resuk = []
        for i in sku_list:
            self.fc.clear_browsing_data_and_relaunch_flow(self.browser, "onboardingcenter.{}.portalshell.int.hp.com/{}".format(self.stack, i))
            logging.info("Printer Profile: {}, SKU: {}".format(self.printer_profile, i))
            self.hpid.handle_privacy_popup(timeout=10, delay=3)
            resuk.append(self.traffic_director.verify_start_setup_btn(raise_e=False))
            resuk.append(self.traffic_director.verify_watch_video_btn(raise_e=False))
            resuk.append(self.traffic_director.verify_country_language_selector_link(raise_e=False))
            if False in resuk:
                logging.info("entered SKU: {} for {} in url does not redirect user to Printer Setup Website".format(i, self.printer_profile))
        return resuk
    
    def get_skus_based_on_printer(self):
        if self.printer_profile == "marconi":
            return self.marconi_skus
        elif self.printer_profile == "kebin":
            return self.kebin_skus
        elif self.printer_profile == "moreto":
            return self.moreto_skus
        elif self.printer_profile == "victoria":
            return self.victoria_skus
        else:
            return None
            