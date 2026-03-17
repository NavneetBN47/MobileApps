import time
import pytest

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"

@pytest.mark.usefixtures("class_setup_fixture_funtional_ota")
class Test_Perform_AIC(object):
   
    #this suite should run on uktron, bopeep or System must have <8 GB of RAM platforms
    @pytest.mark.ota
    @pytest.mark.function
    def test_01_verify_aic_visibilty_on_non_supported_platform_C57033741(self):
        button_verified = self.fc.fd["devicesMFE"].verify_hpai_assistant_button_on_header()
        assert button_verified is not True, f"HP AI Assistant button should not be visible on unsupported platform, but found element: {button_verified}"
        self.fc.close_myHP()