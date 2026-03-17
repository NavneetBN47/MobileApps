import pytest
import time

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"

@pytest.mark.usefixtures("class_setup_fixture_robotics_led_or_button")
class Test_Suite_PenControl_UI(object):

    #this suite should run on willie with trio pen and robotic introduction
  
    @pytest.mark.consumer
    @pytest.mark.function
    @pytest.mark.ota
    def test_01_trio_pen_consumer_C56331599(self):
        assert self.fc.fd["devicesMFE"].verify_pen_card_show() is False, "Pen card is shown before introducing the pen"
        self.vcosmos.introduce_pen()
        self.vcosmos.clean_up_logs()
        self.fc.fd["devicesMFE"].verify_pen_card_show()
        self.fc.fd["devicesMFE"].click_pen_card()
        time.sleep(2)
        #"HP Digital pen" name should be displayed in the UI of the module
        assert self.fc.fd["pen_control"].get_trio_pen_name_consumer() == "HP Digital Pen", "HP Digital Pen is not displayed"
