from selenium.common.exceptions import WebDriverException
from MobileApps.libs.flows.web.smb.smb_flow import SMBFlow
import logging
from SAF.decorator.saf_decorator import string_validation

class StringComparisonException(Exception):
    pass

class Sustainability(SMBFlow):
    flow_name = "sustainability"
    hp_forest_positive_url = "https://www.hp.com/us-en/printers/forest-first-printing.html?jumpid=va_29658a92aa"
    recycle_cartridges_url = "https://www.hp.com/en-us/hp-information/recycling/ink-toner.html"
    sustainable_impact_url = "https://www.hp.com/us-en/hp-information/sustainable-impact.html"

############################ Sustainability Screen Page  ############################ 

    def verify_sustainability_forest_first_icon(self):
        return self.driver.wait_for_object("sustainability_forest_first_icon", timeout=20)

    #all the string verification will be done using string_validation decorator for localization   
    @string_validation("banner_bannerHeader")
    def verify_sustainability_forest_first_title(self):
        return self.driver.wait_for_object("banner_bannerHeader", timeout=30)

    @string_validation("banner_bannerBodyCopy")
    def verify_sustainability_forest_first_description(self):
        return self.driver.wait_for_object("banner_bannerBodyCopy")

    @string_validation("banner_bannerButton")
    def verify_sustainability_learn_more_button(self):
        return self.driver.wait_for_object("banner_bannerButton")

    @string_validation("impactCard_header")
    def verify_sustainable_impact_title_text(self):
        return self.driver.wait_for_object("impactCard_header")

    def verify_sustainability_hp_plus_printed_pages_count(self):
        return self.driver.wait_for_object("sustainability_hp_plus_printed_pages_count")

    @string_validation("impactCard_bodyCopy1")
    def verify_sustainability_hp_plus_printed_pages_count_description(self):
        return self.driver.wait_for_object("impactCard_bodyCopy1")

    @string_validation("impactCard_subhead")
    def verify_sustainability_forest_restoration_title(self):
        return self.driver.wait_for_object("impactCard_subhead")

    @string_validation("impactCard_bodyCopy2")
    def verify_sustainability_forest_restoration_description(self):
        return self.driver.wait_for_object("impactCard_bodyCopy2")
    
    def verify_sustainability_what_we_are_doing_title_icon(self):
        return self.driver.wait_for_object("sustainability_what_we_are_doing_title_icon")

    @string_validation("hpActionsCard_header")
    def verify_sustainability_what_we_are_doing_title_text(self):
        return self.driver.wait_for_object("hpActionsCard_header")

    def verify_sustainability_forest_first_projects_title_icon(self):
        return self.driver.wait_for_object("sustainability_forest_first_projects_title_icon")

    @string_validation("hpActionsCard_subhead1")
    def verify_sustainability_forest_first_projects_title_text(self):
        return self.driver.wait_for_object("hpActionsCard_subhead1")

    @string_validation("hpActionsCard_bodyCopy1")
    def verify_sustainability_forest_first_projects_description(self):
        return self.driver.wait_for_object("hpActionsCard_bodyCopy1")

    @string_validation("hpActionsCard_primaryButton1")
    def verify_sustainability_view_projects_btn_text(self):
        return self.driver.wait_for_object("hpActionsCard_primaryButton1")

    def verify_sustainability_recycle_supplies_title_icon(self):
        return self.driver.wait_for_object("sustainability_recycle_supplies_title_icon")

    @string_validation("recycleSuppliesCard_header1")
    def verify_sustainability_recycle_supplies_title_text(self):
        return self.driver.wait_for_object("recycleSuppliesCard_header1")
    
    def verify_sustainability_recycle_supplies_icon(self):
        return self.driver.wait_for_object("sustainability_recycle_supplies_icon")

    @string_validation("recycleSuppliesCard_bodyCopy1")
    def verify_sustainability_recycle_supplies_description(self):
        return self.driver.wait_for_object("recycleSuppliesCard_bodyCopy1")

    @string_validation("recycleSuppliesCard_primaryButton")
    def verify_sustainability_recycle_supplies_recycle_cartridges_btn_text(self):
        return self.driver.wait_for_object("recycleSuppliesCard_primaryButton")

    @string_validation("hpActionsCard_subhead2")
    def verify_sustainability_explore_our_sustainable_impact_title_text(self):
        return self.driver.wait_for_object("hpActionsCard_subhead2")

    def verify_sustainability_explore_our_sustainable_impact_title_icon(self):
        return self.driver.wait_for_object("sustainability_explore_our_sustainable_impact_title_icon")

    @string_validation("hpActionsCard_bodyCopy2")
    def verify_sustainability_explore_our_sustainable_impact_description(self):
        return self.driver.wait_for_object("hpActionsCard_bodyCopy2")

    @string_validation("hpActionsCard_primaryButton2")
    def verify_sustainability_explore_our_sustainable_impact_Explore_impact_btn_text(self):
        return self.driver.wait_for_object("hpActionsCard_primaryButton2")

    @string_validation("disclaimers_header")
    def verify_sustainability_disclaimers_title_text(self):
        return self.driver.wait_for_object("disclaimers_header")

    @string_validation("disclaimers_note1")
    def verify_sustainability_disclaimers_description_para_one(self):
        return self.driver.wait_for_object("disclaimers_note1")

    @string_validation("disclaimers_note2")
    def verify_sustainability_disclaimers_description_para_two(self):
        return self.driver.wait_for_object("disclaimers_note2")

    def click_sustainability_learn_more_button(self):
        return self.driver.click("banner_bannerButton", timeout=20)

    def verify_new_tab_opened(self):
        return self.driver.wait_for_new_window()
        
    def get_sustainability_hp_plus_printed_pages_count(self):
        return int(self.driver.wait_for_object("sustainability_hp_plus_printed_pages_count").text)

    def click_sustainability_forest_first_view_projects_button(self):
        return self.driver.click("sustainability_forest_first_view_projects_btn",timeout=20)

    @string_validation("hpActionsCard_subhead1")
    def verify_forest_first_project_title(self):
        return self.driver.wait_for_object("hpActionsCard_subhead1",timeout=20)
    
    @string_validation("forestFirstProjectsPage_card1_header1")
    def verify_forest_first_project_hoopa_valley_title(self):
        return self.driver.wait_for_object("forestFirstProjectsPage_card1_header1")
    
    @string_validation("forestFirstProjectsPage_card2_header2")
    def verify_forest_first_project_title_michigan_state(self):
        return self.driver.wait_for_object("forestFirstProjectsPage_card2_header2")
    
    @string_validation("forestFirstProjectsPage_card3_header3")
    def verify_forest_first_project_title_woodland_trust(self):
        return self.driver.wait_for_object("forestFirstProjectsPage_card3_header3")
    
    @string_validation("forestFirstProjectsPage_card4_header4")
    def verify_forest_first_project_title_mecklenburg_county_forests(self):
        return self.driver.wait_for_object("forestFirstProjectsPage_card4_header4")
    
    @string_validation("forestFirstProjectsPage_card5_header5")
    def verify_forest_first_project_title_willamette(self):
        return self.driver.wait_for_object("forestFirstProjectsPage_card5_header5")
    
    @string_validation("forestFirstProjectsPage_card6_header6")
    def verify_forest_first_project_title_mississippi_alluvial_valley(self):
        return self.driver.wait_for_object("forestFirstProjectsPage_card6_header6")

    @string_validation("forestFirstProjectsPage_card7_header7")
    def verify_forest_first_project_title_tyndall_air_force_base(self):
        return self.driver.wait_for_object("forestFirstProjectsPage_card7_header7")

    @string_validation("forestFirstProjectsPage_card8_header8")
    def verify_forest_first_project_title_brazil_china_forest_restoration(self):
        return self.driver.wait_for_object("forestFirstProjectsPage_card8_header8")

    def click_sustainability_recycle_supplies_cartridges_button(self):
        return self.driver.click("sustainability_recycle_supplies_cartridges_btn", timeout=20)
    
    def click_sustainability_explore_our_sustainable_impact_button(self):
        return self.driver.click("sustainability_explore_our_sustainable_impact_btn", timeout=20)
    
    def verify_hp_forest_positive_url(self):
        #Verifying url matches
        return self.driver.wdvr.current_url == self.hp_forest_positive_url
    
    def verify_recycle_cartridges_url(self):
        return self.driver.wdvr.current_url == self.recycle_cartridges_url
    
    def verify_sustainable_impact_url(self):
        return self.driver.wdvr.current_url == self.sustainable_impact_url