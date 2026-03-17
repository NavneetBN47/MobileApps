import pytest
pytest.app_info = "JWEB_VALUE_STORE"

class Test_Suite_02_Value_Store_Put(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, ios_jweb_value_store_setup):
        cls = cls.__class__
        cls.driver, cls.fc = ios_jweb_value_store_setup

        cls.home = cls.fc.fd["home"]
        cls.native = cls.fc.fd["native"]
        cls.value_store_plugin = cls.fc.fd["value_store_plugin"]

    def test_01_put_create_value_pair(self):
        """
        C36117614: Create a value pair
            - From ValueStore.put(), set key to ApplicationinstanceId and value to 50c7339b-1e88-49d0-9ae6-818bb97d9a8a
            - Click on Set Value button
            - Verify the value pair is created
        """
        self.home.select_weblet_tab_nav()
        result = self.fc.put_key_value_pair("ApplicationinstanceId", "50c7339b-1e88-49d0-9ae6-818bb97d9a8a")[0]
        assert result["key"] == "ApplicationinstanceId", "expecting key: ApplicationinstanceId, got: {}".format(result["key"])
        assert result["newValue"] == "50c7339b-1e88-49d0-9ae6-818bb97d9a8a", "expecting value: 50c7339b-1e88-49d0-9ae6-818bb97d9a8a, got: {}".format(result["newValue"])

    def test_02_put_create_multiple_value_pairs(self):
        """
        C36117615: Create multiple value pairs
            - From ValueStore.put(), use comma separated values to set two keys and two values
            - Click on Set Value button
            - Verify two value pairs are created
        """
        self.home.select_weblet_tab_nav()
        pair1, pair2 = self.fc.put_key_value_pair("ApplicationinstanceId,StratusUserId", "50c7339b-1e88-49d0-9ae6-818bb97d9a8a,5f918e1cc0788b6c3ef398f5")
        assert pair1["key"] == "ApplicationinstanceId", "expecting key: ApplicationinstanceId, got: {}".format(pair1["key"])
        assert pair1["newValue"] == "50c7339b-1e88-49d0-9ae6-818bb97d9a8a", "expecting value: 50c7339b-1e88-49d0-9ae6-818bb97d9a8a, got: {}".format(pair1["newValue"])
        assert pair2["key"] == "StratusUserId", "expecting key: StratusUserId, got: {}".format(pair2["key"])
        assert pair2["newValue"] == "5f918e1cc0788b6c3ef398f5", "expecting value: 50c7339b-1e88-49d0-9ae6-818bb97d9a8a, got: {}".format(pair2["newValue"])

    def test_03_put_update_key_value_pair(self):
        """
        C36117616: Update a key value pair
            - From ValueStore.put(), set key to ApplicationinstanceId and value to 50c7339b-1e88-49d0-9ae6-818bb97d9a8a
            - Click on Set Value button
            - Verify the value pair is created
            - From ValueStore.put(), set same key but new value 
            - Click on Set Value button
            - Verify the value pair is updated
        """
        self.home.select_weblet_tab_nav()
        self.fc.put_key_value_pair("ApplicationinstanceId", "50c7339b-1e88-49d0-9ae6-818bb97d9a8a")
        result = self.fc.put_key_value_pair("ApplicationinstanceId", "new_value")[0]
        assert result["key"] == "ApplicationinstanceId", "key not found in response"
        assert result["newValue"] == "new_value", "new value not updated"
        assert result["oldValue"] == "50c7339b-1e88-49d0-9ae6-818bb97d9a8a", "value not found in response"

    def test_04_put_update_multiple_key_value_pairs(self):
        """
        C36117617: Update multiple key value pairs
            - From ValueStore.put(), use comma separated values to set two keys and two values
            - Click on Set Value button
            - Verify two value pairs are created
            - From ValueStore.put(), use comma separated values to set same two keys but new values
            - Click on Set Value button
            - Verify two value pairs are updated
        """
        self.home.select_weblet_tab_nav()
        self.fc.put_key_value_pair("ApplicationinstanceId,StratusUserId", "50c7339b-1e88-49d0-9ae6-818bb97d9a8a,5f918e1cc0788b6c3ef398f5")
        pair1, pair2 = self.fc.put_key_value_pair("ApplicationinstanceId,StratusUserId", "new_value1,new_value2")
        assert pair1["key"] == "ApplicationinstanceId", "expecting key: ApplicationinstanceId, got: {}".format(pair1["key"])
        assert pair1["newValue"] == "new_value1", "expecting value: new_value1, got: {}".format(pair1["newValue"])
        assert pair1["oldValue"] == "50c7339b-1e88-49d0-9ae6-818bb97d9a8a", "expecting value: 50c7339b-1e88-49d0-9ae6-818bb97d9a8a, got: {}".format(pair1["oldValue"])
        assert pair2["key"] == "StratusUserId", "expecting key: StratusUserId, got: {}".format(pair2["key"])
        assert pair2["newValue"] == "new_value2", "expecting value: new_value2, got: {}".format(pair2["newValue"])
        assert pair2["oldValue"] == "5f918e1cc0788b6c3ef398f5", "expecting value: 5f918e1cc0788b6c3ef398f5, got: {}".format(pair1["oldValue"])

    def test_05_put_key_blank(self):
        """
        C36117618: Verify the behavior on Put when Key is blank
            - From ValueStore.put(), set ensure key value is empty and value is set
            - Click on Set Value button
            - Verify the InvalidOption error
        """
        self.home.select_weblet_tab_nav()
        result = self.fc.put_key_value_pair("", "50c7339b-1e88-49d0-9ae6-818bb97d9a8a")[0]
        assert result['errorReason'] == "Key is invalid"
        assert result['errorType'] == "InvalidOptions"

    def test_06_put_value_blank(self):
        """
        C36117619: Verify the behavior on Put when Value is blank
            - From ValueStore.put(), set ensure key value is set and value is empty
            - Click on Set Value button
            - Verify the empty value for key is created
        """
        self.home.select_weblet_tab_nav()
        result = self.fc.put_key_value_pair("ApplicationinstanceId", "")[0]
        assert result["key"] == "ApplicationinstanceId", "expecting key: ApplicationinstanceId, got: {}".format(result["key"])
        assert result["newValue"] == "", "expecting value: '', got: {}".format(result["newValue"])

    def test_07_put_key_and_value_blank(self):
        """
        C36117620: Verify the behavior on Put when Key and Value are blank
            - From ValueStore.put(), set ensure key value and value are empty
            - Click on Set Value button
            - Verify the value pair is not created
        """
        self.home.select_weblet_tab_nav()
        result = self.fc.put_key_value_pair("", "")[0]
        assert result['errorReason'] == "Key is invalid"
        assert result['errorType'] == "InvalidOptions"

    def test_08_put_user_defined_key_value_pair(self):
        """
        C36117621: Create a user defined key value pair
            - From ValueStore.put(), set key to user defined key and value to user defined value
            - Click on Set Value button
            - Verify the value pair is created
        """
        self.home.select_weblet_tab_nav()
        result = self.fc.put_key_value_pair("Test1", "10")[0]
        assert result["key"] == "Test1", "expecting key: Test1, got: {}".format(result["key"])
        assert result["newValue"] == "10", "expecting value: 10, got: {}".format(result["newValue"])

    def test_09_put_multiple_user_defined_key_value_pair(self):
        """
        C36117622: Create multiple user defined key value pairs
            - From ValueStore.put(), set two keys to user defined key and two values to user defined value
            - Click on Set Value button
            - Verify the two value pairs are created
        """
        self.home.select_weblet_tab_nav()
        pair1, pair2 = self.fc.put_key_value_pair("Test1,Test2", "10,20")
        assert pair1["key"] == "Test1", "expecting key: Test1, got: {}".format(pair1["key"])
        assert pair1["newValue"] == "10", "expecting value: 10, got: {}".format(pair1["newValue"])
        assert pair2["key"] == "Test2", "expecting key: Test2, got: {}".format(pair2["key"])
        assert pair2["newValue"] == "20", "expecting value: 20, got: {}".format(pair2["newValue"])
