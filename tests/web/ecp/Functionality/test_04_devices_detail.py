import pytest
from time import sleep
from SAF.misc import saf_misc
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.flows.web.ecp.ecp_api_utility import *
import random
pytest.app_info = "ECP"

class Test_01_ECP_Devices_Detail(object):

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(self, ecp_setup, request):
        self = self.__class__
        self.driver, self.fc = ecp_setup
        self.driver.set_size("max")
        self.stack = request.config.getoption("--stack")
        self.home = self.fc.fd["home"]
        self.devices = self.fc.fd["devices"]
        self.endpoint_security = self.fc.fd["endpoint_security"]
        self.account = ma_misc.get_ecp_account_info(self.stack)
        self.hpid_username = self.account["email"]
        self.hpid_password = self.account["password"]
        # self.customer = self.account["customer"]
        self.tenantID = self.account["tenantID"]

    @pytest.fixture(scope="function", autouse="true")
    def go_to_devices(self):
        self.fc.go_home(self.stack, self.hpid_username, self.hpid_password)
        # self.fc.select_customer(self.customer)
        self.home.click_devices_menu_btn()
        return self.devices.verify_device_page()

    def test_01_verify_properties_tab(self):
        #
        #self.devices.search_device("online") # It will randomly select the first device, so commenting this line
        self.devices.click_first_entry_link()
        self.devices.click_device_details_properties_tab()
        self.devices.verify_device_accordion()
        self.devices.verify_ews_accordion()
        self.devices.verify_network_accordion()
        self.devices.verify_security_accordion()
        # self.devices.verify_supplies_accordion() # Not available in the application
        self.devices.verify_show_editable_items_only()
        self.devices.verify_show_editable_items_only_toggle_status()

    def test_02_verify_device_specific_policy_tab_when_no_settings_applied(self):
        # https://hp-testrail.external.hp.com/index.php?/cases/view/32292070
        #self.devices.search_device("online") # It will randomly select the first device, so commenting this line
        self.devices.click_first_entry_link()
        self.devices.click_device_details_policy_tab()
        self.devices.verify_device_details_policies_tab_compliance_status_widget()
        self.devices.click_device_details_policies_tab_compliance_status_widget()
        self.devices.verify_device_details_device_specific_policy_card()
        # self.devices.verify_device_details_policy_card_title() # Not available in the application
        self.devices.verify_device_specific_policy_edit_button()
        self.devices.click_device_details_policy_widget_expand_button()
        if self.devices.device_specific_policy_card_empty() is False:
            self.devices.click_device_specific_policy_edit_button()
            self.devices.click_device_specific_policy_checkbox()
            self.devices.click_device_specific_policy_checkbox()
            self.devices.click_device_specific_policy_next_button()
            self.devices.click_device_specific_policy_remove_button()
            self.devices.click_device_details_policy_widget_expand_button()
        self.devices.verify_device_specific_policy_card_no_policy_message()

    def test_03_verify_add_device_specific_policy(self):
        # https://hp-testrail.external.hp.com/index.php?/cases/view/32292088
        #self.devices.search_device("online") # It will randomly select the first device, so commenting this line
        self.devices.click_first_entry_link()
        self.devices.click_device_details_policy_tab()
        self.devices.click_device_details_policies_tab_compliance_status_widget()
        self.devices.verify_device_details_device_specific_policy_card()
        self.devices.click_device_specific_policy_edit_button()
        self.devices.search_policy_settings("Company Name")
        self.devices.click_device_specific_policy_checkbox()
        self.devices.click_device_specific_policy_next_button()
        self.devices.click_device_specific_policy_create_button()
        self.endpoint_security.dismiss_toast_successful_message()
        self.devices.click_device_details_policy_widget_expand_button()
        self.devices.verify_device_specific_policy_setting_added("company-name")

    def test_04_verify_remove_device_specific_policy(self):
        # https://hp-testrail.external.hp.com/index.php?/cases/view/32292090
        #self.devices.search_device("online") # It will randomly select the first device, so commenting this line
        self.devices.click_first_entry_link()
        self.devices.click_device_details_policy_tab()
        self.devices.click_device_details_policies_tab_compliance_status_widget()
        self.devices.verify_device_details_device_specific_policy_card()
        self.devices.click_device_specific_policy_edit_button()
        self.devices.click_device_specific_policy_checkbox()
        self.devices.click_device_specific_policy_checkbox()
        self.devices.click_device_specific_policy_next_button()
        self.devices.click_device_specific_policy_remove_button()
        self.devices.check_toast_successful_message("Device-Specific Policy has been removed.")
        self.devices.click_device_details_policy_widget_expand_button()
        assert self.devices.device_specific_policy_card_empty() == True

    def test_05_verify_simulator_onboarding_by_registering_the_company(self):
        # Select a random profile
        self.profile = random.choice(["camden", "busch"])
        
        # Creating Simulator through API
        create_simulator_uri = "https://g2sim.wpp.api.hp.com/wpp/simulator/printers"
        response = create_simulator(self.stack, self.profile, create_simulator_uri)
        serial_number = response.json()["entity_id"]
        product_number = response.json()["model_number"]

        # PRE-Registering to Company 
        pre_register_uri = "https://"+self.stack+"-us1.api.ws-hp.com/ucde/ucde/v2/ecosystem/programmgtsvc/companies/"+self.tenantID+"/participantinfos"
        response = pre_registering_the_device(self.stack, serial_number, product_number, pre_register_uri)

        # Registering the Printer and collecting the device Cloud- ID
        enabling_web_services_uri = "https://g2sim.wpp.api.hp.com/wpp/simulator/printers/"+serial_number+"/register"
        response = registering_simulator(self.stack, enabling_web_services_uri)
        device_cloud_id = response.json()["cloud_id"]

        # Verify the Device in the ECP
        sleep(15) # Waiting for the device to be registered and to display in the ECP
        self.devices.click_refresh_button()
        # self.devices.click_groups_side_bar_expand_btn()
        retries = 7 # Retrying to search the device for 7 times to display in the ECP
        while retries > 0 and self.devices.search_device(serial_number) is False:
            self.devices.click_refresh_button()
            retries -= 1
            self.devices.search_device(serial_number)
        self.devices.click_first_entry_link()
        assert device_cloud_id == self.devices.get_device_cloud_id()

        # Verify the Device Grants Details
        device_grants_uri = "https://stage-us1.api.ws-hp.com/v2/grant-controller/grants?deviceId="+device_cloud_id+"&includeSources=true"
        response = get_grants_the_device(self.stack, device_grants_uri)

        contents = response.json()["contents"]

        # Check if the grant smcloud and smcloud advanced is present
        assert any(content["grant"] == "ws-hp.com/smcloud" for content in contents), "Grant 'ws-hp.com/smcloud' not found in the response"
        assert any(content["grant"] == "ws-hp.com/smcloud-advanced" for content in contents), "Grant 'ws-hp.com/smcloud-advanced' not found in the response"
        assert any(content["grant"] == "ws-hp.com/enterprise-telemetry" for content in contents), "Grant 'ws-hp.com/enterprise-telemetry' not found in the response"

        # Uninstalling the Simulator
        unregistering_simulator_uri = "https://stage-us1.api.ws-hp.com/ucde/ucde/v2/ecosystem/programmgtsvc/participantinfos"
        response = unregister_the_device(self.stack, serial_number, product_number, unregistering_simulator_uri)

        # Verify the Device deletion in the ECP
        sleep(5)
        self.devices.click_devcies_tab_breadcrumb()
        self.devices.click_refresh_button()
        self.devices.search_device(serial_number)
        self.devices.verify_no_items_found()

    def test_06_verify_simulator_onboarding_by_enabling_web_services(self):
        # Select a random profile
        self.profile = random.choice(["camden", "busch"])
        
        # Creating Simulator through API
        create_simulator_uri = "https://g2sim.wpp.api.hp.com/wpp/simulator/printers"
        response = create_simulator(self.stack, self.profile, create_simulator_uri)
        serial_number = response.json()["entity_id"]
        product_number = response.json()["model_number"]

        # Registering the Printer and collecting the device Cloud- ID
        enabling_web_services_uri = "https://g2sim.wpp.api.hp.com/wpp/simulator/printers/"+serial_number+"/register"
        response = registering_simulator(self.stack, enabling_web_services_uri)
        device_cloud_id = response.json()["cloud_id"]

        # PRE-Registering to Company 
        pre_register_uri = "https://"+self.stack+"-us1.api.ws-hp.com/ucde/ucde/v2/ecosystem/programmgtsvc/companies/"+self.tenantID+"/participantinfos"
        response = pre_registering_the_device(self.stack, serial_number, product_number, pre_register_uri)

        # Verify the Device in the ECP
        sleep(15) # Waiting for the device to be registered and to display in the ECP
        self.devices.click_refresh_button()
        # self.devices.click_groups_side_bar_expand_btn()
        retries = 7 # Retrying to search the device for 7 times to display in the ECP
        while retries > 0 and self.devices.search_device(serial_number) is False:
            self.devices.click_refresh_button()
            retries -= 1
            self.devices.search_device(serial_number)
        self.devices.click_first_entry_link()
        assert device_cloud_id == self.devices.get_device_cloud_id()

        # Verify the Device Grants Details
        device_grants_uri = "https://stage-us1.api.ws-hp.com/v2/grant-controller/grants?deviceId="+device_cloud_id+"&includeSources=true"
        response = get_grants_the_device(self.stack, device_grants_uri)

        contents = response.json()["contents"]

        # Check if the grant smcloud and smcloud advanced is present
        assert any(content["grant"] == "ws-hp.com/smcloud" for content in contents), "Grant 'ws-hp.com/smcloud' not found in the response"
        assert any(content["grant"] == "ws-hp.com/smcloud-advanced" for content in contents), "Grant 'ws-hp.com/smcloud-advanced' not found in the response"
        assert any(content["grant"] == "ws-hp.com/enterprise-telemetry" for content in contents), "Grant 'ws-hp.com/enterprise-telemetry' not found in the response"

        # Uninstalling the Simulator
        unregistering_simulator_uri = "https://stage-us1.api.ws-hp.com/ucde/ucde/v2/ecosystem/programmgtsvc/participantinfos"
        response = unregister_the_device(self.stack, serial_number, product_number, unregistering_simulator_uri)

        # Verify the Device deletion in the ECP
        sleep(5)
        self.devices.click_devcies_tab_breadcrumb()
        self.devices.click_refresh_button()
        self.devices.search_device(serial_number)
        self.devices.verify_no_items_found()