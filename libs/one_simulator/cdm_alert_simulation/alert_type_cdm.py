
"""
OneSimulator Error Simulator Module
Provides structured error simulation capabilities for printer testing
"""
import logging
import requests
from enum import Enum
from typing import Dict

class AlertTypeCDM(Enum):
    """Enumeration of supported error types with CDM message IDs"""
    READY = "Ready"

    #Errors
    ANTI_THEFT_ENABLED_ERROR_65612 = "antiTheftEnabledError_65612"
    ANTI_THEFT_ENABLED_ERROR_66175 = "antiTheftEnabledError_66175"
    CARTRIDGES_MISSING_65537 ="Cartridge_Missing_65537"
    CARTRIDGE_FAULTY_65542 = "Cartridge_Faulty_65542"
    INCOMPATIBLE_CARTRIDGE_65543 = "IncompatibleCartridge_65543"
    CARTRIDGE_IN_WRONG_SLOT_65544 = "Cartridge_Wrong_Slot_65544"
    CARTRIDGE_EXPECTED_SETUP_65590 = "CartridgeExpectedSetup_65590"
    CARTRIDGEEXPECTEDSETUP_LOW_65590="CartridgeExpectedSetup_Low_65590"
    CARTRIDGEEXPECTEDSETUP_VERYLOW_65590="CartridgeExpectedSetup_VeryLow_65590"
    CARTRIDGEEXPECTEDSETUP_ALTERED_SUPPLY_65590="CartridgeExpectedSetup_Altered_Supply_65590"
    CARTRIDGE_NON_EXPECTED_65591 = "CartridgeNonExpected_65591"
    UNSUBSCRIBEDSTATE_INCOMPATIBLE_INK_65765 = "UnSubscribedState_InCompatible_Ink_65765"
    CARTRIDGE_MISSING_66262 = "Cartridge_Missing_66262"
    CARTRIDGE_PROBLEM_66277="cartridge_problem_66277"
    CARTRIDGE_PROBLEM_66278="cartridge_problem_66278"
    CARTRIDGE_PROBLEM_66279="cartridge_problem_66279"
    INCOMPATIBLE_CARTRIDGES_66283="incompatible_cartridges_66283"
    INCOMPATIBLE_CARTRIDGES_66284="incompatible_cartridges_66284"
    INCOMPATIBLE_CARTRIDGES_66285="incompatible_cartridges_66285"
    CARTRIDGES_REJECTED_66293="cartridges_rejected_66293"
    USE_SETUP_CARTRIDGES_66297="use_setup_cartridges_66297"
    DO_NOT_USE_SETUP_CARTRIDGES_66299="do_not_use_setup_cartridges_66299"
    DO_NOT_USE_SETUP_CARTRIDGES_66300="do_not_use_setup_cartridges_66300"
    HP_PROTECTED_CARTRIDGES_INSTALLED_66304="hp_protected_cartridges_installed_66304"
    HP_PROTECTED_CARTRIDGES_INSTALLED_66305="hp_protected_cartridges_installed_66305"
    HP_INSTANT_INK_66315="hp_instant_ink_66315"
    NONHP_CHIP_DETECTED_66339="nonhp_chip_detected_66339"
    NONHP_CIRCUITRY_DETECTED_66341="Non_HP_Circuitry_66341"
    DO_NOT_USE_SETUP_CARTRIDGES_66298="do_not_use_setup_cartridges_66298"
    INCOMPATIBLE_CARTRIDGE_65543_REGION="Incompatible_Cartridge_Region_65543"
    OUTOFINK_66019="OutOfInk_66019"
    PRINTHEADPROBLEM_66207="PrintHeadProblem_66207"
    INCOMPATABLE_PRINTHEAD="Incompatible_Printhead_66213"
    NON_HP_CHIP="Non_HP_Chip_66339"
    OOBE_HP_TRADE_66175="OOBE_HP_Trade_66175"
    OOBE_HP_ALTERED_SUPPLY_ANTI_THEFT_66175="OOBE_HP_Altered_Supply_Anti-Theft_66175"
    OOBE_HP_ALTERED_SUPPLY_66175_HPPLUS="OOBE_HP_Altered_Supply_66175_HPplus"
    OOBE_LOI_SUPPLY_66175="OOBE_LOI_Supply_66175"
    OOBE_VLOI_SUPPLY_66175="OOBE_VLOI_Supply_66175"
    OOBE_FAULTY_SUPPLY_SHORTED_CONTACTPADS_66175="OOBE_Faulty_Supply_Shorted_contactpads_66175"
    DO_NOT_USE_SETUP_OOBE_PRINTER_TRIAL_PEN_66175="Do_not_use_SETUP_OOBE printer/Trial_Pen_66175"
    HP_ALTERED_SUPPLY_INSERT_T4_PEN_FROM_ANOTHER_PRINTER_66175="HP_Altered_Supply_(insert T4 pen)_from_another_printer_66175"
    NON_HP_CIRCUITRY_66175="Non_HP_Circuitry_66175"
    HPPI_CIRCUITRY_PEN_DIGITAL_SIGNATURE="HPII_Circuitry/Pen Digital Signature_66175"
    PEN_TYPE_PROTO_BIT_REGIONALISATION_SECTION_66175="Pen_Type/Proto_bit/Regionalisation_Section_66175"
    INCOMPATIBLE_HP_INSTANT_INK_66175="Incompatible_HP_Instant Ink_66175"
    UNSUBSCRIBED_STATE_INSTANT_INK_SUPPLY_INSTALL_NEW_INSTANT_INK_SUPPLY_66175 ="Unsubscribed_state_Instant_Ink_Supply/Install_New_Instant _ink_Supply_66175"
    MISINSTALLED_CARTRIDGE_66175="Misinstalled_Cartridge_66175"
    OOBE_FAULTY_SUPPLY_SHORTED_CONTACTPADS_66175_HPPLUS="OOBE_Faulty_Supply_Shorted_contactpads_66175_HPplus"
    SUBSCRIBED_STATE_PREVIOUSLY_USED_HP_INSTANT_INK_HPPLUSII_66175="Subscribed_state_Previously_Used_HP_Instant Ink_HPplusII_66175"
    INCOMPATIBLE_CARTRIDGE_REGION_66175="Incompatible_Cartridge_Region_66175"
    PRINTHEADPROBLEM_66211="PrintHeadProblem_66211"
    HP_PROTECTED_PRINTHEADS_INSTALLED_66230 = "HP_Protected_Printheads_Installed_66230"
    PRINTHEAD_REPLACEMENT_INCOMPLETE_66130 ="Printhead_Replacement_Incomplete_66130"
    PRINTHEAD_NOT_PRESENT_66128 = "Printhead_Not_Present_66128"
    PRINTHEAD_RESEAT_66131 = "Printhead_Reseat_66131"
    OUTOFINK_66537="OutOfInk_66537"
    CARTRIDGE_MISSING_65589 = "Cartridge_Missing_65589"
    CARTRIDGE_SAFE_STOP_65939="Cartridge_Safe_Stop_65939"
    PRINTHEAD_FAILURE_66442="Printhead_Failure_66442"
    IDSSTARTUP_BLOCKED_LOI_FLOW_66440="IdsStartup_Blocked_Loi_Flow_66440"
    OUTOFINK_66618="OutOfInk_66618" 
    # selene - error
    ANTITHEFT_ENABLED_SUPPLYERROR_66035="AntiTheft_Enabled_SupplyError_66035"
    CARTRIDGE_UNAUTHORIZED_65926="Cartridge_Unauthorized_65926"
    CARTRIDGE_VERYLOWSTOP_66039="Cartridge_VeryLowStop_66039"
    CARTRIDGE_MEMORYERROR_65542="Cartridge_MemoryError_65542"
    CARTRIDGE_MISSING_66034="Cartridge_Missing_66034"
    USED_SUPPLY_PROMPT_66043="Used_Supply_Prompt_66043"
    CARTRIDGE_WRONG_SLOT="Cartridge_Wrong_Slot"
    
    # Warnings
    CARTRIDGE_VERY_LOW_65546 = "Cartridge_VeryLow_65546"
    VLOI_SUPPLY_66710="VLOI_Supply_66710"
    PRINTER_SUPPLY_UPGRADE_AVAILABLE_65549="printer_supply_upgrade_available_65549"
    UPGRADABLESUPPLY_65549="upgradableSupply_65549"
    CARTRIDGE_USED_OR_COUNTERFEIT_QUESTION_65592 = "Cartridge_UsedOrCounterfeit_Flow_65592"
    UNSUBSCRIBED_STATE_INCOMPATIBLE_INK_66241 = "UnSubscribedState_InCompatible_Ink_66241"
    VLOI_SUPPLY_66712="VLOI_Supply_66712"
    HP_ALTERED_SUPPLY_COUNTERFEITFLOW_CONTINUE_CANCEL_66268 = "HP_Altered_Supply_CounterfeitFlow_Continue_Cancel_66268"
    HP_ALTERED_SUPPLY_COUNTERFEIT_66268 = "HP_Altered_Supply_Counterfeit_Continue_66268"
    HP_ALTERED_SUPPLY_FROM_COUNTERFEITINSTALLEDFLOW_YES_66269 = "HP_Altered_Supply_From_CounterfeitInstalledFlow_Yes_66269"
    HP_ALTERED_SUPPLY_CARTRIDGE_REFILLED_YES_66269 = "HP_Altered_Supply_cartridgeRefilled_Yes_66269"
    HP_ALTERED_SUPPLY_REFILLED_FLOW_NO_66443 = "HP_Altered_Supply_RefilledFlow_No_66443"
    HP_ALTERED_SUPPLY_CARTRIDGE_REFILLED_66443 = "HP_Altered_Supply_cartridgeRefilled_No_66443"
    HP_ALTERED_SUPPLY_COUNTERFEIT_QUESTION_66267 = "HP_Altered_Supply_CounterfeitQuestion_66267"
    CARTRIDGE_VERY_LOW_FLOW_66242="Cartridge_Very_Low_Flow_65546"
    CARTRIDGE_UPGRADABLE_FLOW_65549="Cartridge_Upgradable_Flow_65549"
    CARTRIDGE_USEDORCOUNTERFEIT_FLOW_65592="Cartridge_UsedOrCounterfeit_Flow_65592"
    CARTRIDGE_USEDORCOUNTERFEIT_FLOW_CONTINUE_CANCEL_65592_65617="Cartridge_UsedOrCounterfeit_Flow_Continue_Cancel_65592_65617"
    CARTRIDGE_USEDORCOUNTERFEIT_QUESTION_65592="Cartridge_UsedOrCounterfeit_Question_65592"
    CARTRIDGE_USEDORCOUNTERFEIT_QUESTION_CONTINUE_65592_65594="Cartridge_UsedOrCounterfeit_Question_Continue_65592_65594"
    CARTRIDGE_USEDORCOUNTERFEIT_QUESTION_YES_65592_65617="Cartridge_UsedOrCounterfeit_Question_Yes_65592_65617"
    CARTRIDGE_USEDORCOUNTERFEIT_QUESTION_NO_65592_66098="Cartridge_UsedOrCounterfeit_Question_No_65592_66098"
    CARTRIDGE_VERY_LOW_66018="Cartridge_VeryLow_66018"
    VLOI_SUPPLY_66241="VLOI_Supply_66241"
    HP_ALTERED_SUPPLY_ANTICOUNTERFEITFLOW_66267="HP_Altered_Supply_AntiCounterfeitFlow_66267"
    CARTRIDGE_VERY_LOW_FLOW_65546="Cartridge_Very_Low_Flow_65546"
    PRINTHEAD_USEDWITH_NONHPINK_66413="Printhead_UsedWith_NonHPInk_66413"
    CARTRIDGE_VERY_LOW_66515="Cartridge_Very_Low_66515"
    CARTRIDGE_ALTERED_66562="Cartridge_Altered_66562"
    CALIBRATION_REQUIRED_66495="Calibration_Required_66495"
    TANK_VERY_LOW_66018="Tank_Very_Low_66018"

    # selene - warning
    CARTRIDGE_VERYLOW_CONTINUE_66085="Cartridge_VeryLow_Continue_66085"

    #INFORMATION
    SINGLE_INK_CARTRIDGE_MODE_65553 = "SingleInkCartridgeMode_65553"
    USED_HP_CARTRIDGE_65554 = "UsedHPCartridge_65554"
    SUPPLIES_LOW_65557 ="Supplies_Low_65557"
    SUPPLIES_LOW_PRINTING_65557 = "Supplies_Low_Printing_65557"
    CARTRIDGE_LOW_66711="cartridges_low_66711"
    LOI_SUPPLY_66711 ="LOI_Supply_66711"
    CARTRIDGE_EXPECTED_SETUP_65561 = "CartridgeExpectedSetup_65561"
    CARTRIDGE_LOW_66242="CartridgeLow_66242"
    SINGLE_CARTRIDGE_MODE_66263="SingleInkCartridgeMode_66263"
    USED_SUPPLY_PROMPT_66264="Used_Supply_Prompt_66264"
    GENUINE_HP_SUPPLY_66265="Genuine_HP_supply_66265"
    LOI_SUPPLY_66713="LOI_Supply_66713"
    CARTRIDGE_LOW_66017="Cartridge_Low_66017"
    FULLTANK_66020="FullTank_66020"
    USED_PRINTHEAD_INSTALLATION_66216="Used_Printhead_Installation_66216"
    NEW_PRINTHEAD_INSTALLATION_66222="New_Printhead_Installation_66222"
    USED_SUPPLY_FLOW_66264="Used_Supply_Flow_66264"
    GENUINE_HP_SUPPLY_FLOW_66265="Genuine_HP_Supply_Flow_66265"
    CARTRIDGE_LOW_FLOW_65557="Cartridge_Low_Flow_65557"
    IDS_DELAYED_BACKTO_HP_66516="Ids_Delayed_BackTo_Hp_66516"
    TANK_LOW_66017="Tank_Low_66017"
    TANK_FILLED_66020="Tank_Filled_66020"
    TANK_FULL_66437="Tank_Full_66437"
    PH_REPLACEMENT_FLOW_66640="PhReplacement_Flow_66640"

    # selene - information
    GENUINEHP_SUPPLYFLOW_66101="GenuineHP_SupplyFlow_66101"
    CARTRIDGE_LOW_65669="Cartridge_Low_65669"
    NON_HP_SUPPLY_FLOW_66092="Non_HP_Supply_Flow_66092"

class SimulatorErrorManagerCDM:
    """Manages error simulation through CDM API calls"""
    def __init__(self, printer_ip: str, serial_number: str = None):
        """
        Initialize the error manager
        """
        self.printer_ip = printer_ip
        self.serial_number = serial_number or "SIMR7XMRH0"
        self.base_url = f"http://{printer_ip}/cdm"

    def set_error_state(self, error_type: AlertTypeCDM, color=None) -> bool:
        """
        Set an error state via CDM API call
        """
        try:
            api_endpoint = f"{self.base_url}/setstatus"
            params = {
                "category": error_type.value,
                "serialNumber": self.serial_number
            }
            if color is not None:
                params["parameter"] = color
            logging.info(f"CDM API URL: {api_endpoint}?{self._format_params(params)}")
           
            response = requests.post(api_endpoint, params=params, timeout=30)
            response.raise_for_status()
           
            return True
           
        except Exception as e:
            logging.error(f"Failed to set error state {error_type.value}: {str(e)}")
            return False

    def _format_params(self, params: Dict[str, str]) -> str:
        """Format parameters for logging"""
        return "&".join([f"{key}={value}" for key, value in params.items()])
