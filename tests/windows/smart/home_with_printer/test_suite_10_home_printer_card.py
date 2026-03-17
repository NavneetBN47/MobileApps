import pytest
import logging
import SPL.driver.driver_factory as p_driver_factory

from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.ma_misc import conftest_misc as c_misc


pytest.app_info = "GOTHAM"
class Test_Suite_10_Home_Printer_Card(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, windows_smart_setup, load_printers_session):
        cls = cls.__class__
        cls.driver, cls.fc = windows_smart_setup

        # # Initializing Printer1
        cls.p = load_printers_session

        # Initializing Printer2
        cls.sys_config = ma_misc.load_system_config_file()
        cls.db_info = cls.sys_config.get("database_info", None)
        cls.p2 = p_driver_factory.get_printer(cls.sys_config["printer_power_config"], db_info=cls.db_info)
        cls.p2.set_mech_mode(mech=False)
        cls.printer_info2 = cls.p2.get_printer_information()
        logging.info("Printer Information:\n {}".format(cls.printer_info2))

        cls.home = cls.fc.fd["home"]
        cls.gotham_utility = cls.fc.fd["gotham_utility"]

        ssid, password = c_misc.get_wifi_info(request)
        host = request.config.getoption("--mobile-device")
        user = "exec"
        cls.driver.connect_to_wifi(host, user, ssid, password)

        cls.driver.ssh.send_command('Remove-Printer -Name "*HP*"')

    def test_01_check_setup_or_add_printer_card(self):
        """
        Go to main UI when no printer is added, verify "Setup or Add printer" card shows in main UI
        Check "Setup or add printer" card UI
        Check pagination in "Setup or add printer" card, verify no pagination shows
        Check left/right arrows in "Setup or add printer" card, verify no arrows show
        Verify main page (with no printer selected in HPC region) UI 

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/32534926
                -> https://hp-testrail.external.hp.com/index.php?/cases/view/32534927
                -> https://hp-testrail.external.hp.com/index.php?/cases/view/32534971
                -> https://hp-testrail.external.hp.com/index.php?/cases/view/32534988
                -> https://hp-testrail.external.hp.com/index.php?/cases/view/13890663
                -> https://hp-testrail.external.hp.com/index.php?/cases/view/28749341
        """    
        self.fc.go_home()
        self.home.verify_setup_or_add_printer_card()
        assert self.home.verify_pagination_text(raise_e=False) is False
        assert self.home.verify_add_new_printer_link(raise_e=False) is False
        assert self.home.verify_previous_device_btn_enabled_status() == "false"
        assert self.home.verify_next_device_btn_enabled_status() == "false"

        self.gotham_utility.click_maximize()
        self.home.verify_setup_or_add_printer_card()

        check_string = 'PrinterSelected data:{\r\n  "IsSelected": false\r\n}'

        self.fc.check_gotham_log(check_string)

    def test_02_check_printer_card_with_one_printer(self):
        """
        Click "Add Printer" button on "Setup or add printer" card, verify Device Picker opens
        Go to main UI when printer is added, , verify printer card shows with added printer, and with "Add new printer" string  
        Check the card when printer is added UI
        *Add a local printer to main UI, verify printer shows on main UI card
        Check left/right arrows when one printer is added, verify left and right arrows show on the printer card
        Check printer name on the main UI, verify correct name shows
        Maximize the main UI screen, verify printer card doesn't change
        Verify main page (with II printer selected in HPC region) UI 
        Switch printer cards, verify CEC Jweb area shows for all cards and the applicable engagements shows for the selected / not selected printer 

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/32534929
                -> https://hp-testrail.external.hp.com/index.php?/cases/view/32535010
                -> https://hp-testrail.external.hp.com/index.php?/cases/view/32535095
                -> https://hp-testrail.external.hp.com/index.php?/cases/view/27266563
                -> https://hp-testrail.external.hp.com/index.php?/cases/view/27266567
                -> https://hp-testrail.external.hp.com/index.php?/cases/view/13890713
                -> https://hp-testrail.external.hp.com/index.php?/cases/view/27266575
                -> https://hp-testrail.external.hp.com/index.php?/cases/view/13890665
                -> https://hp-testrail.external.hp.com/index.php?/cases/view/28749341
                -> https://hp-testrail.external.hp.com/index.php?/cases/view/29548762
                -> https://hp-testrail.external.hp.com/index.php?/cases/view/28749339

        """
        self.fc.select_a_printer(self.p, from_carousel=True)
        self.home.verify_carousel_printer_image()

        self.home.verify_add_new_printer_link()
        assert self.home.verify_previous_device_btn_enabled_status() == "true"
        assert self.home.verify_next_device_btn_enabled_status() == "false"
        assert self.home.verify_pagination_text(raise_e=False) is False
        printer_model_name = self.home.get_carousel_printer_model_name()
        assert self.p.get_printer_information()["model name"] in printer_model_name

        self.gotham_utility.click_maximize()
        assert self.p.get_printer_information()["model name"] in printer_model_name

        self.home.verify_cec_banner()

        check_string = 'PrinterSelected data:{\r\n  "IsSelected": true,'
        self.fc.check_gotham_log(check_string)

        self.home.click_previous_device_btn()
        self.home.verify_setup_or_add_printer_card()
        self.home.verify_cec_banner()

    def test_03_check_printer_card_with_multiple_printers(self):
        """
        *Add multiple printers to main UI, verify all printer show on main UI cards
        Add multiple printers, verify the 1st added printer is listed to the far left 
        Add multiple printers, verify the recent added printer is listed to the far right 
        Check left/right arrows when multiple printers are added, verify both left and right arrows show on the printer card 
        Check pagination when multiple printers are added, verify correct pagination shows for each printer card 
        Maximize the main UI screen, verify printer card doesn't change 

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/27266570
                -> https://hp-testrail.external.hp.com/index.php?/cases/view/27266572
                -> https://hp-testrail.external.hp.com/index.php?/cases/view/27426891
                -> https://hp-testrail.external.hp.com/index.php?/cases/view/27266568
                -> https://hp-testrail.external.hp.com/index.php?/cases/view/27266566
                -> https://hp-testrail.external.hp.com/index.php?/cases/view/27266575
                -> https://hp-testrail.external.hp.com/index.php?/cases/view/13416174
                -> https://hp-testrail.external.hp.com/index.php?/cases/view/28934171
        """
        self.fc.select_a_printer(self.p2)
        self.home.verify_add_new_printer_link()
        assert self.home.verify_pagination_text().get_attribute("Name") == "2 of 2 printers."
        assert self.home.verify_previous_device_btn_enabled_status() == "true"
        assert self.home.verify_next_device_btn_enabled_status() == "false"
        printer2_model_name = self.home.get_carousel_printer_model_name(index=1)
        assert self.printer_info2["model name"] in printer2_model_name
        # Verify the "Shortcuts" tile shows on Main UI for all the printers
        self.home.verify_main_page_tiles()

        self.home.click_previous_device_btn()
        self.home.verify_add_new_printer_link()
        assert self.home.verify_pagination_text().get_attribute("Name") == "1 of 2 printers."
        assert self.home.verify_previous_device_btn_enabled_status() == "true"
        assert self.home.verify_next_device_btn_enabled_status() == "true"
        printer1_model_name = self.home.get_carousel_printer_model_name()
        assert self.p.get_printer_information()["model name"] in printer1_model_name
        # Verify the "Shortcuts" tile shows on Main UI for all the printers
        self.home.verify_main_page_tiles()

        self.home.click_previous_device_btn()
        self.home.verify_setup_or_add_printer_card()
        assert self.home.verify_pagination_text(raise_e=False) is False
        assert self.home.verify_add_new_printer_link(raise_e=False) is False
        assert self.home.verify_previous_device_btn_enabled_status() == "false"
        assert self.home.verify_next_device_btn_enabled_status() == "true"

    def test_04_check_hide_printer(self):
        """
        Right click on printer on printer card, click left/right arrow on printer card, verify next printer card shows with no issues

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/29388317
        """
        self.home.click_next_device_btn()
        self.home.verify_add_new_printer_link()
        if not self.home.verify_carousel_finish_setup_btn(raise_e=False):
            self.home.verify_carousel_printer_status_text(timeout=120)
        else:
            self.home.verify_carousel_finish_setup_subtitle()

        self.home.right_click_printer_carousel()
        self.home.click_hide_printer_list_item()
        self.home.verify_hide_this_printer_dialog_load()
        self.home.click_hide_this_printer_dialog_hide_printer_btn()
        assert self.home.verify_hide_this_printer_dialog_load(raise_e=False) is False
        assert self.home.verify_pagination_text(raise_e=False) is False

        self.home.click_previous_device_btn()
        self.home.verify_setup_or_add_printer_card()
        self.home.click_next_device_btn()
        self.home.verify_add_new_printer_link()
