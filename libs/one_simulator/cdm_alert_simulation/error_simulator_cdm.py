from MobileApps.libs.one_simulator.cdm_alert_simulation.alert_type_cdm import SimulatorErrorManagerCDM, AlertTypeCDM


class ErrorSimulatorCDM(SimulatorErrorManagerCDM):
    def anti_theft_enabled_error_65612(self, color):
        """
        Simulate a printer anti-theft enabled error condition
        """
        return self.set_error_state(AlertTypeCDM.ANTI_THEFT_ENABLED_ERROR_65612, color=color)

    def anti_theft_enabled_error_66175(self, color):
        """
        Simulate a printer anti-theft enabled error condition
        """
        return self.set_error_state(AlertTypeCDM.ANTI_THEFT_ENABLED_ERROR_66175, color=color)

    def missing_all_cartridge_65537(self, color):
        """
        Simulate a missing all cartridge error condition
        """
        return self.set_error_state(AlertTypeCDM.CARTRIDGES_MISSING_65537, color=color)

    def cartridge_faulty_65542(self, color):
        """
        Simulate a cartridge failure error condition
        """
        return self.set_error_state(AlertTypeCDM.CARTRIDGE_FAULTY_65542, color=color)

    def incompatible_ink_cartridge_65543(self, color):
        """
        Simulate an incompatible ink cartridge error condition
        """
        return self.set_error_state(AlertTypeCDM.INCOMPATIBLE_CARTRIDGE_65543, color=color)

    def cartridge_in_wrong_slot_65544(self, color):
        """
        Simulate a cartridge in wrong slot error condition
        """
        return self.set_error_state(AlertTypeCDM.CARTRIDGE_IN_WRONG_SLOT_65544, color=color)

    def trade_cartridge_when_expect_host_65590(self, color):
        """
        Simulate a trade cartridge when expect host error condition
        """
        return self.set_error_state(AlertTypeCDM.CARTRIDGE_EXPECTED_SETUP_65590, color=color)

    def cartridge_expected_setup_low_65590(self, color):
        """
        Simulate a cartridge expected setup low error condition
        """
        return self.set_error_state(AlertTypeCDM.CARTRIDGEEXPECTEDSETUP_LOW_65590, color=color)

    def cartridge_expected_setup_verylow_65590(self, color):
        """
        Simulate a cartridge expected setup very low error condition
        """
        return self.set_error_state(AlertTypeCDM.CARTRIDGEEXPECTEDSETUP_VERYLOW_65590, color=color)

    def cartridge_expected_setup_altered_supply_65590(self, color):
        """
        Simulate a cartridge expected setup altered supply error condition
        """
        return self.set_error_state(AlertTypeCDM.CARTRIDGEEXPECTEDSETUP_ALTERED_SUPPLY_65590, color=color)

    def host_cartridge_when_expect_trade_65591(self, color):
        """
        Simulate a host cartridge when expect trade error condition
        """
        return self.set_error_state(AlertTypeCDM.CARTRIDGE_NON_EXPECTED_65591, color=color)

    def anti_theft_enabled_supply_detected_65612(self, color):
        """
        Simulate an anti-theft enabled supply detected error condition
        """
        return self.set_error_state(AlertTypeCDM.ANTITHEFT_ENABLED_SUPPLYDETECTED_65612, color=color)

    def unsubscribedstate_inCompatible_ink_65765(self, color):
        """
        Simulate a subscription consumable needs enrollment error condition
        """
        return self.set_error_state(AlertTypeCDM.UNSUBSCRIBEDSTATE_INCOMPATIBLE_INK_65765, color=color)

    def cartridge_or_account_issue_66175(self, color):
        """
        Simulate a cartridge or account issue error condition
        """
        return self.set_error_state(AlertTypeCDM.CARTRIDGE_OR_ACCOUNT_ISSUE_66175, color=color)

    def cartridge_missing_66262(self, color):
        """
        Simulate a cartridge missing error condition
        """
        return self.set_error_state(AlertTypeCDM.CARTRIDGE_MISSING_66262, color=color)

    def cartridge_problem_66277(self, color):
        """
        Simulate a cartridge problem error condition
        """
        return self.set_error_state(AlertTypeCDM.CARTRIDGE_PROBLEM_66277, color=color)

    def cartridge_problem_66278(self, color):
        """
        Simulate a cartridge problem error condition
        """
        return self.set_error_state(AlertTypeCDM.CARTRIDGE_PROBLEM_66278, color=color)

    def cartridge_problem_66279(self, color):
        """
        Simulate a cartridge problem error condition
        """
        return self.set_error_state(AlertTypeCDM.CARTRIDGE_PROBLEM_66279, color=color)

    def incompatible_cartridges_66283(self, color):
        """
        Simulate an incompatible cartridges error condition
        """
        return self.set_error_state(AlertTypeCDM.INCOMPATIBLE_CARTRIDGES_66283, color=color)

    def incompatible_cartridges_66284(self, color):
        """
        Simulate an incompatible cartridges error condition
        """
        return self.set_error_state(AlertTypeCDM.INCOMPATIBLE_CARTRIDGES_66284, color=color)

    def incompatible_cartridges_66285(self, color):
        """
        Simulate an incompatible cartridges error condition
        """
        return self.set_error_state(AlertTypeCDM.INCOMPATIBLE_CARTRIDGES_66285, color=color)

    def cartridges_rejected_66293(self, color):
        """
        Simulate a cartridges rejected error condition
        """
        return self.set_error_state(AlertTypeCDM.CARTRIDGES_REJECTED_66293, color=color)

    def use_setup_cartridges_66297(self, color):
        """
        Simulate a use setup cartridges error condition
        """
        return self.set_error_state(AlertTypeCDM.USE_SETUP_CARTRIDGES_66297, color=color)

    def do_not_use_setup_cartridges_66299(self, color):
        """
        Simulate a do not use setup cartridges error condition
        """
        return self.set_error_state(AlertTypeCDM.DO_NOT_USE_SETUP_CARTRIDGES_66299, color=color)

    def do_not_use_setup_cartridges_66300(self, color):
        """
        Simulate a do not use setup cartridges error condition
        """
        return self.set_error_state(AlertTypeCDM.DO_NOT_USE_SETUP_CARTRIDGES_66300, color=color)

    def hp_protected_cartridges_installed_66304(self, color):
        """
        Simulate an HP protected cartridges installed error condition
        """
        return self.set_error_state(AlertTypeCDM.HP_PROTECTED_CARTRIDGES_INSTALLED_66304, color=color)

    def hp_protected_cartridges_installed_66305(self, color):
        """
        Simulate an HP protected cartridges installed error condition
        """
        return self.set_error_state(AlertTypeCDM.HP_PROTECTED_CARTRIDGES_INSTALLED_66305, color=color)

    def hp_instant_ink_66315(self, color):
        """
        Simulate an HP Instant Ink error condition
        """
        return self.set_error_state(AlertTypeCDM.HP_INSTANT_INK_66315, color=color)

    def nonhp_chip_detected_66339(self, color):
        """
        Simulate a non-HP chip detected error condition
        """
        return self.set_error_state(AlertTypeCDM.NONHP_CHIP_DETECTED_66339, color=color)

    def nonhp_circuitry_detected_66341(self, color):
        """
        Simulate a non-HP circuitry detected error condition
        """
        return self.set_error_state(AlertTypeCDM.NONHP_CIRCUITRY_DETECTED_66341, color=color)

    def do_not_use_setup_cartridges_66298(self, color):
        """
        Simulate a do not use setup cartridges error condition
        """
        return self.set_error_state(AlertTypeCDM.DO_NOT_USE_SETUP_CARTRIDGES_66298, color=color)

    def incompatible_cartridge_region_65543(self, color):
        """
        Simulate an incompatible cartridge region error condition
        """
        return self.set_error_state(AlertTypeCDM.INCOMPATIBLE_CARTRIDGE_65543_REGION, color=color)

    def unsubscribedstate_incompatible_ink_65765(self, color):
        """
        Simulate an unsubscribed state incompatible ink error condition
        """
        return self.set_error_state(AlertTypeCDM.UNSUBSCRIBEDSTATE_INCOMPATIBLE_INK_65765, color=color)

    def outofink_66019(self, color):
        """
        Simulate an out of ink error condition
        """
        return self.set_error_state(AlertTypeCDM.OUTOFINK_66019, color=color)

    def printheadproblem_66207(self, color):
        """
        Simulate a print head problem error condition
        """
        return self.set_error_state(AlertTypeCDM.PRINTHEADPROBLEM_66207, color=color)

    def incompatible_printhead_66213(self, color):
        """
        Simulate an incompatible print head error condition
        """
        return self.set_error_state(AlertTypeCDM.INCOMPATABLE_PRINTHEAD, color=color)

    def non_hp_chip_66339(self, color):
        """
        Simulate a non-HP chip error condition
        """
        return self.set_error_state(AlertTypeCDM.NON_HP_CHIP, color=color)

    def oobe_hp_trade_66175(self, color):
        """
        Simulate an OOBE HP trade error condition
        """
        return self.set_error_state(AlertTypeCDM.OOBE_HP_TRADE_66175, color=color)

    def oobe_hp_altered_supply_anti_theft_66175(self, color):
        """
        Simulate an OOBE HP altered supply anti-theft 66175 error condition
        """
        return self.set_error_state(AlertTypeCDM.OOBE_HP_ALTERED_SUPPLY_ANTI_THEFT_66175, color=color)

    def oobe_hp_altered_supply_66175_hpplus(self, color):
        """
        Simulate an OOBE HP altered supply 66175 HP+ error condition
        """
        return self.set_error_state(AlertTypeCDM.OOBE_HP_ALTERED_SUPPLY_66175_HPPLUS, color=color)

    def oobe_loi_supply_66175(self, color):
        """
        Simulate an OOBE LOI supply 66175 error condition
        """
        return self.set_error_state(AlertTypeCDM.OOBE_LOI_SUPPLY_66175, color=color)

    def oobe_vloi_supply_66175(self, color):
        """
        Simulate an OOBE VLOI supply 66175 error condition
        """
        return self.set_error_state(AlertTypeCDM.OOBE_VLOI_SUPPLY_66175, color=color)

    def oobe_faulty_supply_shorted_contactpads_66175(self, color):
        """
        Simulate an OOBE faulty supply shorted contact pads 66175 error condition
        """
        return self.set_error_state(AlertTypeCDM.OOBE_FAULTY_SUPPLY_SHORTED_CONTACTPADS_66175, color=color)

    def do_not_use_setup_oobe_printer_trial_pen_66175(self, color):
        """
        Simulate a do not use setup OOBE printer trial pen 66175 error condition
        """
        return self.set_error_state(AlertTypeCDM.DO_NOT_USE_SETUP_OOBE_PRINTER_TRIAL_PEN_66175, color=color)

    def hp_altered_supply_insert_t4_pen_from_another_printer_66175(self, color):
        """
        Simulate an HP altered supply insert T4 pen from another printer 66175 error condition
        """
        return self.set_error_state(AlertTypeCDM.HP_ALTERED_SUPPLY_INSERT_T4_PEN_FROM_ANOTHER_PRINTER_66175, color=color)

    def non_hp_circuitry_66175(self, color):
        """
        Simulate a non-HP circuitry 66175 error condition
        """
        return self.set_error_state(AlertTypeCDM.NON_HP_CIRCUITRY_66175, color=color)

    def hppi_circuitry_pen_digital_signature_66175(self, color):
        """
        Simulate an HPPI circuitry pen digital signature 66175 error condition
        """
        return self.set_error_state(AlertTypeCDM.HPPI_CIRCUITRY_PEN_DIGITAL_SIGNATURE, color=color)

    def pen_type_proto_bit_regionalisation_section_66175(self, color):
        """
        Simulate a pen type proto bit regionalisation section 66175 error condition
        """
        return self.set_error_state(AlertTypeCDM.PEN_TYPE_PROTO_BIT_REGIONALISATION_SECTION_66175, color=color)

    def incompatible_hp_instant_ink_66175(self,  color):
        """
        Simulate an incompatible HP instant ink 66175 error condition
        """
        return self.set_error_state(AlertTypeCDM.INCOMPATIBLE_HP_INSTANT_INK_66175, color=color)

    def unsubscribed_state_instant_ink_supply_install_new_instant_ink_supply_66175(self, color):
        """
        Simulate an unsubscribed state instant ink supply install new instant ink supply 66175 error condition
        """
        return self.set_error_state(AlertTypeCDM.UNSUBSCRIBED_STATE_INSTANT_INK_SUPPLY_INSTALL_NEW_INSTANT_INK_SUPPLY_66175, color=color)

    def misinstalled_cartridge_66175(self, color):
        """
        Simulate a misinstalled cartridge 66175 error condition
        """
        return self.set_error_state(AlertTypeCDM.MISINSTALLED_CARTRIDGE_66175, color=color)

    def oobe_faulty_supply_shorted_contactpads_66175_hpplus(self, color):
        """
        Simulate an OOBE faulty supply shorted contact pads 66175 HP+ error condition
        """
        return self.set_error_state(AlertTypeCDM.OOBE_FAULTY_SUPPLY_SHORTED_CONTACTPADS_66175_HPPLUS, color=color)

    def subscribed_state_previously_used_hp_instant_ink_hpplusii_66175(self, color):
        """
        Simulate a subscribed state previously used HP instant ink HP+II 66175 error condition
        """
        return self.set_error_state(AlertTypeCDM.SUBSCRIBED_STATE_PREVIOUSLY_USED_HP_INSTANT_INK_HPPLUSII_66175, color=color)

    def incompatible_cartridge_region_66175(self, color):
        """
        Simulate an incompatible cartridge region 66175 error condition
        """
        return self.set_error_state(AlertTypeCDM.INCOMPATIBLE_CARTRIDGE_REGION_66175, color=color)

    def print_head_problem_66211(self, color):
        """
        Simulate a print head problem 66211 error condition
        """
        return self.set_error_state(AlertTypeCDM.PRINTHEADPROBLEM_66211, color=color)

    def hp_protected_printheads_installed_66230(self, color):
        """
        Simulate an HP protected printheads installed 66230 error condition
        """
        return self.set_error_state(AlertTypeCDM.HP_PROTECTED_PRINTHEADS_INSTALLED_66230, color=color)

    def antitheft_enabled_supplyerror_66035(self, color):
        """
        Simulate an anti-theft enabled supply error 66035 error condition
        """
        return self.set_error_state(AlertTypeCDM.ANTITHEFT_ENABLED_SUPPLYERROR_66035, color=color)

    def cartridge_unauthorized_65926(self, color):
        """
        Simulate a cartridge unauthorized 65926 error condition
        """
        return self.set_error_state(AlertTypeCDM.CARTRIDGE_UNAUTHORIZED_65926, color=color)

    def c(self, color):
        """
        Simulate a cartridge very low stop 66039 error condition
        """
        return self.set_error_state(AlertTypeCDM.CARTRIDGE_VERYLOWSTOP_66039, color=color)

    def cartridge_memoryerror_65542(self, color):
        """
        Simulate a cartridge memory error 65542 error condition
        """
        return self.set_error_state(AlertTypeCDM.CARTRIDGE_MEMORYERROR_65542, color=color)

    def cartridge_missing_66034(self, color):
        """
        Simulate a cartridge missing 66034 error condition
        """
        return self.set_error_state(AlertTypeCDM.CARTRIDGE_MISSING_66034, color=color)

    def used_supply_prompt_66043(self, color):
        """
        Simulate a Used Supply Prompt 66043 error condition
        """
        return self.set_error_state(AlertTypeCDM.USED_SUPPLY_PROMPT_66043, color=color)
    
    def cartridge_wrong_slot(self, color):
        """
        Simulate a Cartridge Wrong Slot condition
        """
        return self.set_error_state(AlertTypeCDM.CARTRIDGE_WRONG_SLOT, color=color)
    
    def incompatible_cartridge_65543(self, color):
        """
        Simulate an incompatible cartridge 65543 error condition
        """
        return self.set_error_state(AlertTypeCDM.INCOMPATIBLE_CARTRIDGE_65543, color=color)

    def printhead_replacement_incomplete_66130(self, color):
        """
        Simulate a printhead replacement incomplete 66130 error condition
        """
        return self.set_error_state(AlertTypeCDM.PRINTHEAD_REPLACEMENT_INCOMPLETE_66130, color=color)

    def printhead_not_present_66128(self, color):
        """
        Simulate a printhead not present 66128 error condition
        """
        return self.set_error_state(AlertTypeCDM.PRINTHEAD_NOT_PRESENT_66128, color=color)

    def printhead_reseat_66131(self, color):
        """
        Simulate a printhead reseat 66131 error condition
        """
        return self.set_error_state(AlertTypeCDM.PRINTHEAD_RESEAT_66131, color=color)

    def outofink_66537(self, color):
        """
        Simulate an out of ink 66537 error condition
        """
        return self.set_error_state(AlertTypeCDM.OUTOFINK_66537, color=color)

    def cartridge_missing_65589(self, color):
        """
        Simulate a cartridge missing error condition
        """
        return self.set_error_state(AlertTypeCDM.CARTRIDGE_MISSING_65589, color=color)

    def cartridge_safe_stop_65939(self, color):
        """
        Simulate a cartridge safe stop 65939 error condition
        """
        return self.set_error_state(AlertTypeCDM.CARTRIDGE_SAFE_STOP_65939, color=color)

    def printhead_failure_66442(self, color):
        """
        Simulate a printhead failure 66442 error condition
        """
        return self.set_error_state(AlertTypeCDM.PRINTHEAD_FAILURE_66442, color=color)

    def idsstartup_blocked_loi_flow_66440(self, color):
        """
        Simulate an insufficient ink to startup brand printhead 66440 error condition
        """
        return self.set_error_state(AlertTypeCDM.IDSSTARTUP_BLOCKED_LOI_FLOW_66440, color=color)

    def outofink_66618(self, color):
        """
        Simulate an out of ink 66618 error condition
        """
        return self.set_error_state(AlertTypeCDM.OUTOFINK_66618, color=color)