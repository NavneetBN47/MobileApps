import json
from MobileApps.libs.ma_misc.ma_misc import get_ecp_account_info

def load_journey_printer_info(stack):
    ecp_account_info = get_ecp_account_info(stack)
    if not ecp_account_info.get("printers", False):
        raise KeyError(f"Account info for stack: {stack} does not have a 'printers' field")

    printers = []
    for key, value in ecp_account_info["printers"].items():
        if value.get("journey_validation", False):
            printers.append((key, value))

    if len(printers) > 0:
        return printers
    else:
        raise KeyError(f"Account: {stack} has no 'journey_validation' printers")
