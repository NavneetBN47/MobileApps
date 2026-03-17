from MobileApps.libs.flows.android.smart.flow_container import FLOW_NAMES
import pytest
import datetime

pytest.app_info = "SMART"

class Test_Suite_01_Fax_Settings_Cover_Page(object):

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, android_smart_setup, softfax_class_cleanup):
        cls = cls.__class__
        cls.driver, cls.fc = android_smart_setup

        # Define flows
        cls.compose_fax = cls.fc.flow[FLOW_NAMES.COMPOSE_FAX]
        cls.fax_settings =cls.fc.flow[FLOW_NAMES.SOFTFAX_FAX_SETTINGS]
        cls.udid = cls.driver.driver_info["desired"]["udid"]

    def test_01_empty_cover_page(self):
        """
        Description: C31379831
            1. Load to Compose Fax with an new account
            2. Click on 3 dot menu/ Fax Settings
            3. Click on Cover Pages item

        Expected Result:
            2. Verify Mobile Fax Setting screen with:
               - Title
               - Mobile Fax Account item
               - Sending item
               - About Mobile Fax item
            3. Verify Cover Pages empty screen with:
               - Title: Cover Pages
               - message "You don't have any cover page templates"
        """
        # Make sure tests not affected by previous test case
        self.fc.reset_app()
        self.__load_fax_settings(create_acc=True)
        self.fax_settings.click_fax_settings_option(self.fax_settings.COVER_PAGES_OPT)
        self.fax_settings.verify_empty_cover_page_screen()

    def test_02_create_edit_cover_pages(self):
        """
        Description: C31379823, C31379827, C31379830
            1. Load to Compose Fax with HPID account login
            2. Click on 3 dot menu/ Fax Settings
            3. Click on Cover Pages item
            4. Click on Create a Cover Page button
            5. Input Cover Page name and Subject
            6. Click on Save button
            7. Click on Select button
            8. Click on Cancel button

        Expected Result:
            4. Verify Add Cover Page screen with:
               - Title
               - Cover Page Details item
            6. Verify Cover Page screen with cover pages list
            7. Verify edit screen:
               - Cancel button
               - Delete button
            8. Verify Cover Page screen
        """
        cover_page_name = "{}_{:%d_%H_%M_%S}".format(self.udid, (datetime.datetime.now()))
        subject = self.test_02_create_edit_cover_pages.__name__
        self.__load_fax_settings()
        self.__create_a_cover_page(cover_page_name, subject)
        self.fax_settings.verify_cover_page(cover_page_name)
        self.fax_settings.click_edit_cancel_btn(self.fax_settings.COVER_PAGE_SELECT_BTN)
        self.fax_settings.verify_cover_page_edit_screen()
        self.fax_settings.click_edit_cancel_btn(self.fax_settings.COVER_PAGE_CANCEL_BTN)
        self.fax_settings.verify_cover_page_screen()

    def test_03_delete_cover_pages(self):
        """
        Description: C31379828, C31379829
            1. Load to Cover Page screen with cover pages list
            2. Click on Edit button
            3. Select a cover page
            4. Click on Delete button
            5. Click on Cancel button
            6. Click on Delete button

        Expected Result:
            4. Verify Are you sure? popup:
               - Message popup
               - Cancel button
               - Delete button
            5. Verify Cover Page edit screen
            6. Verify Cover Page screen
        """
        cover_page_name = "{}_{:%d_%H_%M_%S}".format("cancel_delete", (datetime.datetime.now()))
        subject = self.test_03_delete_cover_pages.__name__
        # Make sure tests not affected by previous test suite
        self.fc.reset_app()
        self.__load_fax_settings()
        self.__create_a_cover_page(cover_page_name, subject)
        self.fax_settings.click_edit_cancel_btn(self.fax_settings.COVER_PAGE_SELECT_BTN)
        self.fax_settings.verify_cover_page_edit_screen()
        self.fax_settings.select_single_cover_page(cover_page_name)
        self.fax_settings.click_cover_pages_delete_btn(is_edited=False)
        self.fax_settings.verify_cover_page_delete_popup()
        self.fax_settings.dismiss_delete_confirmation_popup(is_deleted=False)
        self.fax_settings.verify_cover_page_edit_screen()
        self.fax_settings.click_cover_pages_delete_btn(is_edited=False)
        self.fax_settings.dismiss_delete_confirmation_popup(is_deleted=True)
        self.fax_settings.verify_cover_page_screen()

    def test_04_delete_edit_cover_pages(self):
        """
        Description: C31379824, C31379825, C31379826
            1. Load to Cover Page screen with cover pages list
            2. Select any cover page
            3. Click on Delete button
            4. Click on Cancel button
            5. Click on Delete button
            6. Click on Delete button

        Expected Result:
            2. Verify Edit Cover Pages screen
            3. Verify Are you sure? popup:
               - Message popup
               - Cancel button
               - Delete button
            4. Verify Edit Cover Page screen
            6. Verify Cover Page screen
        """
        cover_page_name = "{}_{:%d_%H_%M_%S}".format("cancel_delete", (datetime.datetime.now()))
        subject = self.test_04_delete_edit_cover_pages.__name__
        # Make sure tests not affected by previous test suite
        self.fc.reset_app()
        self.__load_fax_settings()
        self.__create_a_cover_page(cover_page_name, subject)
        self.fax_settings.select_single_cover_page(cover_page_name)
        self.fax_settings.verify_edit_cover_page_screen()
        self.fax_settings.click_cover_pages_delete_btn(is_edited=True)
        self.fax_settings.dismiss_delete_confirmation_popup(is_deleted=False)
        self.fax_settings.verify_edit_cover_page_screen()
        self.fax_settings.click_cover_pages_delete_btn(is_edited=True)
        self.fax_settings.dismiss_delete_confirmation_popup(is_deleted=True)
        self.fax_settings.verify_cover_page_screen()

    ######################################################################
    #                           PRIVATE FUNCTIONS                        #
    ######################################################################
    
    def __load_fax_settings(self, create_acc=True):
        """
        - Load Compose Fax screen with HPID account login or created a new HPID account
        - Click on Fax Settings on from More Option menu
        """
        self.fc.flow_home_load_compose_fax_screen(create_acc=create_acc,
                                                  check_onboarding=False)
        self.compose_fax.verify_compose_fax_screen()
        self.compose_fax.click_menu_option_btn(self.compose_fax.MENU_FAX_SETTINGS_BTN)
        self.fax_settings.verify_fax_settings_screen()
    
    def __create_a_cover_page(self, cover_page_name, subject):
        """
        - Click on Create Cover Page button
        - Add cover page name and subject
        - Click on Save button
        """
        self.fax_settings.click_fax_settings_option(self.fax_settings.COVER_PAGES_OPT)
        self.fax_settings.click_create_cover_page_btn()
        self.fax_settings.add_edit_cover_page(cover_page_name, subject)
        self.fax_settings.verify_cover_page_screen()