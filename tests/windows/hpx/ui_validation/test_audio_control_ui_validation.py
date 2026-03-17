import pytest
from PIL import Image
import time
import requests

from MobileApps.libs.flows.windows.hpx.navigation_panel import NavigationPanel
from MobileApps.tests.windows.hpx.ui_validation.ui_validation_helpers import *
from applitools.images import Eyes, BatchInfo, TestResults

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"

class Test_Suit_Audio_Control_UI_Validation_C50712695:
    @pytest.mark.applitools
    @screenshot_test("Smoke Test - Audio Control Layout")  
    def test_verify_audio_control_screen_layout(self, eyes):
        """
        Navigate to the PC audio control screen and verify the layout of the screen.
        """
        # Maximize application window if required
        if "Maximize myHP" == self.fc.fd["devices"].verify_window_maximize():
            self.fc.fd["devices"].maximize_app()

        # Create an instance of NavigationPanel
        navigation_panel = NavigationPanel(self.driver)

        # Navigate to the PC audio control screen
        navigation_panel.navigate_to_pc_audio()
       