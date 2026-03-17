from MobileApps.libs.flows.web.jweb.jweb_flow import JwebFlow

class LoggerPlugin(JwebFlow):
    flow_name = "logger_plugin"

    def input_text_output_file_name(self, text):
        """
        Logger.createLogger() tab, insert text into Output file name textbox
        """
        self.driver.send_keys("output_file_name_text_box", text)

    def toggle_create_logger_checkboxes(self, checkbox_name, checkbox_value):
        """
        Logger.createLogger() tab, select checkbox_name option
        """
        checkbox_list = ["write_to_console", "file_name", "module_name", "method_name", "line_number", "stack_trace"]
        if checkbox_name not in checkbox_list:
            raise ValueError("Checkbox:{} not present within createLogger() selection".format(checkbox_name))
        
        checkbox_index = checkbox_list.index(checkbox_name)
        checkbox_value = str(checkbox_value).lower()
        if self.driver.wait_for_object("logger_checkbox", index=checkbox_index).get_attribute('aria-checked') != checkbox_value:
            self.driver.click("logger_checkbox", index=checkbox_index)

    def set_log_level_threshold(self, threshold_option):
        """
        Logger.createLogger() tab, open log threshold drop down, and select log level threshold
        """
        threshold_option = threshold_option.lower()
        if threshold_option not in ['trace', 'debug', 'info', 'warning', 'error']:
            raise ValueError("Threshold Option:{} not present within set log threshold dropdown")
        
        self.driver.click("open_log_level_trace_list_btn")
        self.driver.click("log_level_{}_option".format(threshold_option))

    def select_create_logger_btn(self):
        """
        Logger.createLogger() tab, click on the create logger button
        """
        self.driver.click("create_logger_btn")

    def select_logger_instance_first_option(self):
        """
        Logger.Log() tab, click on the create logger button
        """
        self.driver.click("open_log_drop_down_btn", index=0)
        self.driver.click("logger_instance_first_option")

    def insert_text_into_log_message_textbox(self, text):
        """
        Logger.Log() tab, send keys to log message textbox
        """
        self.driver.send_keys("log_message_textbox", text)

    def select_message_type_btn(self):
        """
        Logger.Log() tab, open message type dropdown button
        """
        self.driver.click("open_log_drop_down_btn", index=1)

    def set_log_message_level_threshold(self, threshold_option):
        """
        Logger.Log() tab, while creating a log, select a log threshold option
        """
        threshold_option = threshold_option.lower()
        if threshold_option not in ['trace', 'debug', 'info', 'warning', 'error']:
            raise ValueError("Threshold Option:{} not present within set log threshold dropdown")
        
        self.driver.click("open_log_drop_down_btn", index=2)
        self.driver.click("log_level_{}_option".format(threshold_option))

    def select_log_message_btn(self):
        """
        Logger.Log() tab, log a message
        """
        self.driver.click("log_message_btn")