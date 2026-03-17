
"""
OneSimulator Error Simulator Module
Provides structured error simulation capabilities for printer testing
"""
import logging
import requests
from enum import Enum
from typing import Dict
 
class AlertTypeLEDM(Enum):
    """Enumeration of supported error types with LEDM message IDs"""
    #Errors
    CARTRIDGES_MISSING_65537 ="Missing_All_Cartridge_65537"
    CARTRIDGE_MISSING_SINGLE_65537 = "Missing_single_Cartridge_65537"
    CARTRIDGE_MISSING_65589 = "Missing_Cartridge_65589"
    CARTRIDGE_FAILURE_65542 = "Cartridge_Failure_65542"
    CARTRIDGE_FAILURE_65542_ERRORCODE_170200 = "Cartridge_Failure_65542_errorcode_170200"
    INCOMPATIBLE_INK_CARTRIDGE_65543 = "Incompatible_Ink_Cartridge_65543"
    TRADE_CARTRIDGE_WHEN_EXPECT_HOST_65590 = "Trade_Cartridge_When_Expect_Host_65590"
    TRADE_CARTRIDGE_WHEN_EXPECT_HOST_IMCOMPATIBLE_EXPECT = "Trade_Cartridge_When_Expect_Host_Imcompatible_expect_setup_65590"
    LOW_ON_INK_65590 = "Low_on_ink_65590"
    TRADE_CARTRIDGE_WHEN_EXPECT_HOST_INSTANT_INK_SUBSCRIPTION_65590 = "Trade_Cartridge_When_Expect_Host_Instant_ink_subscrition_65590"
    HP_ALTERED_SUPPLY_INSTANT_INK_SUBS_65590 = "HP_Altered_supply_Instant_Ink_subs_65590"
    HP_ALTERED_SUPPLY_65590_65592 = "HP_Altered_supply_65590_65592"
    HOST_CARTRIDGE_WHEN_EXPECT_TRADE_65591 = "Host_Cartridge_When_Expect_Trade_65591"
    ANTITHEFT_ENABLED_SUPPLY_DETECTED_65612 = "AntiTheft_Enabled_SupplyDetected_65612"
    CARTRIDGEFAILURE_INSTANT_INK_SUBS_65675 = "cartridgeFailure_Instant_Ink_subs_65675"
    CARTRIDGEFAILURE_65675 = "cartridgeFailure_65675"
    USE_OTHER_FAMILY_INCOMPATIBLE_65676 = "Use_other_family_Incompatible_Cartridges_65676"
    INCOMPATIBLE_CARTRIDGES_65676 = "Incompatible_Cartridges_65676"
    REGIONAL_CARTRIDGES_65676 = "Regional_Cartridges_65676"
    CARTRIDGEMISSING_65690 = "cartridgeMissing_65690"
    ANTITHEFT_ENABLED_SUPPLYDETECTED_65694 = "AntiTheft_Enabled_SupplyDetected_65694"
    TRADE_PROTECTED_CARTRIDGES_INSTANT_INK_SUB_65694 = "Trade_protected_cartridges_Instant_Ink_sub_65694"
    SUBSCRIPTIONCONSUMABLE_NEEDS_ENROLLMENT_65765 = "SubscriptionConsumable_Needs_Enrollment_65765"
    UNSUBSCRIBED_STATE_INSTALL_NEW_INSTANT_INK_SUPPLY_65765 = "Unsubscribed_state_Install_New_Instant_Ink_Supply_65765"
    MISSING_CARTRIDGE_HYBRIDINKSUB_65769 = "Missing_Cartridge_HybridInksub_65769"
    MISSING_CARTRIDGE_INSTANTINKSUB_65769 = "Missing_Cartridge_InstantInksub_65769"
    ANTITHEFT_ENABLED_SUPPLY_DETECTED_65773="AntiTheft_Enabled_SupplyDetected_65773"
    CARTRIDGEIN_WRONGSLOT_65544 = "CartridgeIn_WrongSlot_65544"
    INSERTNONSETUPCARRIDGE_65688="insertNonSETUPCartridge_65688"
    INSTANTINK_XMOS2_REJECTCARTRIDGE_65846="InstantInk_XMOS2_Rejectcartridge_65846"
    ALIGNMENT_ERROR_66564 = "alignment_error_66564"
    NON_HP_CIRCUITRY_66341 = "Non_HP_Circuitry_66341"
    NON_HP_CHIP_66339 = "Non_hp_chip_66339"
    HP_INSTANT_INK_66315 = "hp_instant_ink_66315"
    HP_PROTECTED_CARTRIDGES_INSTALLED_66305 = "hp_protected_cartridges_installed_66305"
    HP_PROTECTED_CARTRIDGES_INSTALLED_66304 = "hp_protected_cartridges_installed_66304"
    DO_NOT_USE_SETUP_CARTRIDGES_66300 = "do_not_use_setup_cartridges_66300"
    DO_NOT_USE_SETUP_CARTRIDGES_66299 = "do_not_use_setup_cartridges_66299"
    DO_NOT_USE_SETUP_CARTRIDGES_66298 = "do_not_use_setup_cartridges_66298"
    USE_SETUP_CARTRIDGES_66297 = "use_setup_cartridges_66297"
    CARTRIDGES_REJECTED_66293 = "cartridges_rejected_66293"
    CARTRIDGES_IN_WRONG_SLOT_66286 = "cartridges_in_wrong_slot_66286"
    INCOMPATIBLE_CARTRIDGES_66285 = "incompatible_cartridges_66285"
    INCOMPATIBLE_CARTRIDGES_66284 = "incompatible_cartridges_66284"
    INCOMPATIBLE_CARTRIDGES_66283 = "incompatible_cartridges_66283"
    CARTRIDGE_PROBLEM_66279 = "cartridge_problem_66279"
    CARTRIDGE_PROBLEM_66278 = "cartridge_problem_66278"
    CARTRIDGE_PROBLEM_66277 = "cartridge_problem_66277"
    CARTRIDGES_MISSING_66262 = "cartridge_Missing_66262"
    OOBE_HP_ALTERED_SUPPLY_REFILLED_66175 = "OOBE_HP_Altered_Supply_refilled_66175"
    OOBE_FAULTY_SUPPLY_66175 = "OOBE_faulty_supply_66175"
    TRIAL_PEN_66175 = "trial_pen_66175"
    INCOMPATIBLE_PEN_66175 = "incompatible_pen_66175"
    NON_HP_CIRCUITRY_66175 = "Non_HP_circuitry_66175"
    PROTECTED_CARTRIDGES_66175 = "Protected_cartridges_66175"
    CALIBRATING_65571 = "calibrating_65571"
    FILL_TANKS_66019 = "Fill_Tanks_66019"
    FAILED_PRINTHEAD_65536 = "Failed_PrintHead_65536"
    MISSING_PRINTHEAD_65536 = "MissingPrintHead_65536"
    INCOMPATIBLE_PRINTHEAD_65536 = "Incompatible_PrintHead_65536"
    INK_CARTRIDGE_EMPTY_65539 = "InkCartridge_Empty_65539"
    SHAID_OOI_Too_EARLY_65541 = "SHAID_OOI_Too_early_65541"
    SHAID_OOI_Too_EARLY_65800 = "SHAID_OOI_Too_early_65800"
    PRINTER_ERROR_65541 = "Printer_Error_65541"
    MEDIA_TOO_SHORT_TO_AUTO_DUPLEX_65572 = "MediaTooShortToAutoDuplex_65572"
    STARTUP_FAILURE_65599 = "Startup_Failure_65599"
    CLOSE_DOOR_COVER_65725 = "closeDoor_cover_65725"
    PRINTHEAD_CARTRIDGE_MISSING_66207 = "PrintHead_Cartridge_Missing_66207"
    PRINTHEAD_FAILURE_66211 = "PrintHead_Failure_66211"
    INCOMPATIBLE_PRINTHEAD_66213 = "Incompatible_PrintHead_66213"
    PROTECTED_PRINTHEAD_66230 = "Protected_PrintHead_66230"
    SHARED_SELECT_ADDRESS_ERROR_66209 = "SharedSelectAddressError_66209"
    FILL_TANKS_66333 = "Fill_Tanks_66333"

    # skyreach - error
    DEFECTIVE_MEMORY_66038 = "Defective_Memory_66038"
    CARTRIDGE_OUT= "Cartridge_Out"
    ANTI_THEFT_ENABLED_SUPPLY_DETECTED = "AntiTheft_Enabled_SupplyDetected"
    INCOMPATIBLE_CARTRIDGE = "Incompatible_Cartridge"
    UNAUTHORIZED_CARTRIDGE = "Unauthorized_Cartridge"
    CARTRIDGE_MISSING = "Cartridge_Missing"
    ALL_CARTRIDGE_MISSING="all_cartridge_missing"
    USED_COUNTERFEIT_CARTRIDGE = "Used_Counterfeit_Cartridge"
    COUNTERFEIT_CARTRIDGES_INSTALLED_66043 = "Counterfeit_Cartridges_Installed_66043"

    # Warnings
    CARTRIDGE_VERY_LOW_65546 = "Cartridge_VeryLow_65546"
    CARTRIDGE_COUNTERFEIT_QUESTION_65592 = "Cartridge_Counterfeit_Question_65592"
    CARTRIDGE_REFILLED_65594 = "Cartridge_Refilled_65594"
    CARTRIDGE_COUNTERFEIT_65617 = "Cartridge_Counterfeit_65617"
    CARTRIDGE_COUNTERFEIT_QUESTION_YES_INSTANT_INK_SUB_65617 = "Cartridge_Counterfeit_Question_Yes_Instant_ink_sub_65617"
    CARTRIDGE_COUNTERFEIT_QUESTION_INSTANT_INK_SUB_65685 = "Cartridge_Counterfeit_Question_Instant_ink_sub_65685"
    CARTRIDGE_COUNTERFEIT_65686 = "Cartridge_Counterfeit_65686"
    CARTRIDGE_COUNTERFEIT_INKSUB_65686 = "Cartridge_Counterfeit_InkSub_65686"
    CARTRIDGE_COUNTERFEIT_QUESTION_YES_INSTANT_INK_SUB_65686 = "Cartridge_Counterfeit_Question_Yes_Instant_ink_sub_65686"
    CARTRIDGE_REFILLED_65687 = "Cartridge_Refilled_65687"
    CARTRIDGE_COUNTERFEIT_QUESTION_YES_CONT_INSTANT_INK_SUB_65687 = "Cartridge_Counterfeit_Question_Yes_cont_Instant_ink_sub_65687"
    CARTRIDGE_VERY_LOW_65764 = "cartridgeVeryLow_65764"
    CARTRIDGE_VERY_LOW1_65764 = "Cartridge_very_low_65764"
    CARTRIDGE_VERY_LOW_INKSUB_65776 = "Cartridge_VeryLow_Inksub_65776"
    CARTRIDGE_VERY_LOW_66241 = "Cartridge_VeryLow_66241"
    UPGRADABLE_SUPPLY_65549 = "upgradableSupply_65549"
    UPGRADABLE_SUPPLY_65677 = "upgradableSupply_65677"
    SUBSCRIPTION_CONSUMABLE_TEMPORARY_USAGE_ALLOWED_65772 = "SubscriptionConsumable_TemporaryUsage_Allowed_65772"
    USED_OR_COUNTERFEIT_CARTRIDGES_DETECTED_66267 = "used_or_counterfeit_cartridges_detected_66267"
    CARTRIDGE_COUNTERFEIT_QUESTION_NO_INSTANT_INK_SUB_66099 = "Cartridge_Counterfeit_Question_No_Instant_ink_sub_66099"
    CARTRIDGE_REFILLED_66099 = "Cartridge_Refilled_66099"
    CARTRIDGE_COUNTERFEIT_QUESTION_NO_INSTANT_INK_SUB_66098 = "Cartridge_Counterfeit_Question_No_Instant_ink_sub_66098"
    CARTRIDGE_REFILLED_66098 = "Cartridge_Refilled_66098"
    CALIBRATION_REQUIRED_65569 = "calibration_required_65569"
    INSTANTINK_XMOS2_TRAILCARTRIDGE_VLOI_65848 = "InstantInk_XMOS2_TrialCartridge_VLOI_65848"
    TANKS_VERY_LOW_66018 = "Tanks_Very_Low_66018"
    SEHOATINSERTION_65613="sehoAtInsertion_65613"
    CARTRIDGE_VERYLOW_65672="Cartridge_VeryLow_65672"
    SUBSCRIPTIONCONSUMABLE_TEMPORARYUSAGE_ALLOWED_65934="SubscriptionConsumable_TemporaryUsage_Allowed_65934"
    TANKS_VERY_LOW_66332 = "Tanks_Very_Low_66332"

    # skyreach - warning
    CARTRIDGE_VERYLOW = "Cartridge_VeryLow"

    #INFORMATION
    SINGLE_CARTRIDGE_MODE_65553 = "SingleCartridgeMode_65553"
    USED_CONSUMABLE_65554 = "Used_Consumable_65554"
    SUPPLIES_LOW_65557 ="Supplies_Low_65557"
    SUPPLIES_LOW_PRINTING_65557 = "Supplies_Low_Printing_65557"
    GENUINE_HP_65561="Genuine_HP_65561"
    READY="ready"
    PREVIOUSLY_USED_CONSUMABLE_INSTANT_INK_SUB_65680 = "Previously_used_Consumable_Instant_Ink_Sub_65680"
    USEDCONSUMABLE_INKSUB_65680="usedConsumable_InkSub_65680"
    SUPPLIES_LOW_PRINTING_65681="Supplies_Low_Printing_65681"
    SUPPLIES_LOW_65681="Supplies_Low_65681"
    LOW_ON_INK_65590_65681 = "Low_on_ink_65590_65681"
    SUPPLIES_LOW_PRINTING_INSTANT_INK_SUBS_65681 = "Supplies_Low_Printing_Instant_ink_subs_65681"
    INSTANTINK_XMO2_GENUINECARTRIDGE_65766="InstantInk_XMO2_GenuineCartridge_65766"
    SINGLECARTRIDGE_MODE_HYBRIDINKSUB_65771="singleCartridgeMode_HybridInksub_65771"
    INSTANTINK_TRADECARTRIDGE_INSTALLED_65796="InstantInk_TradeCartridge_Installed_65796"
    INSTANTINK_SUBSCRIPTION_SUCCESSFUL_65767 = "InstantInk_subscription_Successful_65767"
    GENUINE_HP_66265 = "genuine_HP_66265"
    USED_CONSUMABLE_66264 = "used_Consumable_66264"
    SINGLE_CARTRIDGE_MODE_66263 = "single_cartridge_mode_66263"
    CARTRIDGE_LOW_66242 = "cartridge_Low_66242"
    GENUINE_HP_INKLEVELZERO_65684 = "Genuine_HP_inklevelZero_65684"
    TANK_LOW_66017 = "Tank_Low_66017"
    TANKS_FILLED_66020 = "Tanks_Filled_66020"
    NONHP_SUPPLY_DETECTED_PRINTING_65559 = "NonHP_Supply_Detected_Printing_65559"
    SUPPLIES_LOW_65669 = "Supplies_Low_65669"
    SUPPLIES_LOW_PRINTING_65669 = "Supplies_Low_Printing_65669"
    GENUINE_CARTRIDGES_INSTALLED_65862 = "Genuine_Cartridges_Installed_65862"
    NONHP_SUPPLY_DETECTED_PRINTING_66092 = "NonHP_Supply_Detected_Printing_66092"
    GENUINE_HP_65851 = "genuineHP_65851"
    SETUP_CARTRIDGE_FOR_PHA_65591_65851 = "setup_cartridge_for_PHA_65591_65851"
    USED_CONSUMABLE_66216 = "used_Consumable_66216"
    GENUINE_INK_CARTRIDGES_INSTALLED_66222 = "Genuine_Ink_Cartridges_Installed_66222"

    # skyreach - information
    CARTRIDGE_LOW = "Cartridge_Low"
    NON_HP_SUPPLY_FLOW_66092 = "Non_HP_Supply_Flow_66092"
    UNAUTHORIZED_SUPPLY_65926 = "Unauthorized_Supply_65926"

class SimulatorErrorManagerLEDM:
    """
    Manages error simulation through LEDM API calls
    """

    def __init__(self, printer_ip: str, serial_number: str = None):
        """
        Initialize the error manager
        """
        self.printer_ip = printer_ip
        self.serial_number = serial_number or "SIMR7XMRH0"
        self.base_url = f"http://{printer_ip}/ledm"

    def set_error_state(self, error_type: AlertTypeLEDM, color=None) -> bool:
        """
        Set an error state via LEDM API call
        """
        try:
            api_endpoint = f"{self.base_url}/setstatus"
            params = {
                "messageID": error_type.value,
                "serialNumber": self.serial_number
            }
            if color is not None:
                params["parameters"] = color
            logging.info(f"LEDM API URL: {api_endpoint}?{self._format_params(params)}")
           
            response = requests.post(api_endpoint, params=params, timeout=30)
            response.raise_for_status()
           
            return True
           
        except Exception as e:
            logging.error(f"Failed to set error state {error_type.value}: {str(e)}")
            return False

    def _format_params(self, params: Dict[str, str]) -> str:
        """Format parameters for logging"""
        return "&".join([f"{key}={value}" for key, value in params.items()])
