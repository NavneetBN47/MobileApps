import pytest
from MobileApps.libs.flows.android.smart.flow_container import FLOW_NAMES
from SAF.misc import saf_misc
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.resources.const.android.const import TEST_DATA

pytest.app_info = "SMART"


class Test_Suite_02_Compose_Fax_Invalid_Information(object):

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, android_smart_setup, softfax_class_cleanup):
        cls = cls.__class__
        cls.driver, cls.fc = android_smart_setup

        # Define flows
        cls.compose_fax = cls.fc.flow[FLOW_NAMES.COMPOSE_FAX]

        # Define variables
        cls.recipient_info = cls.fc.get_softfax_recipient_info()
        cls.sender_info = saf_misc.load_json(ma_misc.get_abs_path(TEST_DATA.SOFTFAX_ACCOUNT))["softfax"]["sender_01"]
        cls.fc.set_hpid_account("ucde", claimable=False, ii_status=True, smart_advance=False)

    def test_01_recipient_phone_number(self):
        """
        Description: C31379708, C31379714, C31379710, C31379709
            1/ Load to Compose Fax screen
            2/ Enter a invalid recipient phone number (default - empty, short, or long)
            3/ Click on Send Fax button
        Expected result:
            3/ Validation message for recipient phone number display
        """
        self.fc.flow_home_load_compose_fax_screen(create_acc=False)
        #input default information:
        self.compose_fax.click_send_fax(raise_e=False)
        self.compose_fax.verify_phone_validation_message(self.compose_fax.EMPTY_PHONE_MSG, is_sender=False)
        #input short recipient information:
        self.compose_fax.enter_recipient_information("1234")
        self.compose_fax.click_send_fax(raise_e=False)
        self.compose_fax.verify_phone_validation_message(self.compose_fax.INVALID_FORMAT_MSG, is_sender=False)
        #input long recipient information:
        self.compose_fax.enter_recipient_information("123456789012345")
        self.compose_fax.click_send_fax(raise_e=False)
        self.compose_fax.verify_phone_validation_message(self.compose_fax.INVALID_FORMAT_MSG, is_sender=False)

    def test_02_sender_phone_number(self):
        """
        Description: C31379725, C31379727, C31379723, C31379726
            1/ Load to Compose Fax screen
            2/ Enter a empty sender phone number
            3/ Click on Send Fax button
        Expected result:
            3/  error message of sender phone number visible
        """
        # Make sure compose fax screen is empty, not affect by previous test suite
        self.fc.reset_app()
        self.fc.flow_home_load_compose_fax_screen(create_acc=False)
        self.compose_fax.enter_recipient_information(self.recipient_info["phone"])
        # Leave sender name as empty:
        self.compose_fax.enter_sender_information("", self.sender_info["phone"])
        self.compose_fax.click_send_fax(raise_e=False)
        self.compose_fax.verify_sender_name_error_message()
        # input default sender information:
        self.compose_fax.enter_sender_information(self.sender_info["name"], "")
        self.compose_fax.click_send_fax(raise_e=False)
        self.compose_fax.verify_phone_validation_message(self.compose_fax.EMPTY_PHONE_MSG, is_sender=True)
        # input short sender information:
        self.compose_fax.enter_sender_information(self.sender_info["name"], "1234")
        self.compose_fax.click_send_fax(raise_e=False)
        self.compose_fax.verify_phone_validation_message(self.compose_fax.INVALID_FORMAT_MSG, is_sender=True)
        # input long sender information:
        self.compose_fax.enter_sender_information(self.sender_info["name"], "123456789012345")
        self.compose_fax.click_send_fax(raise_e=False)
        self.compose_fax.verify_phone_validation_message(self.compose_fax.INVALID_FORMAT_MSG, is_sender=True)