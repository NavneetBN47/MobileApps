import pytest
from SAF.misc import saf_misc
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.ma_misc import conftest_misc
pytest.app_info = "smb"

class Test_07_SMB_Sustainability(object):

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(self, smb_setup, request):
        self = self.__class__
        self.driver, self.fc = smb_setup
        self.driver.set_size("max")
        self.stack = request.config.getoption("--stack")
        #locale will be received in language_region format
        self.locale = self.driver.session_data["locale"]+"/"+self.driver.session_data["language"]
        self.spec_file = self.driver.session_data["language"]+"-"+self.driver.session_data["locale"].upper()
        self.home = self.fc.fd["home"]
        self.sustainability = self.fc.fd["sustainability"]
        self.login_account = ma_misc.get_smb_account_info(self.stack)
        self.hpid_username = self.login_account["email"]
        self.hpid_password = self.login_account["password"]
        self.hpid_tenantID = self.login_account["tenantID"]
        self.attachment_path = conftest_misc.get_attachment_folder()

    def test_01_verify_sustainability_ui_screen(self):
        # https://hp-testrail.external.hp.com/index.php?/cases/view/32546629
        self.fc.go_home(self.stack, self.hpid_username, self.hpid_password, self.hpid_tenantID, self.locale)
        self.home.click_sustainability_menu_btn()

        #To load localization files based on the specified language
        self.fc.load_localization_files(self.spec_file)

        # creating a folder to store Screenshot 
        ma_misc.create_localization_screenshot_folder("sustainability_localization_screenshot", self.attachment_path)
        self.driver.wdvr.get_screenshot_as_file(self.attachment_path + "sustainability_screenshot/{}_sustainability_localization.png".format(self.locale))

        self.sustainability.verify_sustainability_forest_first_icon()
        self.sustainability.verify_sustainability_forest_first_title()
        self.sustainability.verify_sustainability_forest_first_description()
        self.sustainability.verify_sustainability_learn_more_button()

        #verify sustainable impact widget
        self.sustainability.verify_sustainable_impact_title_text()
        self.sustainability.verify_sustainability_hp_plus_printed_pages_count()
        self.sustainability.verify_sustainability_hp_plus_printed_pages_count_description()
        self.sustainability.verify_sustainability_forest_restoration_title()
        self.sustainability.verify_sustainability_forest_restoration_description()

        # verify what we are doing widget
        self.sustainability.verify_sustainability_what_we_are_doing_title_icon()
        self.sustainability.verify_sustainability_what_we_are_doing_title_text()
        self.sustainability.verify_sustainability_forest_first_projects_title_icon()
        self.sustainability.verify_sustainability_forest_first_projects_title_text()
        self.sustainability.verify_sustainability_forest_first_projects_description()
        self.sustainability.verify_sustainability_view_projects_btn_text()
        
        #verify recycle supplies widget
        self.sustainability.verify_sustainability_recycle_supplies_title_icon()
        self.sustainability.verify_sustainability_recycle_supplies_title_text()
        self.sustainability.verify_sustainability_recycle_supplies_icon()
        self.sustainability.verify_sustainability_recycle_supplies_description()
        self.sustainability.verify_sustainability_recycle_supplies_recycle_cartridges_btn_text()

        #verify explore our sustainable impact
        self.sustainability.verify_sustainability_explore_our_sustainable_impact_title_text()
        self.sustainability.verify_sustainability_explore_our_sustainable_impact_title_icon()
        self.sustainability.verify_sustainability_explore_our_sustainable_impact_description()
        self.sustainability.verify_sustainability_explore_our_sustainable_impact_Explore_impact_btn_text()

        #verify disclaimers field
        self.sustainability.verify_sustainability_disclaimers_title_text()
        self.sustainability.verify_sustainability_disclaimers_description_para_one()
        self.sustainability.verify_sustainability_disclaimers_description_para_two()

    def test_02_verify_forest_first_learn_more_button(self):                                                                                         
        # https://hp-testrail.external.hp.com/index.php?/cases/view/32546631

        self.fc.go_home(self.stack, self.hpid_username, self.hpid_password, self.hpid_tenantID, self.locale)
        self.home.click_sustainability_menu_btn()
        self.sustainability.click_sustainability_learn_more_button()
        self.sustainability.verify_new_tab_opened()
        self.sustainability.verify_hp_forest_positive_url()

    # def test_03_verify_number_of_pages_printed_with_home_usage_dashboard(self):
    #     # https://hp-testrail.external.hp.com/index.php?/cases/view/32546637

    #     self.fc.go_home(self.stack, self.hpid_username, self.hpid_password, self.hpid_tenantID, self.locale)
    #     total_pages_printed_count_of_usage_widget = self.home.get_total_pages_in_usage_print_color_toggle()
    #     self.home.click_sustainability_menu_btn()
    #     total_pages_printed_to_hp_plus_printers = self.sustainability.get_sustainability_hp_plus_printed_pages_count()
    #     assert total_pages_printed_count_of_usage_widget == total_pages_printed_to_hp_plus_printers
   
    def test_04_verify_forest_first_view_projects_button(self):
        #https://hp-testrail.external.hp.com/index.php?/cases/view/32546890

        self.fc.go_home(self.stack, self.hpid_username, self.hpid_password, self.hpid_tenantID, self.locale)
        self.home.click_sustainability_menu_btn()
        self.sustainability.click_sustainability_forest_first_view_projects_button()
        self.sustainability.verify_forest_first_project_title()
    
    def test_05_verify_recycle_supplies_cartridges_button(self):
        #https://hp-testrail.external.hp.com/index.php?/cases/view/32546904

        self.fc.go_home(self.stack, self.hpid_username, self.hpid_password, self.hpid_tenantID, self.locale)
        self.home.click_sustainability_menu_btn()
        self.sustainability.click_sustainability_recycle_supplies_cartridges_button()
        self.sustainability.verify_new_tab_opened()
        self.sustainability.verify_recycle_cartridges_url()
    
    def test_06_verify_explore_our_sustainable_impact_button(self):
        #https://hp-testrail.external.hp.com/index.php?/cases/view/32546894
        self.fc.go_home(self.stack, self.hpid_username, self.hpid_password, self.hpid_tenantID, self.locale)
        self.home.click_sustainability_menu_btn()
        self.sustainability.click_sustainability_explore_our_sustainable_impact_button()
        self.sustainability.verify_new_tab_opened()
        self.sustainability.verify_sustainable_impact_url()
    
    def test_07_verify_forest_first_view_projects_page_ui(self):
        #
        self.fc.go_home(self.stack, self.hpid_username, self.hpid_password, self.hpid_tenantID, self.locale)
        self.home.click_sustainability_menu_btn()
        self.sustainability.click_sustainability_forest_first_view_projects_button()
        self.sustainability.verify_forest_first_project_title()
        self.sustainability.verify_forest_first_project_hoopa_valley_title()
        self.sustainability.verify_forest_first_project_title_michigan_state()
        self.sustainability.verify_forest_first_project_title_woodland_trust()
        self.sustainability.verify_forest_first_project_title_mecklenburg_county_forests()
        self.sustainability.verify_forest_first_project_title_willamette()
        self.sustainability.verify_forest_first_project_title_mississippi_alluvial_valley()
        self.sustainability.verify_forest_first_project_title_tyndall_air_force_base()
        self.sustainability.verify_forest_first_project_title_brazil_china_forest_restoration()