import pytest
from PIL import Image
import time

from MobileApps.libs.flows.windows.hpx.navigation_panel import NavigationPanel
from MobileApps.tests.windows.hpx.ui_validation.ui_validation_helpers import *
from applitools.images import Eyes, BatchInfo

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"

class Test_Suit_Screen_Distance_UI_Validation_C50712702:
    @pytest.mark.applitools
    @screenshot_test("Smoke Test - Screen Distance Layout")  
    def test_verify_screen_distance_screen_layout(self, eyes):
        """
        Navigate to the screen distance screen and verify the layout of the screen.
        """
        if "Maximize myHP" == self.fc.fd["devices"].verify_window_maximize():
            self.fc.fd["devices"].maximize_app()

        # Create an instance of NavigationPanel
        navigation_panel = NavigationPanel(self.driver)

        # Navigate to the screen distance screen
        navigation_panel.navigate_to_screen_distance()

            