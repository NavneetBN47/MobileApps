import pytest

pytest.app_info = "JWEB_VALUE_STORE"

class Test_Suite_01_Home_Screen(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, jweb_value_store_test_setup):
        cls = cls.__class__
        cls.driver, cls.fc = jweb_value_store_test_setup
        cls.home = cls.fc.fd["home"]
        cls.weblet_home = cls.fc.fd["weblet_home"]
        cls.value_store = cls.fc.fd["value_store"]
        cls.value_store_plugin = cls.fc.fd["value_store_plugin"]
        cls.home.click_maximize()

    @pytest.fixture(scope="function")
    def reset_application(self):
        self.fc.reset_application()

    @pytest.fixture(autouse=True, scope="function")
    def set_webview_mode(self):
        self.weblet_home.select_webview_mode()
        self.home.select_weblet_tab_nav()

    def test_01_verify_set_subscriber_is_not_clicked(self):
        """
        C36117624: verify the behavior when Set Subscriber is not clicked
            - Put a key value pair in ValueStore.put()
            - Remove key value pair in ValueStore.remove()
            - Verify there are no subscriber events
        """
        self.fc.put_key_value_pair("ApplicationinstanceId", "50c7339b-1e88-49d0-9ae6-818bb97d9a8a")
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
        assert "ValueUpdated" in self.fc.return_and_close_subscriber_alert_text(), "ValueUpdated not found in subscriber alert text"
        assert self.value_store_plugin.verify_subscriber_result("ValueUpdated"), "ValueUpdated not found in subscriber result"
        self.value_store_plugin.send_text_to_remove_value("ApplicationinstanceId")
        self.value_store_plugin.select_remove_btn()
        assert "ValueRemoved" in self.fc.return_and_close_subscriber_alert_text(), "ValueUpdated not found in subscriber alert text"
        assert self.value_store_plugin.verify_subscriber_result("ValueRemoved"), "ValueRemoved not found in subscriber result"
