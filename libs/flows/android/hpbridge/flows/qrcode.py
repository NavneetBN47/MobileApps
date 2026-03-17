from MobileApps.libs.flows.android.hpbridge.flows.hpbridge_flow import HPBridgeFlow


class ScanQRCode(HPBridgeFlow):
    flow_name = "qrcode"

    def __init__(self, driver):
        super(ScanQRCode, self).__init__(driver)
        self.context = "WEBVIEW_com.tencent.mm:tools"
        self.page = "qrcode.png"

    def long_press_qrcode(self):
        """
        Long press the qrcode
        :return:
        """
        self.driver.long_press("qrcode")

        self.switch_to_native_view()
        self.driver.click("qrcode_recognize")

