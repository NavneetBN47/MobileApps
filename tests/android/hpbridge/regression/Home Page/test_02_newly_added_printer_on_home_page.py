import pytest
from MobileApps.libs.flows.android.hpbridge.utility.api_utility import APIUtility
from MobileApps.libs.flows.android.hpbridge.flows.hpbridge_flow import HPBridgeFlow
import MobileApps.libs.flows.android.hpbridge.utility.utlitiy_misc as utility_misc
pytest.app_info = "hpbridge"
HPBridgeFlow.set_pytest_data()


class TestNewlyAddedPrinterOnHomePage(object):

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(self, request, hpbridge_test_setup):
        self = self.__class__
        self.driver, self.fc = hpbridge_test_setup

        # Define flows
        self.wechat = self.fc.flow["wechat"]
        self.mp_home = self.fc.flow["mp_home"]
        self.mp_faq = self.fc.flow["mp_faq"]
        self.binding = self.fc.flow["bind_printer"]
        self.msg_center = self.fc.flow["mp_message_center"]
        self.qrcode = self.fc.flow["qrcode"]


        # define variables
        self.printer = utility_misc.load_printer()
        self.api_utility = APIUtility()
        self.api_utility.unbind_all_printers()

    def test_c27109890_new_added_printer(self):
        """
        Pre-conditions:
            1. Install the WeChat app.
            2. Login Wechat with a valid account.
        Steps：
            1. Launch the Applet.
               Bind a printer A and go to the home page.
            2. Bind a printer B and then go to the home page.
            3. Select the picture print or document print till to the print settings page with the printer B.
               Change the printer to printer A on print settings page.
               Click the print button
            4. Back to the home page.
               Check the result.

        Expected:
            1. Verify the printer icon display well on home. Verify there is a new in red at the top right corner of the printer A icon.
            2. Verify the new in red disappear at the top right corner of the printer A icon. Verify the new in red display at the top right corner of the printer B icon.
            3. Verify the print job can be printed out successfully.
            4. Verify the new in red still display at the top right corner of the printer B icon
        :return:
        """

        # 1. Bind a printer A and go to the home page.
        self.wechat.save_qrcode_to_device(self.printer["printer_id"])
        self.wechat.send_qrcode()
        self.wechat.scan_qrcode_to_mp()
        self.mp_home.check_add_printer_filed_with_device()

        # self.wechat.goto_mp()
        # # 1. Verify the printer icon display well on home. Verify there is a new in red at the top right corner of the printer A icon.
        #
        # self.mp_home.check_add_printer_filed_with_device()


