import pytest

pytest.app_info = "POOBE"

class Test_poobe_Flow(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(self, olex_123_psw_test_setup, request):
        self = self.__class__
        self.driver, self.fc, self.printer_profile, self.hpid, self.ssh_client = olex_123_psw_test_setup
        self.printer_type = request.config.getoption("--printer-operation")
        self.traffic_director = self.fc.fd["traffic_director"]
        self.td_live_ui = self.fc.fd["td_live_ui"]
        
        """
        testRail: https://hp-testrail.external.hp.com/index.php?/suites/view/3624&group_by=cases:section_id&group_order=asc&display_deleted_cases=0&group_id=3809236 
        """
    def test_01_save_page_context_between_all_tabs(self):
        if self.printer_profile.startswith(("cherry", "lotus")):
            pytest.skip("Skipping test - only cherry/lotus specific tests should run on cherry/lotus profiles")
        self.fc.verify_traffic_director_load_paper_step()
        self.traffic_director.click_printer_features_btn()
        self.traffic_director.verify_learn_tab_printer_features()
        self.traffic_director.verify_learn_tab_hp_plus_instant_ink()
        self.traffic_director.verify_learn_tab_printer_features_is_default_selected_shown()
        self.traffic_director.click_setup_tab()
        self.fc.verify_traffic_director_load_paper_step()
        self.traffic_director.click_printer_features_btn()
        self.traffic_director.verify_learn_tab_printer_features()
        self.traffic_director.verify_learn_tab_print_features_content()
        self.traffic_director.verify_learn_tab_hp_plus_instant_ink()
        self.traffic_director.click_printer_features_btn_hp_plus_instant_ink()
        self.traffic_director.verify_learn_tab_instant_ink_content()
        self.traffic_director.click_setup_tab()
        self.traffic_director.click_printer_features_btn()
        self.traffic_director.verify_learn_tab_instant_ink_is_default_selected_shown()
        self.traffic_director.verify_learn_tab_instant_ink_content()
        self.traffic_director.click_get_help_btn()
        self.traffic_director.verify_get_help_connectivity_subtab_content()
        self.traffic_director.click_get_help_connectivity_subtab_content()
        self.traffic_director.click_get_help_subtab_hp_smart_installation()
        self.traffic_director.click_supported_os_drop_down_on_subtab_hp_smart_installantion()
        self.traffic_director.verify_hp_smart_installation_subtab()
        self.traffic_director.click_setup_tab()
        self.traffic_director.click_get_help_btn()
        self.traffic_director.verify_hp_smart_installation_subtab()
        self.traffic_director.click_setup_tab()
        self.traffic_director.click_next_btn()
        self.td_live_ui.navigate_install_ink_step(self.printer_profile)
        self.fc.verify_traffic_director_print_alignment_step()
        self.traffic_director.click_printer_features_btn()
        self.traffic_director.verify_learn_tab_hp_plus_instant_ink()
        self.traffic_director.verify_learn_tab_instant_ink_content()
        self.traffic_director.click_setup_tab()
        self.fc.verify_traffic_director_print_alignment_step()
        self.traffic_director.click_get_help_btn()
        self.traffic_director.verify_hp_smart_installation_subtab()
        self.traffic_director.click_setup_tab()
        self.fc.verify_traffic_director_print_alignment_step()