import pytest
pytest.app_info = "JWEB_VALUE_STORE"

class Test_Suite_03_Value_Store_Get(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, ios_jweb_value_store_setup):
        cls = cls.__class__
        cls.driver, cls.fc = ios_jweb_value_store_setup

        cls.home = cls.fc.fd["home"]
        cls.native = cls.fc.fd["native"]
        cls.value_store_plugin = cls.fc.fd["value_store_plugin"]

    def test_01_get_key_value_pair(self):
        """
        C36117627: Get a key value pair
            - From ValueStore.put(), set key to ApplicationinstanceId and value to 50c7339b-1e88-49d0-9ae6-818bb97d9a8a
            - Click on Set Value button and verify the value pair is created
            - From ValueStore.get(), send text to Keys input field
            - Click on Get Value button and verify the value pair is returned
        """
        self.home.select_weblet_tab_nav()
        self.fc.put_key_value_pair("ApplicationinstanceId", "50c7339b-1e88-49d0-9ae6-818bb97d9a8a")
        self.value_store_plugin.send_text_to_get_value_keys("ApplicationinstanceId")
        self.value_store_plugin.select_get_value_btn()
        result = self.value_store_plugin.get_value_store_get_result()['result'][0]
        assert result["key"] == "ApplicationinstanceId", "expecting key: ApplicationinstanceId, got: {}".format(result["key"])
        assert result["value"] == "50c7339b-1e88-49d0-9ae6-818bb97d9a8a", "expecting value: 50c7339b-1e88-49d0-9ae6-818bb97d9a8a, got: {}".format(result["value"])

    def test_02_get_multiple_key_value_pairs(self):
        """
        C36117628: Get multiple key value pairs
            - From ValueStore.put(), use comma separated values to set two keys and two values
            - Click on Set Value button and verify two value pairs are created
            - From ValueStore.get(), send text to Keys input field
            - Click on Get Value button and verify the value pairs are returned
        """
        self.home.select_weblet_tab_nav()
        self.fc.put_key_value_pair("ApplicationinstanceId,StratusUserId", "50c7339b-1e88-49d0-9ae6-818bb97d9a8a,5f918e1cc0788b6c3ef398f5")
        self.value_store_plugin.send_text_to_get_value_keys("ApplicationinstanceId,StratusUserId")
        self.value_store_plugin.select_get_value_btn() 
        pair1, pair2 = self.value_store_plugin.get_value_store_get_result()['result']
        assert pair1["key"] == "ApplicationinstanceId", "expecting key: ApplicationinstanceId, got: {}".format(pair1["key"])
        assert pair1["value"] == "50c7339b-1e88-49d0-9ae6-818bb97d9a8a", "expecting value: 50c7339b-1e88-49d0-9ae6-818bb97d9a8a, got: {}".format(pair1["value"])
        assert pair2["key"] == "StratusUserId", "expecting key: StratusUserId, got: {}".format(pair2["key"])
        assert pair2["value"] == "5f918e1cc0788b6c3ef398f5", "expecting value: 5f918e1cc0788b6c3ef398f5, got: {}".format(pair2["value"])
