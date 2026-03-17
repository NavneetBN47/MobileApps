from MobileApps.libs.one_simulator.ledm_alert_simulation.alert_type_ledm import AlertTypeLEDM, SimulatorErrorManagerLEDM


class WarningSimulatorLEDM(SimulatorErrorManagerLEDM):
    def cartridge_very_low_65546(self, color):
        """
        Simulate a very low cartridge condition
        """
        return self.set_error_state(AlertTypeLEDM.CARTRIDGE_VERY_LOW_65546, color=color)

    def cartridge_counterfeit_question_65592(self, color):
        """
        Simulate a counterfeit cartridge question condition
        """
        return self.set_error_state(AlertTypeLEDM.CARTRIDGE_COUNTERFEIT_QUESTION_65592, color=color)

    def cartridge_refilled_65594(self, color):
        """
        Simulate a refilled cartridge condition
        """
        return self.set_error_state(AlertTypeLEDM.CARTRIDGE_REFILLED_65594, color=color)

    def cartridge_counterfeit_65617(self, color):
        """
        Simulate a counterfeit cartridge condition
        """
        return self.set_error_state(AlertTypeLEDM.CARTRIDGE_COUNTERFEIT_65617, color=color)

    def cartridge_counterfeit_question_yes_instant_ink_sub_65617(self, color):
        """
        Simulate a counterfeit cartridge question condition
        """
        return self.set_error_state(AlertTypeLEDM.CARTRIDGE_COUNTERFEIT_QUESTION_YES_INSTANT_INK_SUB_65617, color=color)

    def cartridge_counterfeit_65686(self, color):
        """
        Simulate a counterfeit cartridge condition
        """
        return self.set_error_state(AlertTypeLEDM.CARTRIDGE_COUNTERFEIT_65686, color=color)

    def cartridge_counterfeit_question_yes_instant_ink_sub_65686(self, color):
        """
        Simulate a counterfeit cartridge question condition
        """
        return self.set_error_state(AlertTypeLEDM.CARTRIDGE_COUNTERFEIT_QUESTION_YES_INSTANT_INK_SUB_65686, color=color)

    def cartridge_counterfeit_inksub_65686(self, color):
        """
        Simulate a counterfeit ink sub cartridge condition
        """
        return self.set_error_state(AlertTypeLEDM.CARTRIDGE_COUNTERFEIT_INKSUB_65686, color=color)

    def cartridge_refilled_65687(self, color):
        """
        Simulate a refilled ink sub cartridge condition
        """
        return self.set_error_state(AlertTypeLEDM.CARTRIDGE_REFILLED_65687, color=color)

    def cartridge_counterfeit_question_yes_cont_instant_ink_sub_65687(self, color):
        """
        Simulate a counterfeit cartridge question condition
        """
        return self.set_error_state(AlertTypeLEDM.CARTRIDGE_COUNTERFEIT_QUESTION_YES_CONT_INSTANT_INK_SUB_65687, color=color)

    def cartridge_very_low_65764(self, color):
        """
        Simulate a very low cartridge condition
        """
        return self.set_error_state(AlertTypeLEDM.CARTRIDGE_VERY_LOW_65764, color=color)

    def cartridge_very_low1_65764(self, color):
        """
        Simulate a very low cartridge condition
        """
        return self.set_error_state(AlertTypeLEDM.CARTRIDGE_VERY_LOW1_65764, color=color)

    def cartridge_very_low_66241(self, color):
        """
        Simulate a very low cartridge condition
        """
        return self.set_error_state(AlertTypeLEDM.CARTRIDGE_VERY_LOW_66241, color=color)

    def cartridge_very_low_inksup_65776(self, color):
        """
        Simulate a very low ink sub cartridge condition
        """
        return self.set_error_state(AlertTypeLEDM.CARTRIDGE_VERY_LOW_INKSUB_65776, color=color)

    def cartridge_counterfeit_question_65685(self, color):
        """
        Simulate a counterfeit cartridge question condition
        """
        return self.set_error_state(AlertTypeLEDM.CARTRIDGE_COUNTERFEIT_QUESTION_INSTANT_INK_SUB_65685, color=color)

    def upgradable_supply_65549(self, color):
        """
        Simulate an upgradable supply condition
        """
        return self.set_error_state(AlertTypeLEDM.UPGRADABLE_SUPPLY_65549, color=color)

    def upgradable_supply_65677(self, color):
        """
        Simulate an upgradable supply condition
        """
        return self.set_error_state(AlertTypeLEDM.UPGRADABLE_SUPPLY_65677, color=color)

    def subscription_consumable_temporary_usage_allowed_65772(self, color):
        """
        Simulate a subscription consumable temporary usage allowed condition
        """
        return self.set_error_state(AlertTypeLEDM.SUBSCRIPTION_CONSUMABLE_TEMPORARY_USAGE_ALLOWED_65772, color=color)

    def used_or_counterfeit_cartridges_detected_66267(self, color):
        """
        Simulate a used or counterfeit cartridges detected condition
        """
        return self.set_error_state(AlertTypeLEDM.USED_OR_COUNTERFEIT_CARTRIDGES_DETECTED_66267, color=color)

    def cartridge_counterfeit_question_no_instant_ink_sub_66099(self, color):
        """
        Simulate a used or refilled cartridges installed condition
        """
        return self.set_error_state(AlertTypeLEDM.CARTRIDGE_COUNTERFEIT_QUESTION_NO_INSTANT_INK_SUB_66099, color=color)

    def cartridge_refilled_66099(self, color):
        """
        Simulate a cartridge refilled condition
        """
        return self.set_error_state(AlertTypeLEDM.CARTRIDGE_REFILLED_66099, color=color)

    def cartridge_counterfeit_question_no_instant_ink_sub_66098(self, color):
        """
        Simulate a cartridge counterfeit question no instant ink sub condition
        """
        return self.set_error_state(AlertTypeLEDM.CARTRIDGE_COUNTERFEIT_QUESTION_NO_INSTANT_INK_SUB_66098, color=color)

    def used_or_refilled_cartridges_installed_66098(self, color):
        """
        Simulate a used or refilled cartridges installed condition
        """
        return self.set_error_state(AlertTypeLEDM.CARTRIDGE_REFILLED_66098, color=color)

    def used_or_refilled_cartridges_installed_66099(self, color):
        """
        Simulate a used or refilled cartridges installed condition
        """
        return self.set_error_state(AlertTypeLEDM.USED_OR_REFILLED_CARTRIDGES_INSTALLED_66099, color=color)

    def calibration_required_65569(self, color):
        """
        Simulate a calibration required condition
        """
        return self.set_error_state(AlertTypeLEDM.CALIBRATION_REQUIRED_65569, color=color)

    def instantink_xmos2_trialcartridge_vloi_65848(self, color):
        """
        Simulate an InstantInk XMOS2 Trial Cartridge VLOI condition
        """
        return self.set_error_state(AlertTypeLEDM.INSTANTINK_XMOS2_TRAILCARTRIDGE_VLOI_65848, color=color)

    def tanks_very_low_66018(self, color):
        """
        Simulate a tanks very low condition
        """
        return self.set_error_state(AlertTypeLEDM.TANKS_VERY_LOW_66018, color=color)

    def seho_at_insertion_65613(self, color):
        """
        Simulate a SEHO at insertion condition
        """
        return self.set_error_state(AlertTypeLEDM.SEHOATINSERTION_65613, color=color)

    def cartridge_very_low_65672(self, color):
        """
        Simulate a Cartridge Very Low condition
        """
        return self.set_error_state(AlertTypeLEDM.CARTRIDGE_VERYLOW_65672, color=color)

    def subscriptionconsumable_temporary_usage_allowed_65934(self, color):
        """
        Simulate a Subscription Consumable Temporary Usage Allowed condition
        """
        return self.set_error_state(AlertTypeLEDM.SUBSCRIPTIONCONSUMABLE_TEMPORARYUSAGE_ALLOWED_65934, color=color)

    def tanks_very_low_66332(self, color):
        """
        Simulate a Tanks Very Low condition
        """
        return self.set_error_state(AlertTypeLEDM.TANKS_VERY_LOW_66332, color=color)

    def cartridge_verylow(self, color):
        """
        Simulate a Cartridge Very Low condition
        """
        return self.set_error_state(AlertTypeLEDM.CARTRIDGE_VERYLOW, color=color)
