import pytest
import logging
import time

pytest.app_info = "POOBE"

class Test_friendly_url_victoria_Flow(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(self, olex_123_psw_test_setup, request):
        self = self.__class__
        self.driver, self.fc, self.printer_profile, self.hpid, self.ssh_client = olex_123_psw_test_setup
        self.printer_type = request.config.getoption("--printer-operation")
        self.browser_type = request.config.getoption("--browser-type")
        self.traffic_director = self.fc.fd["traffic_director"]
        
        self.friendly_url_victoria = {"dj6100":"714J5B", "dj6500":"714D5C", "envy6100":"714G5A", "envy6100e": "714L7A", "envy6100r": "714N0A",
                                      "envy6500":"714B6A","envy6500e":"714N7A"}
        self.result = []

        """
        testRail: https://hp-testrail.external.hp.com/index.php?/suites/view/3624&group_by=cases:section_id&group_order=asc&display_deleted_cases=0&group_id=4330019
        "envy6100r": "714N0A" This is paas printer "Use USB instead" button on HP software page was removed by design see: https://hp-jira.external.hp.com/browse/OLEX-1061
        """
    def test_01_friendly_url_for_victoria(self):
        if self.printer_profile not in ["victoria"]:
            pytest.skip("Skipping this test for all other printers except Victoria")
        for key, value in self.friendly_url_victoria.items():
            self.fc.clear_browsing_data_and_relaunch_flow(self.browser_type, url=self.traffic_director.td_url.replace("714N5A", key))
            time.sleep(3)
            logging.info("Friendly URL: {}".format(key))
            self.hpid.verify_privacy_popup(timeout=15)
            sku = self.driver.get_current_url().split("/")[-1]
            if sku not in value:
                self.result.append(False)
                logging.warning("Friendly URL:{} should not redirect to this SKU:{}".format(key, self.driver.get_current_url().split("/")[-1]))
            else:
                self.fc.fd["td_live_ui"].navigate_power_on_country_language_step()
                self.fc.fd["td_live_ui"].navigate_load_paper_step(self.printer_profile)
                self.fc.fd["td_live_ui"].fd["load_ink_td"].verify_web_page()
                self.fc.fd["td_live_ui"].fd["load_ink_td"].verify_install_ink_card_image(0)
                self.fc.fd["traffic_director"].verify_veneer_stepper()
                self.fc.fd["traffic_director"].click_veneer_stepper_step(2)
                self.fc.fd["td_live_ui"].fd["Load_paper_td"].verify_web_page()
                self.fc.fd["traffic_director"].click_veneer_stepper_step(3)
                assert self.fc.fd["td_live_ui"].fd["load_ink_td"].verify_web_page(raise_e=False) is False
                self.fc.fd["traffic_director"].click_next_btn()
                self.fc.fd["td_live_ui"].fd["load_ink_td"].verify_web_page(raise_e=False)
                self.fc.fd["td_live_ui"].navigate_install_ink_step(self.printer_profile)
                self.fc.fd["td_live_ui"].navigate_alignment_step(self.printer_profile)
                self.fc.fd["td_live_ui"].navigate_hp_software_step(self.printer_profile)
                self.fc.fd["td_live_ui"].fd["hp_software"].click_trouble_installing_get_tips_btn()
                self.fc.fd["td_live_ui"].fd["hp_software"].click_trobleshooting_modal_close_btn()
                self.fc.fd["td_live_ui"].fd["hp_software"].click_install_hp_smart_btn()
        if False in self.result:
            pytest.fail("Friendly URL is not working for Victoria printer check logs for more details")