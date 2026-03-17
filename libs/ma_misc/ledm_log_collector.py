from MobileApps.resources.const.printer.const import LEDM_URL
import requests
import os 

class LEDMLogCollector:
    def __init__(self):
        self.printer_ip = None
          
    def collect_product_status_dyn(self):
        # Placeholder for log collection logic
        if not self.printer_ip:
            raise ValueError("Printer IP is not set.")
        try:
            response = requests.get(f"http://{self.printer_ip}{LEDM_URL.PRODUCT_STATUS_DYN}")
            response.raise_for_status()
            return response.text
        except requests.RequestException as e:
            print(f"Error collecting logs: {e}")

    def collect_product_consumable_config_dyn(self):
        # Placeholder for log collection logic
        if not self.printer_ip:
            raise ValueError("Printer IP is not set.")
        try:
            response = requests.get(f"http://{self.printer_ip}{LEDM_URL.PRODUCT_CONSUMABLE_CONFIG_DYN}")
            response.raise_for_status()
            return response.text
        except requests.RequestException as e:
            print(f"Error collecting logs: {e}")
            return None
    
    def collect_product_config_dyn(self):
        # Placeholder for log collection logic
        if not self.printer_ip:
            raise ValueError("Printer IP is not set.")
        try:
            response = requests.get(f"http://{self.printer_ip}{LEDM_URL.PRODUCT_CONFIG_DYN}")
            response.raise_for_status()
            return response.text
        except requests.RequestException as e:
            print(f"Error collecting logs: {e}")
            return None

    def write_log_to_file(self,log_data, file_path):
        if log_data:
            os.makedirs(os.path.dirname(file_path), exist_ok=True)
            with open(file_path, 'w') as log_file:
                log_file.write(log_data)
            print(f"Log written to: {file_path}")
        else:
            print(f"No data to write to {file_path}")
