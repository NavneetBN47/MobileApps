import pytest
pytest.app_info = "JWEB_VALUE_STORE"

class Test_Suite_04_Value_Store_Remove(object):
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

    def test_01_remove_key_value_pair(self):
        """
        C36117625: Remove Key Value Pair
            - From ValueStore.put(), set key to ApplicationinstanceId and value to 50c7339b-1e88-49d0-9ae6-818bb97d9a8a
            - Click on Set Value button and verify the value pair is created
            - From ValueStore.remove(), send text to Keys input field
            - Click on Remove button and verify the value pair is removed
        """
        self.fc.put_key_value_pair("ApplicationinstanceId", "50c7339b-1e88-49d0-9ae6-818bb97d9a8a", get_result=False)
        self.value_store_plugin.send_text_to_remove_value("ApplicationinstanceId")
        self.value_store_plugin.select_remove_btn()
        result = self.value_store_plugin.get_remove_value_result()['result'][0]
        assert result["key"] == "ApplicationinstanceId", "expecting ApplicationinstanceId: Test1, got: {}".format(result["key"])
        assert result["value"] == "50c7339b-1e88-49d0-9ae6-818bb97d9a8a", "expecting value: 50c7339b-1e88-49d0-9ae6-818bb97d9a8a, got: {}".format(result["value"])
        self.value_store_plugin.send_text_to_get_value_keys("ApplicationinstanceId")
        self.value_store_plugin.select_get_value_btn()
        result = self.value_store_plugin.get_value_store_get_result()['result'][0]
        assert result["key"] == "ApplicationinstanceId", "expecting key: ApplicationinstanceId, got: {}".format(result["key"])
        assert result["value"] == None, "expecting key: None, got: {}".format(result["value"])

    def test_02_remove_multiple_key_value_pairs(self):
        """
        C36117626: Remove multiple Key Value Pairs
            - From ValueStore.put(), use comma separated values to set two keys and two values
            - Click on Set Value button and verify two value pairs are created
            - From ValueStore.remove(), send text to Keys input field
            - Click on Remove button and verify the value pairs are removed
        """
        self.fc.put_key_value_pair("ApplicationinstanceId,StratusUserId", "50c7339b-1e88-49d0-9ae6-818bb97d9a8a,5f918e1cc0788b6c3ef398f5", get_result=False)
        self.value_store_plugin.send_text_to_remove_value("ApplicationinstanceId,StratusUserId")
        self.value_store_plugin.select_remove_btn()
        pair1, pair2 = self.value_store_plugin.get_remove_value_result()['result']
        assert pair1["key"] == "ApplicationinstanceId", "expecting ApplicationinstanceId: Test1, got: {}".format(pair1["key"])
        assert pair1["value"] == "50c7339b-1e88-49d0-9ae6-818bb97d9a8a", "expecting value: 50c7339b-1e88-49d0-9ae6-818bb97d9a8a, got: {}".format(pair1["value"])
        assert pair2["key"] == "StratusUserId", "expecting StratusUserId: Test1, got: {}".format(pair2["key"])
        assert pair2["value"] == "5f918e1cc0788b6c3ef398f5", "expecting value: 5f918e1cc0788b6c3ef398f5, got: {}".format(pair2["value"])
        self.value_store_plugin.send_text_to_get_value_keys("ApplicationinstanceId,StratusUserId")
        self.value_store_plugin.select_get_value_btn()
        pair1, pair2 = self.value_store_plugin.get_value_store_get_result()['result']
        assert pair1["key"] == "ApplicationinstanceId", "expecting key: ApplicationinstanceId, got: {}".format(pair1["key"])
        assert pair1["value"] == None, "expecting key: None, got: {}".format(pair1["value"])
        assert pair2["key"] == "StratusUserId", "expecting key: StratusUserId, got: {}".format(pair2["key"])
        assert pair2["value"] == None, "expecting key: None, got: {}".format(pair2["value"])
