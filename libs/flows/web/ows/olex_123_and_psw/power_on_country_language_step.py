from MobileApps.libs.flows.web.ows.ows_flow import OWSFlow
from MobileApps.libs.ma_misc.ma_misc import get_subfolder_path


class CountryLanguageTrafficDirector(OWSFlow):
    flow_name = "td_country_language"
    flow_url = "country-language"

    folder_name = get_subfolder_path(__file__, OWSFlow.project)

    def verify_country_language_page(self):
        """
        Verify country-language step for traffic ditrector marconi.
        """
        self.driver.wait_for_object("power_on_country_language_step")

    def verify_power_on_card_content(self):
        """
        Verify select language and country/region card.
        """
        self.driver.wait_for_object("power_on_card_0_image")
        self.driver.wait_for_object("power_on_card_0_instruction")

    def verify_country_language_card(self):
        for i in range(2):
            self.driver.wait_for_object("country_language_card_{}_image".format(i))
            self.driver.wait_for_object("country_language_card_{}_instruction".format(i))

    def verify_header_title(self):
        """
        Verify Country-language header title.
        """
        self.driver.wait_for_object("title")

    def verify_card_description(self):
        """
        Verify country languange step card description.
        """
        self.driver.wait_for_object("card_description")