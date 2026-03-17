import pytest
from PIL import Image
import time
import time

from MobileApps.libs.flows.windows.hpx.navigation_panel import NavigationPanel
from MobileApps.tests.windows.hpx.ui_validation.ui_validation_helpers import *
from applitools.images import Eyes, BatchInfo

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"

class Test_Suit_System_Control_UI_Validation_C50712704:
    @pytest.mark.applitools
    @screenshot_test("Smoke Test - System Control Layout")  
    def test_verify_system_control_screen_layout(self, eyes):
        """
        Navigate to the PC system control screen and verify the layout of the screen.
        """
        if "Maximize myHP" == self.fc.fd["devices"].verify_window_maximize():
            self.fc.fd["devices"].maximize_app()

        # Create an instance of NavigationPanel
        navigation_panel = NavigationPanel(self.driver)

        # Navigate to the PC audio control screen
        navigation_panel.navigate_to_pc_audio()

           