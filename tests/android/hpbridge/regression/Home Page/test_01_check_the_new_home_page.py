import pytest
from MobileApps.libs.flows.android.hpbridge.utility.api_utility import APIUtility
from MobileApps.libs.flows.android.hpbridge.flows.hpbridge_flow import HPBridgeFlow
import MobileApps.libs.flows.android.hpbridge.utility.utlitiy_misc as utility_misc
pytest.app_info = "hpbridge"
HPBridgeFlow.set_pytest_data()


class TestNewHomePage(object):

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


        # define variables
        self.printer = utility_misc.load_printer()
        self.api_utility = APIUtility()
        self.api_utility.unbind_all_printers()

    def test_c27109887_new_home_page_fields(self):
        """
        Pre-conditions:
            1. Install the WeChat app.
            2. Login Wechat with a valid account.
            3. The test printer has been enabled webservice and got the welcome page with QR code and Email address displayed on it.
            4. The test printer is not bound with the login Wechat account.
        Steps：
            1. Search out the WeChat Applet and then launch the Applet.
                Check the all stings and buttons on new home page.
            2. Click all buttons on this page.

        Expected:
            1. Verify the printer home page with no bound printer display correctly.
            2. Verify the "Me" icon displayed on the upper left corner of applet home page,and it jumps to the "我的" page with message center.
            3. Verify the announcement displayed correctly.
            4. Verify the "添加打印机" displayed correctly and it will jump to the "绑定打印机" page.
            5. Verify the"文档打印" "照片打印" "百度网盘打印""发票打印" "网络文章打印" "证件照打印" and "身份证复印"displayed well, red "新" displayed on the top right corner of "网络文章打印" and "证件照打印"(The "新" lab will never disappear) , and "您还未绑定设备，请先添加打印机" will pop up when click on it.
            6. Verify the advertisement carousel displayed correctly.
            7. Verify the "?" and "shop" icon displayed on the middle right of applet home page,and "售后服务""X"“帮助”should be displayed when click the "?" icon.
            8. Verify the content store displayed correctly.
        :return:
        """
        self.wechat.goto_mp()
        # 1. Verify the printer home page with no bound printer display correctly.
        self.mp_home.check_add_printer_filed_no_device()
        # 2. Verify the "Me" icon displayed on the upper left corner of applet home page,and it jumps to the "我的" page with message center.
        self.mp_home.click_personal_center_icon()
        self.msg_center.check_page_title()
        self.msg_center.back_to_home_page()
        # 3. Verify the announcement displayed correctly.
        self.mp_home.check_announcement()
        self.mp_home.click_add_first_printer_btn()
        self.binding.check_bind_printer_page()
        self.binding.back_to_home_page()
        # 5. Verify the"文档打印" "照片打印" "百度网盘打印""发票打印" "网络文章打印" "证件照打印" and "身份证复印"displayed well, red "新" displayed on the top right corner of "网络文章打印" and "证件照打印"(The "新" lab will never disappear) , and "您还未绑定设备，请先添加打印机" will pop up when click on it.

        self.mp_home.check_home_page_without_printer()
        # 6. Verify the advertisement carousel displayed correctly.
        self.mp_home.check_advertisement()

        # 7. Verify the "?" and "shop" icon displayed on the middle right of applet home page,and "售后服务""X"“帮助”should be displayed when click the "?" icon.
        self.mp_home.check_hp_shop()
        self.mp_home.check_help_support_no_device()


    def test_c27726039_launch_applet_for_already_bound_printer(self):
        """
        Pre-conditions:
            1. Install the WeChat app.
            2. Login Wechat with a valid account.
            3. The test printer has been enabled webservice and got the welcome page with QR code and Email address displayed on it.
            4. The test printer has bound with the login Wechat account.
        Steps：
            1. Launch the applet
            2. Observe the printer area.

        Expected:
            1. Verify the mum loading shown firstly on printer area, and then the bound printer displayed well.
        :return:
        """
        # bind a printer with API, if there is no printer bound
        if self.api_utility.get_printer_amount() == 0:
            self.api_utility.bind_default_printer()

        self.wechat.goto_mp()
        # 1. VVerify the mum loading shown firstly on printer area, and then the bound printer displayed well.
        self.mp_home.check_add_printer_filed_with_device()

