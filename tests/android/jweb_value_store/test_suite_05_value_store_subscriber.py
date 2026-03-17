import pytest
pytest.app_info = "JWEB_VALUE_STORE"

class Test_Suite_05_Value_Store_Subscriber(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, android_jweb_value_store_setup):
        cls = cls.__class__
        cls.driver, cls.fc = android_jweb_value_store_setup

        cls.home = cls.fc.fd["home"]
        cls.native = cls.fc.fd["native"]
        cls.value_store_plugin = cls.fc.fd["value_store_plugin"]

    @pytest.fixture(scope="function", autouse="true")
    def navigate_to_home_screen(self):
        self.fc.flow_load_home_screen()
        self.home.select_weblet_tab_nav()

    def test_01_verify_set_subscriber_is_not_clicked(self):
        """
        C36117624: verify the behavior when Set Subscriber is not clicked
            - Put a key value pair in ValueStore.put()
            - Remove key value pair in ValueStore.remove()
            - Verify there are no subscriber events
        """
        self.fc.put_key_value_pair("ApplicationinstanceId", "50c7339b-1e88-49d0-9ae6-818bb97d9a8a", get_result=False)
        assert not self.value_store_plugin.get_subscriber_alert_text(raise_e=False), "Undesired subscriber alert popup found"
        self.value_store_plugin.send_text_to_remove_value("ApplicationinstanceId")
        self.value_store_plugin.select_remove_btn()
        assert not self.value_store_plugin.get_subscriber_alert_text(raise_e=False), "Undesired subscriber alert popup found"

    def test_02_verify_set_subscriber_is_clicked(self):
        """
        C36117623: verify the behavior when Set Subscriber is clicked
            - Click on Set Subscriber button
            - Put a key value pair in ValueStore.put()
            - Remove key value pair in ValueStore.remove()
            - Verify subscriber events ValueUpdated and ValueRemoved
        """
        self.value_store_plugin.select_set_subscriber_btn()
        self.fc.put_key_value_pair("ApplicationinstanceId", "50c7339b-1e88-49d0-9ae6-818bb97d9a8a", get_result=False)
        toast_text = self.fc.return_and_close_subscriber_alert_text()
        assert "ValueUpdated" in toast_text, "ValueUpdated not found in subscriber alert text"
        assert self.value_store_plugin.verify_subscriber_result("ValueUpdated"), "ValueUpdated not found in subscriber result"
        self.value_store_plugin.send_text_to_remove_value("ApplicationinstanceId")
        self.value_store_plugin.select_remove_btn()
        assert "ValueRemoved" in self.fc.return_and_close_subscriber_alert_text(), "ValueUpdated not found in subscriber alert text"
        assert self.value_store_plugin.verify_subscriber_result("ValueRemoved"), "ValueRemoved not found in subscriber result"
