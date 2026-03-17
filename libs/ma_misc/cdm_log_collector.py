from MobileApps.resources.const.printer.const import CDM_URL
import requests
import os

class CDMLogCollector:
    def __init__(self):
        self.printer_ip = None

    def collect_supplies_public(self):
        # Placeholder for log collection logic
        if not self.printer_ip:
            raise ValueError("Printer IP is not set.")
        try:
            response = requests.get(f"http://{self.printer_ip}{CDM_URL.CDM_SUPPLIES_PUBLIC}")
            response.raise_for_status()
            return response.text
        except requests.RequestException as e:
            print(f"Error collecting logs: {e}")
    
    def collect_alerts(self):
        # Placeholder for log collection logic
        if not self.printer_ip:
            raise ValueError("Printer IP is not set.")
        try:
            response = requests.get(f"http://{self.printer_ip}{CDM_URL.CDM_ALERTS}")
            response.raise_for_status()
            return response.text
        except requests.RequestException as e:
            print(f"Error collecting logs: {e}")

    def write_log_to_file(self,log_data, file_path):
        if log_data:
            os.makedirs(os.path.dirname(file_path), exist_ok=True)
            with open(file_path, 'w') as log_file:
                log_file.write(log_data)
            print(f"Log written to: {file_path}")
        else:
            print(f"No data to write to {file_path}")