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

    def test_01_put_create_value_pair(self):
        """
        C36117614: Create a value pair
            - From ValueStore.put(), set key to ApplicationinstanceId and value to 50c7339b-1e88-49d0-9ae6-818bb97d9a8a
            - Click on Set Value button
            - Verify the value pair is created
        """
        result = self.fc.put_key_value_pair("ApplicationinstanceId", "50c7339b-1e88-49d0-9ae6-818bb97d9a8a")[0]
        assert result["key"] == "ApplicationinstanceId", "expecting key: ApplicationinstanceId, got: {}".format(result["key"])
        assert result["value"] == "50c7339b-1e88-49d0-9ae6-818bb97d9a8a", "expecting value: 50c7339b-1e88-49d0-9ae6-818bb97d9a8a, got: {}".format(result["value"])

    def test_02_put_create_multiple_value_pairs(self):
        """
        C36117615: Create multiple value pairs
            - From ValueStore.put(), use comma separated values to set two keys and two values
            - Click on Set Value button
            - Verify two value pairs are created
        """
        pair1, pair2 = self.fc.put_key_value_pair("ApplicationinstanceId,StratusUserId", "50c7339b-1e88-49d0-9ae6-818bb97d9a8a,5f918e1cc0788b6c3ef398f5")
        assert pair1["key"] == "ApplicationinstanceId", "expecting key: ApplicationinstanceId, got: {}".format(pair1["key"])
        assert pair1["value"] == "50c7339b-1e88-49d0-9ae6-818bb97d9a8a", "expecting value: 50c7339b-1e88-49d0-9ae6-818bb97d9a8a, got: {}".format(pair1["value"])
        assert pair2["key"] == "StratusUserId", "expecting key: StratusUserId, got: {}".format(pair2["key"])
        assert pair2["value"] == "5f918e1cc0788b6c3ef398f5", "expecting value: 50c7339b-1e88-49d0-9ae6-818bb97d9a8a, got: {}".format(pair2["value"])

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
        self.fc.put_key_value_pair("ApplicationinstanceId", "50c7339b-1e88-49d0-9ae6-818bb97d9a8a")
        result = self.fc.put_key_value_pair("ApplicationinstanceId", "new_value")[0]
        assert result["key"] == "ApplicationinstanceId", "key not found in response"
        assert result["value"] == "new_value", "new value not updated"
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
        self.fc.put_key_value_pair("ApplicationinstanceId,StratusUserId", "50c7339b-1e88-49d0-9ae6-818bb97d9a8a,5f918e1cc0788b6c3ef398f5")
        pair1, pair2 = self.fc.put_key_value_pair("ApplicationinstanceId,StratusUserId", "new_value1,new_value2")
        assert pair1["key"] == "ApplicationinstanceId", "expecting key: ApplicationinstanceId, got: {}".format(pair1["key"])
        assert pair1["value"] == "new_value1", "expecting value: new_value1, got: {}".format(pair1["value"])
        assert pair1["oldValue"] == "50c7339b-1e88-49d0-9ae6-818bb97d9a8a", "expecting value: 50c7339b-1e88-49d0-9ae6-818bb97d9a8a, got: {}".format(pair1["oldValue"])
        assert pair2["key"] == "StratusUserId", "expecting key: StratusUserId, got: {}".format(pair2["key"])
        assert pair2["value"] == "new_value2", "expecting value: new_value2, got: {}".format(pair2["value"])
        assert pair2["oldValue"] == "5f918e1cc0788b6c3ef398f5", "expecting value: 5f918e1cc0788b6c3ef398f5, got: {}".format(pair1["oldValue"])

    def test_05_put_key_blank(self, reset_application):
        """
        C36117618: Verify the behavior on Put when Key is blank
            - From ValueStore.put(), set ensure key value is empty and value is set
            - Click on Set Value button
            - Verify the InvalidOption error
        """
        result = self.fc.put_key_value_pair("", "50c7339b-1e88-49d0-9ae6-818bb97d9a8a")[0]
        assert result['errorReason'] == "Provided Key was empty"
        assert result['errorType'] == "InvalidOptions"

    def test_06_put_value_blank(self, reset_application):
        """
        C36117619: Verify the behavior on Put when Value is blank
            - From ValueStore.put(), set ensure key value is set and value is empty
            - Click on Set Value button
            - Verify the empty value for key is created
        """
        result = self.fc.put_key_value_pair("ApplicationinstanceId", "")[0]
        assert result['errorReason'] == "Provided value is null or empty"
        assert result['errorType'] == "UnknownError"

    def test_07_put_key_and_value_blank(self, reset_application):
        """
        C36117620: Verify the behavior on Put when Key and Value are blank
            - From ValueStore.put(), set ensure key value and value are empty
            - Click on Set Value button
            - Verify the value pair is not created
        """
        result = self.fc.put_key_value_pair("", "")[0]
        assert result['errorReason'] == "Provided Key was empty"
        assert result['errorType'] == "InvalidOptions"

    def test_08_put_user_defined_key_value_pair(self):
        """
        C36117621: Create a user defined key value pair
            - From ValueStore.put(), set key to user defined key and value to user defined value
            - Click on Set Value button
            - Verify the value pair is created
        """
        result = self.fc.put_key_value_pair("Test1", "10")[0]
        assert result["key"] == "Test1", "expecting key: Test1, got: {}".format(result["key"])
        assert result["value"] == "10", "expecting value: 10, got: {}".format(result["value"])

    def test_09_put_multiple_user_defined_key_value_pair(self):
        """
        C36117622: Create multiple user defined key value pairs
            - From ValueStore.put(), set two keys to user defined key and two values to user defined value
            - Click on Set Value button
            - Verify the two value pairs are created
        """
        pair1, pair2 = self.fc.put_key_value_pair("Test1,Test2", "10,20")
        assert pair1["key"] == "Test1", "expecting key: Test1, got: {}".format(pair1["key"])
        assert pair1["value"] == "10", "expecting value: 10, got: {}".format(pair1["value"])
        assert pair2["key"] == "Test2", "expecting key: Test2, got: {}".format(pair2["key"])
        assert pair2["value"] == "20", "expecting value: 20, got: {}".format(pair2["value"])
