import pytest
from PIL import Image
import time

from MobileApps.tests.windows.hpx.ui_validation.ui_validation_helpers import *
from applitools.images import Eyes, BatchInfo
from MobileApps.libs.flows.windows.hpx.navigation_panel import NavigationPanel

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"

class Test_Suit_Device_Page_UI_Validation_C50712698:
    @pytest.mark.applitools
    @screenshot_test("Smoke Test - Device Page Layout")  
    def test_verify_device_page_screen_layout(self, eyes):
        """
        Navigate to the PC Device Page and verify the layout of the screen.
        """
        # Maximize application window if required
        if "Maximize myHP" == self.fc.fd["devices"].verify_window_maximize():
            self.fc.fd["devices"].maximize_app()

        # Create an instance of NavigationPanel
        navigation_panel = NavigationPanel(self.driver)

        # Navigate to the device page screen
        navigation_panel.navigate_to_devices()
        
        
        
        