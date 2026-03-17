from MobileApps.libs.flows.android.hpx.hpx_flow import HPXFlow

class HpxCameraScan(HPXFlow):
    flow_name = "hpx_camera_scan"

    def click_x_button_on_camera_scan(self):
        self.driver.click("x_button_on_camera_scan")
