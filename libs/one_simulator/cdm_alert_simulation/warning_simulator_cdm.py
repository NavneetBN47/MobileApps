
from MobileApps.libs.one_simulator.cdm_alert_simulation.alert_type_cdm import SimulatorErrorManagerCDM, AlertTypeCDM


class WarningSimulatorCDM(SimulatorErrorManagerCDM):
    def cartridges_very_low_65546(self, color):
        """
        Simulate a very low cartridge condition
        """
        return self.set_error_state(AlertTypeCDM.CARTRIDGE_VERY_LOW_65546, color=color)

    def vloi_supply_66710(self, color):
        """
        Simulate a VLOI supply condition
        """
        return self.set_error_state(AlertTypeCDM.VLOI_SUPPLY_66710, color=color)    

    def printer_supply_upgrade_available_65549(self, color):
        """
        Simulate a printer supply upgrade available condition
        """
        return self.set_error_state(AlertTypeCDM.PRINTER_SUPPLY_UPGRADE_AVAILABLE_65549, color=color)

    def upgradable_supply_65549(self, color):
        """
        Simulate an upgradable supply condition
        """
        return self.set_error_state(AlertTypeCDM.UPGRADABLE_SUPPLY_65549, color=color)

    def cartridge_use_or_counterfeit_question_65592(self, color):
        """
        Simulate a cartridge use or counterfeit question condition
        """
        return self.set_error_state(AlertTypeCDM.CARTRIDGE_USED_OR_COUNTERFEIT_QUESTION_65592, color=color)

    def cartridge_very_low_66241(self, color):
        """
        Simulate a very low cartridge condition
        """
        return self.set_error_state(AlertTypeCDM.UNSUBSCRIBED_STATE_INCOMPATIBLE_INK_66241, color=color)

    def vloi_supply_66712(self, color):
        """
        Simulate a VLOI supply condition
        """
        return self.set_error_state(AlertTypeCDM.VLOI_SUPPLY_66712, color=color)

    def hp_altered_supply_counterfeit_66268(self, color):
        """
        Simulate a counterfeit or used cartridges identified condition
        """
        return self.set_error_state(AlertTypeCDM.HP_ALTERED_SUPPLY_COUNTERFEIT_66268, color=color)

    def counterfeit_or_used_cartridges_installed_66269(self, color):
        """
        Simulate a counterfeit or used cartridges installed condition
        """
        return self.set_error_state(AlertTypeCDM.HP_ALTERED_SUPPLY_CARTRIDGE_REFILLED_YES_66269, color=color)

    def hp_altered_supply_refilled_flow_no_66443(self, color):
        """
        Simulate a used or refilled cartridges installed condition
        """
        return self.set_error_state(AlertTypeCDM.HP_ALTERED_SUPPLY_REFILLED_FLOW_NO_66443, color=color)

    def hp_altered_supply_counterfeit_66267(self, color):
        """
        Simulate a used or counterfeit cartridges detected condition
        """
        return self.set_error_state(AlertTypeCDM.HP_ALTERED_SUPPLY_COUNTERFEIT_QUESTION_66267, color=color)

    def used_or_counterfeit_cartridges_installed_66268(self, color):
        """
        Simulate a used or counterfeit cartridges installed condition
        """
        return self.set_error_state(AlertTypeCDM.USED_OR_COUNTERFEIT_CARTRIDGES_INSTALLED_66268, color=color)

    def cartridge_very_low_flow_65546(self, color):
        """
        Simulate a very low cartridge condition
        """
        return self.set_error_state(AlertTypeCDM.CARTRIDGE_VERY_LOW_FLOW_65546, color=color)

    def cartridge_upgradable_flow_65549(self, color):
        """
        Simulate a cartridge upgradable condition
        """
        return self.set_error_state(AlertTypeCDM.CARTRIDGE_UPGRADABLE_FLOW_65549, color=color)

    def cartridge_used_or_counterfeit_flow_65592(self, color):
        """
        Simulate a cartridge used or counterfeit condition
        """
        return self.set_error_state(AlertTypeCDM.CARTRIDGE_USEDORCOUNTERFEIT_FLOW_65592, color=color)

    def cartridge_usedorcounterfeit_flow_continue_cancel_65592_65617(self, color):
        """
        Simulate a cartridge used or counterfeit flow continue/cancel condition
        """
        return self.set_error_state(AlertTypeCDM.CARTRIDGE_USEDORCOUNTERFEIT_FLOW_CONTINUE_CANCEL_65592_65617, color=color)

    def cartridge_usedorcounterfeit_question_65592(self, color):
        """
        Simulate a cartridge used or counterfeit question condition
        """
        return self.set_error_state(AlertTypeCDM.CARTRIDGE_USEDORCOUNTERFEIT_QUESTION_65592, color=color)

    def cartridge_usedorcounterfeit_question_continue_65592_65594(self, color):  
        """
        Simulate a cartridge used or counterfeit question continue condition
        """
        return self.set_error_state(AlertTypeCDM.CARTRIDGE_USEDORCOUNTERFEIT_QUESTION_CONTINUE_65592_65594, color=color)

    def cartridge_usedorcounterfeit_question_yes_65592_65617(self, color):
        """
        Simulate a cartridge used or counterfeit question yes condition
        """
        return self.set_error_state(AlertTypeCDM.CARTRIDGE_USEDORCOUNTERFEIT_QUESTION_YES_65592_65617, color=color)

    def cartridge_usedorCounterfeit_question_No_65592_66098(self, color):
        """
        Simulate a cartridge used or counterfeit question no condition
        """
        return self.set_error_state(AlertTypeCDM.CARTRIDGE_USEDORCOUNTERFEIT_QUESTION_NO_65592_66098, color=color)

    def cartridge_very_low_66018(self, color):
        """
        Simulate a cartridge very low condition
        """
        return self.set_error_state(AlertTypeCDM.CARTRIDGE_VERY_LOW_66018, color=color)

    def unsubscribedstate_incompatible_ink_66241(self, color):
        """
        Simulate an unsubscribed state incompatible ink condition
        """
        return self.set_error_state(AlertTypeCDM.UNSUBSCRIBED_STATE_INCOMPATIBLE_INK_66241, color=color)

    def vloi_supply_66241(self, color):
        """
        Simulate a VLOI supply condition
        """
        return self.set_error_state(AlertTypeCDM.VLOI_SUPPLY_66241, color=color)

    def hp_altered_supply_anticounterfeitflow_66267(self, color):
        """
        Simulate a HP altered supply anti-counterfeit flow condition
        """
        return self.set_error_state(AlertTypeCDM.HP_ALTERED_SUPPLY_ANTICOUNTERFEITFLOW_66267, color=color)

    def hp_altered_supply_counterfeitflow_continue_cancel_66268(self, color):
        """
        Simulate a HP altered supply counterfeit flow continue/cancel condition
        """
        return self.set_error_state(AlertTypeCDM.HP_ALTERED_SUPPLY_COUNTERFEITFLOW_CONTINUE_CANCEL_66268, color=color)

    def hp_altered_supply_from_counterfeitinstalledflow_Yes_66269(self, color):
        """
        Simulate a HP altered supply from counterfeit installed flow yes condition
        """
        return self.set_error_state(AlertTypeCDM.HP_ALTERED_SUPPLY_FROM_COUNTERFEITINSTALLEDFLOW_YES_66269, color=color)

    def hp_altered_supply_cartridgerefilled_yes_66269(self, color):
        """
        Simulate a HP altered supply cartridge refilled yes condition
        """
        return self.set_error_state(AlertTypeCDM.HP_ALTERED_SUPPLY_CARTRIDGE_REFILLED_YES_66269, color=color)

    def vloi_supply_66710(self, color):
        """
        Simulate a VLOI supply condition
        """
        return self.set_error_state(AlertTypeCDM.VLOI_SUPPLY_66710, color=color)

    def vloi_supply_66712(self, color):
        """
        Simulate a VLOI supply condition
        """
        return self.set_error_state(AlertTypeCDM.VLOI_SUPPLY_66712, color=color)

    def cartridge_verylow_continue_66085(self, color):
        """
        Simulate a Cartridge VeryLow Continue 66085 error condition
        """
        return self.set_error_state(AlertTypeCDM.CARTRIDGE_VERYLOW_CONTINUE_66085, color=color)

    def printhead_used_with_non_hp_ink(self, color):
        """
        Simulate a printhead used with non-HP ink condition
        """
        return self.set_error_state(AlertTypeCDM.PRINTHEAD_USEDWITH_NONHPINK_66413, color=color)

    def cartridge_very_low_66515(self, color):
        """
        Simulate a cartridge very low condition
        """
        return self.set_error_state(AlertTypeCDM.CARTRIDGE_VERY_LOW_66515, color=color)

    def cartridge_altered_66562(self, color):
        """
        Simulate a cartridge altered condition
        """
        return self.set_error_state(AlertTypeCDM.CARTRIDGE_ALTERED_66562, color=color)

    def calibration_required_66495(self, color):
        """
        Simulate an alignment triggered after replacement condition
        """
        return self.set_error_state(AlertTypeCDM.CALIBRATION_REQUIRED_66495, color=color)

    def tank_very_low_66018(self, color):
        """
        Simulate a tank very low condition
        """
        return self.set_error_state(AlertTypeCDM.TANK_VERY_LOW_66018, color=color)