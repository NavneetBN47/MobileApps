import pytest
import random
from MobileApps.libs.flows.windows.hpx_rebranding.flow_container import FlowContainer


pytest.app_info =  "HPX"
class Test_Suite_02_Add_Printers_In_Diff_Ways(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, windows_test_setup, load_printers_session):
        cls = cls.__class__
        cls.driver = windows_test_setup
        cls.p = load_printers_session
        cls.ip = cls.p.get_printer_information()["ip address"]
        cls.hostname = cls.p.get_printer_information()['serial number']
        cls.fc = FlowContainer(cls.driver)
        cls.printer_name = cls.p.get_printer_information()["model name"]

        # Initializing Printer2
        # cls.p2 = cls.fc.initialize_printer()
        # cls.hostname2 = cls.p2.get_printer_information()['serial number']
        # cls.ip2 = cls.p2.get_printer_information()["ip address"]

        
    @pytest.mark.regression
    def test_01_add_printer_via_ip_or_hostname_C53365410_C53175451(self):
        """
        Verify "Search by IP or Hostname" to add the printer.

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/53365410
                  -> https://hp-testrail.external.hp.com/index.php?/cases/view/53175451
        """
        self.fc.launch_hpx_to_home_page()
        self.fc.fd["devicesMFE"].click_add_button()
        self.fc.fd["addprinter"].verify_add_device_panel()
        self.fc.fd["addprinter"].click_choose_printer_button()
        self.fc.fd["addprinter"].verify_progress_bar(timeout=90)
        if self.fc.fd["addprinter"].verify_no_printers_screen(raise_e=False):
            self.fc.fd["addprinter"].click_add_using_ip_address_btn()
        self.fc.fd["addprinter"].click_input_textbox()
        # Can't test with seaching by hostname since simulator printer doesn't support it.
        self.fc.fd["addprinter"].search_printer(self.ip)
        #  Enter IP address or Hostname in input ip address or hostname textbox.
        # if random.choice([True, False]):
        # #  Enter IP address
        #     self.fc.fd["addprinter"].search_printer(self.ip)
        # else:
        # #  Enter Hostname
        #     self.fc.fd["addprinter"].search_printer(self.hostname)
        self.fc.fd["addprinter"].click_add_printer_btn()
        if self.fc.fd["addprinter"].verify_auto_install_driver_to_print(raise_e=False):
            self.fc.fd["addprinter"].verify_auto_install_driver_to_print_disappear()
            if self.fc.fd["addprinter"].verify_auto_install_driver_done(timeout=5, raise_e=False):
                self.fc.fd["addprinter"].click_continue_btn()
            else:
                self.fc.fd["addprinter"].click_top_exit_setup_btn()
                if self.fc.fd["addprinter"].verify_setup_incomplete_dialog(raise_e=False):
                    self.fc.fd["addprinter"].click_setup_incomplete_dialog_exit_setup_btn()
                    if self.fc.fd["addprinter"].verify_printer_setup_is_incomplete_dialog(raise_e=False):
                        self.fc.fd["addprinter"].click_printer_setup_is_incomplete_dialog_ok_btn()
        self.fc.fd["devicesMFE"].verify_device_card_show_up()

    ##############################################################
    #    One simulator printer can't trigger offline status      #
    ##############################################################
    # @pytest.mark.regression
    # def test_02_verify_install_driver_screen_C53676524_C53676634_C53676651_C53678697(self):
    #     """
    #     simulator printer doesn't support trigger offline status.
    #     Verify "Install driver to print-Manual Install" screen.
    #     Verify the "Back" button functionality from "Remove and add the printer again" screen.
    #     Verify "Printer & scanners" button.

    #     TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/53676524
    #                  https://hp-testrail.external.hp.com/index.php?/cases/view/53676634
    #                  https://hp-testrail.external.hp.com/index.php?/cases/view/53676651
    #                  https://hp-testrail.external.hp.com/index.php?/cases/view/53678697

    #     """
    #     self.fc.fd["devicesMFE"].click_add_button()
    #     self.fc.fd["addprinter"].verify_add_device_panel()
    #     self.fc.fd["addprinter"].click_choose_printer_button()
    #     self.fc.fd["addprinter"].verify_progress_bar(timeout=90)
    #     self.fc.fd["addprinter"].click_input_textbox()
    #     self.fc.search_network_printer(self.p2)
    #     self.fc.fd["addprinter"].click_add_printer_btn()
    #     if not self.fc.fd["addprinter"].verify_install_driver_to_print_screen(timeout=60, raise_e=False):
    #         pytest.skip('The test printer is not an onboarded printer.')
    #     else:
    #         self.fc.trigger_printer_offline_status(self.p2)
    #         self.fc.fd["addprinter"].verify_auto_install_driver_to_print_disappear()
    #         self.fc.fd["addprinter"].click_driver_unavailable_btn()
    #         self.fc.fd["addprinter"].verify_remove_and_add_the_printer_again_screen()
    #         self.fc.fd["addprinter"].click_back_btn()
    #         self.fc.fd["addprinter"].verify_auto_install_driver_to_print_disappear()
    #         self.fc.fd["addprinter"].verify_install_driver_to_print_screen()
    #         self.fc.fd["addprinter"].click_printers_and_scanners_btn()
    #         self.fc.fd["addprinter"].verify_install_driver_to_print_screen()
    #         self.fc.fd["hpx_rebranding_utility"].verify_ps_big_plus_btn() 

    # @pytest.mark.regression
    # def test_03_trigger_printer_online(self):
    #     """
    #     Connect network to printer.
    #     """
    #     self.fc.restore_printer_online_status(self.p2)

    @pytest.mark.regression
    def test_04_verify_search_again_functionality_C53178593(self):
        """
        Verify "Search again" functionality.

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/53178593
        """
        # self.fc.restart_myHP()
        self.fc.fd["devicesMFE"].click_add_button()
        self.fc.fd["addprinter"].verify_add_device_panel()
        self.fc.fd["addprinter"].click_choose_printer_button()
        self.fc.fd["addprinter"].verify_progress_bar(timeout=90)
        self.fc.fd["addprinter"].verify_search_again_link_is_enable()
        self.fc.fd["addprinter"].click_search_again_link()
        self.fc.fd["addprinter"].verify_add_device_screen()