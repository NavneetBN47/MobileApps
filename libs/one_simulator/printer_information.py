class PrinterInformation:
    """
    Simulator printer class that mimics the interface of a real printer object
    but uses data from REST API or manual configuration instead of hardware.
    """
    def __init__(self, printer_data):
        self.printer_data = printer_data
        self.status = "Ready"  # Simulator is always ready
        self.p_con = None  # No real connection for simulator
        self.p_obj = None  # No real printer object for simulator
        self.printer_cdm = None  # No CDM for simulator
   
    def get_printer_information(self):
        """
        Get information of printer with following keys:
            - serial number
            - ip address
            :return: dictionary of printer information
        """
        # Return simulated printer information instead of accessing real hardware
       
        printer_info = { 
            "serial number": self.printer_data.get("SerialNumber"),
            "ip address":  self.printer_data.get("IpAddress"),
            "model name": self.printer_data.get("ModelName")
        }
        return printer_info