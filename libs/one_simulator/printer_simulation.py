"""
Simulator printer module for creating mock printer objects
that mimic real printer interfaces without hardware dependencies.
"""
import logging
import requests
import MobileApps.libs.one_simulator.printer_information as printer_info
 
def create_simulator_printer_from_api(oneSimulatorServer, modelName, isUSB=False, timeout=30):
    """
    Create a simulator printer object by calling REST API
   
    :param oneSimulatorServer: IP address or hostname of the OneSimulator server
    :param modelName: Profile name for the printer model
    :param isUSB: Whether to create USB connection (default: False for network)
    :param timeout: Request timeout in seconds
    :return: SimulatorPrinter object
    """
    # Build the OneSimulator CreateInstance URL
    api_url = ('http://' + oneSimulatorServer +
               '/onesimulator/CreateInstance?Profile=' + modelName +
               '&ipaddress=&Protocols=IPP,SNMP,CDM,WSDiscovery,LEDM,Bonjour' +
               '&Feature=WSDStatusSimulation,IPPStatusSimulation,LEDMStatusSimulation,Scan,TCPPrint,CDMStatusSimulation' +
               '&isReadWriteEnabled=true&getCommunityName=null&disableDefaultGetCommunity=true' +
               '&setCommunityName=null&userName=null&authenticationType=null&authPassphrase=null' +
               '&privacyType=null&privacyPassphrase=null&isUSB=' + str(isUSB))
   
    logging.info("Calling OneSimulator API: {}".format(api_url))
   
    try:
        response = requests.post(api_url, timeout=timeout)
        response.raise_for_status()
        printer_data = response.json()
       
        logging.info("Created simulator printer from API response: {}".format(printer_data))
       
        # API returns a list, we need the first dictionary
        if isinstance(printer_data, list) and len(printer_data) > 0:
            printer_data = printer_data[0]
       
        return printer_info.PrinterInformation(printer_data)
    except Exception as e:
        logging.error("Failed to get printer info from simulator API: {}".format(str(e)))
        raise

def delete_simulator_printer(oneSimulatorServer, serial_number, timeout=30):
    """
    Delete a simulator printer object by clearing its data
    :param serial_number: Serial number of the printer to delete
    """
    logging.info("Deleting simulator printer: {}".format(serial_number))
    api_url = ('http://' + oneSimulatorServer +
            '/onesimulator/DeleteInstance/' + serial_number)
    logging.info("Calling OneSimulator API: {}".format(api_url))

    try:
        response = requests.delete(api_url, timeout=timeout)
        response.raise_for_status()

        logging.info("Deleted simulator printer successfully")
    except Exception as e:
        logging.error("Failed to delete simulator printer: {}".format(str(e)))
        raise

 