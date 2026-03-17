from MobileApps.libs.flows.android.hpx.hpx_flow import HPXFlow

class HpxHome(HPXFlow):
    flow_name = "hpx_home"

    def verify_camera_scan_tile(self, timeout=20, raise_e=True):
        """ 
        verifies whether camera scan tile is displayed on the homepage or not
        """
        if self.driver.wait_for_object("camera_scan_tile", timeout=timeout, raise_e=raise_e):
            return True
        return False

    def click_camera_scan_tile(self, timeout=30, raise_e=False, max_swipes=5):
        """ Swipes to find the camera scan tile and clicks on it."""
        for _ in range(max_swipes):
            if self.driver.wait_for_object("camera_scan_tile", timeout=timeout, raise_e=raise_e):
                self.driver.click("camera_scan_tile", timeout=10)
                return True
            self.driver.swipe()
        raise Exception("Unable to find and click on 'camera_scan_tile' after swiping.")

    def verify_homepage_bottom_devices_btn(self):
        return self.driver.wait_for_object("homepage_bottom_devices_btn")

    def verify_homepage_bottom_shop_btn(self):
        return self.driver.wait_for_object("homepage_bottom_shop_btn")
