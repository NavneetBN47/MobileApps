import logging


class LivePrinter:
    """Container for live printer identity and connection string generation."""

    def __init__(self, ip_address, product_name=None):
        self.ip_address = ip_address
        self.product_name = product_name
    
    def get_printer_information(self):
        """
        Get printer information in the format expected by the framework.
        
        :return: Dictionary with keys: ip address, model name
        """
        return {
            "ip address": self.ip_address,
            "model name": self.product_name
        }

    def create_printer_object(ip_address, product_name=None):
        """
        Create a live/manual printer object from explicit network identity.
        
        Returns a LivePrinter object that mimics the interface of a real printer,
        similar to how create_simulator_printer_from_api returns a PrinterInformation wrapper.

        :param ip_address: Live printer IP or hostname
        :param product_name: Optional product/printer name for logging only
        :return: LivePrinter object with get_printer_information() method
        """
        if not ip_address:
            raise ValueError("ip_address is required to create a live printer object")
        
        printer_obj = LivePrinter(ip_address, product_name)
        logging.info(
            "Creating live printer object with host: %s model: %s",
            ip_address,
            product_name,
        )
        return printer_obj