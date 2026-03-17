from MobileApps.libs.flows.android.smart.flow_container import FLOW_NAMES
import pytest

pytest.app_info = "SMART"

class Test_Suite_01_Printers_UI(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, android_smart_setup, load_printers_session):
        cls = cls.__class__
        cls.driver, cls.fc = android_smart_setup
        cls.p = load_printers_session

        # Define the flows
        cls.home = cls.fc.flow[FLOW_NAMES.HOME]
        cls.printers = cls.fc.flow[FLOW_NAMES.PRINTERS]

        # Define the variable
        cls.printer_ip = cls.p.p_obj.ipAddress
        cls.printer_name = cls.p.get_printer_information()["bonjour name"]

    def test_01_printer_ui(self):
        """
        Description: C31297082
         1. Load Home screen
         2. Click on big "+" or small "+" icon on Home screen
         3. Select Add Printer
        Expected Results:
         3. Verify below points:
           + Navigation bar: back button, printers title, search icon
           + Looking for Wi-Fi Direct Printers? Button
        """
        self.fc.flow_load_home_screen(skip_value_prop=True)
        self.home.load_printer_selection()
        self.printers.select_printer_option_add_printer()
        self.printers.verify_printers_screen()

    def test_02_search_invalid_printer(self):
        """
        Description: C31297084
         1. Load Home screen
         2. Click on Big + button if printer not connected, otherwise clicking small + button
         3. Click on Searching icon on printer lists screen
         4. Enter a invalid printer ip or name

        Expected Result:
         4. There's no printers on the list with keyboard
        """
        self.__search_printer_screen("invalid_name")
        self.printers.verify_search_printers_screen(is_empty=True)

    def test_03_select_printer(self):
        """
        Description: C31297086
         1. Load Home screen
         2. Click on big "+" icon if printer not connected, otherwise clicking small + button
         3. Select a target printer on printer list

        Expected Result:
         3. Verify Home screen with printer connected
        """
        self.fc.flow_load_home_screen(skip_value_prop=True)
        self.fc.flow_home_select_network_printer(self.p)
        self.home.verify_loaded_printer()

    @pytest.mark.parametrize("keyword", ["partial_name", "full_name", "ip"])
    def test_04_select_printer_via_searching_by(self, keyword):
        """
        Description: C31297086, C31297087, C31297088
         1. Load Home screen
         2. Click on big "+" icon if printer not connected, otherwise clicking small + button
         3. Click on Search icon
         4. Enter a valid printer name
         5. Select a target printer on printer list

        Expected Result:
         4. At least one available printer displays on printers list
         5. Verify Home screen with printer connected
        """
        searched_str = {"partial_name": self.printer_name[0:self.printer_name.rfind("[")],
                        "full_name": self.printer_name,
                        "ip": self.printer_ip}
        self.__search_printer_screen(searched_str[keyword])
        number_of_printer = self.printers.count_printers()
        if (keyword == "partial_name" or keyword == "ip") and number_of_printer < 1:
            raise AssertionError("There's no printers on list.")
        elif keyword == "full_name" and number_of_printer != 1:
            raise AssertionError("There's no printers or more than 1 printer on the lists.")

    @pytest.mark.parametrize("path", ["value_prop", "home"])
    def test_05_get_started_button(self, path):
        """
        Description: C31298134
         1. Launch the App and navigate to printer screen based on path param
         2. Tap on "Add Your first Printer" Card or + sign
         3. From the Choose Printer Type screen, Tap on "Get Started" Button
        Verification:
         3. Verify printer connection type screen
          - wifi radio button
          - ethernet radio button
          - "How do you want to connect this printer?" text
          - continue button
        """
        if path == "home":
            self.fc.flow_load_home_screen(skip_value_prop=True)
            self.home.load_printer_selection()
            self.printers.select_printer_option_get_started()
        else:
            self.fc.flow_load_printer_screen_from_value_prop()
        self.printers.verify_printer_connection_type_screen()

    def test_06_printer_options_screen(self):
        """
        Description: C31297527
         1. Launch the App to Home screen
         2. Tap on "Add Your first Printer" Card or + sign to add your printer
        Verification:
         2. Verify Printer Options screen
          - Set up a new printer image
          - Get Started button
          - Add a printer that's already set up image
          - Add printer button
        """
        self.fc.flow_load_home_screen(skip_value_prop=True)
        self.home.load_printer_selection()
        self.printers.verify_printer_options_screen()

    def test_07_printer_option_screen_via_plus_btn(self):
        """
        Description: C31297081, C31298128, C31297083, C31298127, C31298130, C31298131, C31297101, C31297096, C31297089, C31303368
         1. Load Home screen with printer connected (if not, need connect to a printer first)
         2. Click on small "+" button on Home top navigation bar
         3. Select Add Printer
         4. Click on "My printer is not listed" button
         5. Click on Search Again button
         6. Click on "My printer is not listed" button
         7. Click on "Exit Setup" button
         8. Click on Add printer sign from Home screen
         9. Click on Add Printer button

        Expected Results:
         3. Verify Add Printer screen
         4. Verify Help find your printer instruction screen
         5. Verify Add Printer screen
         7. Verify  Home screen
         9. Verify Add Printers screen
        """
        self.fc.flow_load_home_screen(skip_value_prop=True)
        self.fc.flow_home_select_network_printer(self.p, is_searched=True)
        self.home.select_nav_add_icon()
        self.printers.verify_printer_options_screen()
        self.printers.select_printer_option_add_printer()
        self.printers.verify_add_printers_screen()
        self.printers.select_my_printer_is_not_listed()
        self.printers.verify_add_printer_help_find_your_printer_instruction_screen()
        self.printers.select_search_again_button()
        self.printers.verify_add_printers_screen()
        # Verify test case C31297096
        self.printers.select_my_printer_is_not_listed()
        self.printers.select_exit_setup_button()
        self.home.verify_home_nav_add_printer_icon()

    ######################################################################
    #                           PRIVATE FUNCTIONS                        #
    ######################################################################
    def __search_printer_screen(self, key_word):
        """
        - Click on Search icon on Printers screen
        - Verify search screen
        : parameter: keyword
        """
        self.fc.flow_load_home_screen(skip_value_prop=True)
        self.home.load_printer_selection()
        self.printers.select_printer_option_add_printer()
        self.printers.select_search_icon()
        self.printers.search_printer(key_word = key_word)
