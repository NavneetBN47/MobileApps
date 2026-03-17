import pytest
import logging
from MobileApps.libs.flows.windows.hpx_rebranding.flow_container import FlowContainer
from MobileApps.libs.flows.web.hpx.printer_status import IorefData
from time import sleep


class PrinterStatusSMSBase:
    """Base class for Printer Status SMS test suites"""
    
    max_retries = 3
    
    def _nav_to_printer_settings_and_trigger_printer_status(self, ioref_num):
        """
        Navigate to printer settings and trigger printer status
        
        Args:
            ioref_num: The IORef number to use (1-15 for different test suites)
        """
        self.fc.fd["devicesMFE"].click_windows_dummy_printer(self.printer_name)
        self.fc.fd["devicesDetailsMFE"].click_view_all_button()
        self.fc.fd["printersettings"].verify_progress_bar()
        self.fc.fd["printersettings"].select_printer_status_item()
        self.fc.fd["printersettings"].select_printer_information()
        self.fc.fd["printer_status"].enable_printer_status(self.serial_number, IorefData.get_ioref_list(num=ioref_num))
        self.fc.fd["printersettings"].select_printer_status_item()
        sleep(2)
        self.fc.fd["printer_status"].verify_ps_ioref_list()
    
    def go_to_printer_status_and_trigger(self, ioref_num):
        """
        Go to Printer device screen and trigger the IORef in printer status screen
        
        Args:
            ioref_num: The IORef number to use (1-15 for different test suites)
        """
        for attempt in range(self.max_retries):
            try:
                if attempt == 0:
                    self.fc.launch_hpx_to_home_page()
                    self.fc.add_a_printer(self.p)
                else:
                    self.fc.reset_hpx(self.p)

                self._nav_to_printer_settings_and_trigger_printer_status(ioref_num)
                self.trigger_status['status'] = True
                break
            except Exception as e:
                if attempt < self.max_retries - 1:
                    logging.info(f"Test failed on attempt {attempt + 1}, restarting app and retrying... Error: {e}")
                    self.fc.restart_hpx()
                    
                    # Check if printer exists after restart
                    printer_exists = self.fc.fd["devicesMFE"].verify_windows_dummy_printer(self.printer_name, timeout=30, raise_e=False)
                    
                    try:
                        if not printer_exists:
                            self.fc.add_a_printer(self.p)
                        else:
                            logging.info(f"Printer found after restart, skipping add printer step")
                        
                        # Navigate to printer settings and trigger status
                        self._nav_to_printer_settings_and_trigger_printer_status(ioref_num)
                        self.trigger_status['status'] = True
                        logging.info(f"Retry attempt {attempt + 1} succeeded")
                        break
                    except Exception as retry_error:
                        logging.info(f"Retry attempt {attempt + 1} also failed: {retry_error}")
                        if attempt == self.max_retries - 2:
                            raise
                else:
                    logging.info(f"Test failed after {self.max_retries} attempts")
                    raise
