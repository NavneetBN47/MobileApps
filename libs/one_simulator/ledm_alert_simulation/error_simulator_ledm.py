from MobileApps.libs.one_simulator.ledm_alert_simulation.alert_type_ledm import AlertTypeLEDM, SimulatorErrorManagerLEDM


class ErrorSimulatorLEDM(SimulatorErrorManagerLEDM):
    def cartridge_missing_65537(self, color):
        """
        Simulate a missing cartridge condition
        """
        return self.set_error_state(AlertTypeLEDM.CARTRIDGES_MISSING_65537, color=color)

    def cartridge_missing_65589(self, color):
        """
        Simulate a missing cartridge condition
        """
        return self.set_error_state(AlertTypeLEDM.CARTRIDGE_MISSING_65589, color=color)

    def cartridge_failure_65542(self, color):
        """
        Simulate a cartridge failure condition
        """
        return self.set_error_state(AlertTypeLEDM.CARTRIDGE_FAILURE_65542, color=color)

    def incompatible_ink_cartridge_65543(self, color):
        """
        Simulate an incompatible ink cartridge condition
        """
        return self.set_error_state(AlertTypeLEDM.INCOMPATIBLE_INK_CARTRIDGE_65543, color=color)

    def trade_cartridge_when_expect_host_65590(self, color):
        """
        Simulate a trade cartridge when expect host condition
        """
        return self.set_error_state(AlertTypeLEDM.TRADE_CARTRIDGE_WHEN_EXPECT_HOST_65590, color=color)

    def hp_altered_supply_65590_65592(self, color):
        """
        Simulate an HP altered supply condition
        """
        return self.set_error_state(AlertTypeLEDM.HP_ALTERED_SUPPLY_65590_65592, color=color)

    def host_cartridge_when_expect_trade_65591(self, color):
        """
        Simulate a host cartridge when expect trade condition
        """
        return self.set_error_state(AlertTypeLEDM.HOST_CARTRIDGE_WHEN_EXPECT_TRADE_65591, color=color)

    def anti_theft_enabled_supply_detected_65612(self, color):
        """
        Simulate an anti-theft enabled supply detected condition
        """
        return self.set_error_state(AlertTypeLEDM.ANTITHEFT_ENABLED_SUPPLY_DETECTED_65612, color=color)

    def cartridge_failure_instant_ink_subs_65675(self, color):
        """
        Simulate a cartridge failure condition
        """
        return self.set_error_state(AlertTypeLEDM.CARTRIDGEFAILURE_INSTANT_INK_SUBS_65675, color=color)

    def cartridge_failure_65675(self, color):
        """
        Simulate a cartridge failure condition
        """
        return self.set_error_state(AlertTypeLEDM.CARTRIDGEFAILURE_65675, color=color)

    def use_other_family_incompatible_65676(self, color):
        """
        Simulate an incompatible cartridges condition
        """
        return self.set_error_state(AlertTypeLEDM.USE_OTHER_FAMILY_INCOMPATIBLE_65676, color=color)

    def incompatible_cartridges_65676(self, color):
        """
        Simulate an incompatible cartridges condition
        """
        return self.set_error_state(AlertTypeLEDM.INCOMPATIBLE_CARTRIDGES_65676, color=color)

    def regional_cartridges_65676(self, color):
        """
        Simulate a regional cartridges condition
        """
        return self.set_error_state(AlertTypeLEDM.REGIONAL_CARTRIDGES_65676, color=color)

    def cartridge_missing_65690(self, color):
        """
        Simulate a cartridge missing condition
        """
        return self.set_error_state(AlertTypeLEDM.CARTRIDGEMISSING_65690, color=color)

    def anti_theft_enabled_supply_detected_65694(self, color):
        """
        Simulate an anti-theft enabled supply detected ink sub condition
        """
        return self.set_error_state(AlertTypeLEDM.ANTITHEFT_ENABLED_SUPPLYDETECTED_65694, color=color)

    def trade_protected_cartridges_instant_ink_sub_65694(self, color):
        """
        Simulate a trade protected cartridges instant ink sub condition
        """
        return self.set_error_state(AlertTypeLEDM.TRADE_PROTECTED_CARTRIDGES_INSTANT_INK_SUB_65694, color=color)

    def subscription_consumable_needs_enrollment_65765(self, color):
        """
        Simulate a subscription consumable needs enrollment condition
        """
        return self.set_error_state(AlertTypeLEDM.SUBSCRIPTIONCONSUMABLE_NEEDS_ENROLLMENT_65765, color=color)

    def unsubscribed_state_install_new_instant_ink_supply_65765(self, color):
        """
        Simulate an unsubscribed state install new instant ink supply condition
        """
        return self.set_error_state(AlertTypeLEDM.UNSUBSCRIBED_STATE_INSTALL_NEW_INSTANT_INK_SUPPLY_65765, color=color)

    def missing_cartridge_hybrid_inksub_65769(self, color):
        """
        Simulate a missing cartridge hybrid ink sub condition
        """
        return self.set_error_state(AlertTypeLEDM.MISSING_CARTRIDGE_HYBRIDINKSUB_65769, color=color)

    def missing_cartridge_instantinksub_65769(self, color):
        """
        Simulate a missing cartridge instant ink sub condition
        """
        return self.set_error_state(AlertTypeLEDM.MISSING_CARTRIDGE_INSTANTINKSUB_65769, color=color)

    def anti_theft_enabled_supply_detected_65773(self, color):
        """
        Simulate an anti-theft enabled supply detected condition
        """
        return self.set_error_state(AlertTypeLEDM.ANTITHEFT_ENABLED_SUPPLY_DETECTED_65773, color=color)

    def cartridges_in_wrong_slot_65544(self, color):
        """
        Simulate a cartridges in wrong slot condition
        """
        return self.set_error_state(AlertTypeLEDM.CARTRIDGEIN_WRONGSLOT_65544, color=color)

    def insert_non_setup_cartridge_65688(self, color):
        """
        Simulate an insert non-setup cartridge condition
        """
        return self.set_error_state(AlertTypeLEDM.INSERTNONSETUPCARRIDGE_65688, color=color)

    def instant_ink_xmos2_reject_cartridge_65846(self, color):   
        """
        Simulate an Instant Ink XMOS2 reject cartridge condition
        """
        return self.set_error_state(AlertTypeLEDM.INSTANTINK_XMOS2_REJECTCARTRIDGE_65846, color=color)

    def alignment_error_66564(self, color):
        """
        Simulate an alignment error condition
        """
        return self.set_error_state(AlertTypeLEDM.ALIGNMENT_ERROR_66564, color=color)
    
    def non_hp_circuitry_detected_66341(self, color):
        """
        Simulate a non-HP circuitry detected condition
        """
        return self.set_error_state(AlertTypeLEDM.NON_HP_CIRCUITRY_66341, color=color)

    def non_hp_chip_detected_66339(self, color):
        """
        Simulate a non-HP circuitry detected condition
        """
        return self.set_error_state(AlertTypeLEDM.NON_HP_CHIP_66339, color=color)

    def hp_instant_ink_66315(self, color):
        """
        Simulate an HP Instant Ink condition
        """
        return self.set_error_state(AlertTypeLEDM.HP_INSTANT_INK_66315, color=color)

    def hp_protected_cartridges_installed_66305(self, color):
        """
        Simulate an HP Protected Cartridges Installed condition
        """
        return self.set_error_state(AlertTypeLEDM.HP_PROTECTED_CARTRIDGES_INSTALLED_66305, color=color)

    def hp_protected_cartridges_installed_66304(self, color):
        """
        Simulate an HP Protected Cartridges Installed condition
        """
        return self.set_error_state(AlertTypeLEDM.HP_PROTECTED_CARTRIDGES_INSTALLED_66304, color=color)

    def do_not_use_setup_cartridges_66300(self, color):
        """
        Simulate an HP Do Not Use Setup Cartridges condition
        """
        return self.set_error_state(AlertTypeLEDM.DO_NOT_USE_SETUP_CARTRIDGES_66300, color=color)

    def do_not_use_setup_cartridges_66299(self, color):
        """
        Simulate an HP Do Not Use Setup Cartridges condition
        """
        return self.set_error_state(AlertTypeLEDM.DO_NOT_USE_SETUP_CARTRIDGES_66299, color=color)

    def do_not_use_setup_cartridges_66298(self, color):
        """
        Simulate an HP Do Not Use Setup Cartridges condition
        """
        return self.set_error_state(AlertTypeLEDM.DO_NOT_USE_SETUP_CARTRIDGES_66298, color=color)

    def use_setup_cartridges_66297(self, color):
        """
        Simulate an HP Use Setup Cartridges condition
        """
        return self.set_error_state(AlertTypeLEDM.USE_SETUP_CARTRIDGES_66297, color=color)

    def cartridges_rejected_66293(self, color):
        """
        Simulate an HP Cartridges Rejected condition
        """
        return self.set_error_state(AlertTypeLEDM.CARTRIDGES_REJECTED_66293, color=color)

    def cartridges_in_wrong_slot_66286(self, color):
        """
        Simulate an HP Cartridges in Wrong Slot condition
        """
        return self.set_error_state(AlertTypeLEDM.CARTRIDGES_IN_WRONG_SLOT_66286, color=color)

    def incompatible_cartridges_66285(self, color):
        """
        Simulate an HP Incompatible Cartridges condition
        """
        return self.set_error_state(AlertTypeLEDM.INCOMPATIBLE_CARTRIDGES_66285, color=color)

    def incompatible_cartridges_66284(self, color):
        """
        Simulate an HP Incompatible Cartridges condition
        """
        return self.set_error_state(AlertTypeLEDM.INCOMPATIBLE_CARTRIDGES_66284, color=color)

    def incompatible_cartridges_66283(self, color):
        """
        Simulate an HP Incompatible Cartridges condition
        """
        return self.set_error_state(AlertTypeLEDM.INCOMPATIBLE_CARTRIDGES_66283, color=color)

    def cartridge_problem_66279(self, color):
        """
        Simulate an HP Cartridge Problem condition
        """
        return self.set_error_state(AlertTypeLEDM.CARTRIDGE_PROBLEM_66279, color=color)

    def cartridge_problem_66278(self, color):
        """
        Simulate an HP Cartridge Problem condition
        """
        return self.set_error_state(AlertTypeLEDM.CARTRIDGE_PROBLEM_66278, color=color)

    def cartridge_problem_66277(self, color):
        """
        Simulate an HP Cartridge Problem condition
        """
        return self.set_error_state(AlertTypeLEDM.CARTRIDGE_PROBLEM_66277, color=color)

    def cartridges_missing_66262(self, color):
        """
        Simulate an HP Cartridges Missing condition
        """
        return self.set_error_state(AlertTypeLEDM.CARTRIDGES_MISSING_66262, color=color)

    def oobe_hp_altered_supply_refilled_66175(self, color):
        """
        Simulate an OOBE HP Altered Supply Refilled condition
        """
        return self.set_error_state(AlertTypeLEDM.OOBE_HP_ALTERED_SUPPLY_REFILLED_66175, color=color)

    def oobe_faulty_supply_66175(self, color):
        """
        Simulate an OOBE Faulty Supply condition
        """
        return self.set_error_state(AlertTypeLEDM.OOBE_FAULTY_SUPPLY_66175, color=color)

    def trial_pen_66175(self, color):
        """
        Simulate a Trial Pen condition
        """
        return self.set_error_state(AlertTypeLEDM.TRIAL_PEN_66175, color=color)

    def incompatible_pen_66175(self, color):
        """
        Simulate an Incompatible Pen condition
        """
        return self.set_error_state(AlertTypeLEDM.INCOMPATIBLE_PEN_66175, color=color)

    def non_hp_circuitry_66175(self, color):
        """
        Simulate a Non-HP Circuitry condition
        """
        return self.set_error_state(AlertTypeLEDM.NON_HP_CIRCUITRY_66175, color=color)

    def protected_cartridges_66175(self, color):
        """
        Simulate a Protected Cartridges condition
        """
        return self.set_error_state(AlertTypeLEDM.PROTECTED_CARTRIDGES_66175, color=color)

    def instantink_subscription_successful_65767(self, color):
        return self.set_error_state(AlertTypeLEDM.INSTANTINK_SUBSCRIPTION_SUCCESSFUL_65767, color=color)

    def calibrating_65571(self, color):
        return self.set_error_state(AlertTypeLEDM.CALIBRATING_65571, color=color)

    def cartridge_missing_single_65537(self, color):
        """
        Simulate a missing single cartridge condition
        """
        return self.set_error_state(AlertTypeLEDM.CARTRIDGE_MISSING_SINGLE_65537, color=color)

    def cartridge_failure_65542_errorcode_170200(self, color):
        """
        Simulate a cartridge failure with error code 170200 condition
        """
        return self.set_error_state(AlertTypeLEDM.CARTRIDGE_FAILURE_65542_ERRORCODE_170200, color=color)

    def fill_tanks_66019(self, color):
        """
        Simulate a fill tanks condition
        """
        return self.set_error_state(AlertTypeLEDM.FILL_TANKS_66019, color=color)

    def failed_printhead_65536(self):
        """
        Simulate a failed printhead condition
        """
        return self.set_error_state(AlertTypeLEDM.FAILED_PRINTHEAD_65536)

    def missing_printhead_65536(self):
        """
        Simulate a missing printhead condition
        """
        return self.set_error_state(AlertTypeLEDM.MISSING_PRINTHEAD_65536)

    def incompatible_printhead_65536(self):
        """
        Simulate an incompatible printhead condition
        """
        return self.set_error_state(AlertTypeLEDM.INCOMPATIBLE_PRINTHEAD_65536)

    def ink_cartridge_empty_65539(self, color):
        """
        Simulate an ink cartridge empty condition
        """
        return self.set_error_state(AlertTypeLEDM.INK_CARTRIDGE_EMPTY_65539, color=color)

    def shaid_ooi_too_early_65541(self, color):
        """
        Simulate a SHaid OOI Too Early condition
        """
        return self.set_error_state(AlertTypeLEDM.SHAID_OOI_Too_EARLY_65541, color=color)

    def shaid_ooi_too_early_65800(self, color):
        """
        Simulate a SHaid OOI Too Early condition
        """
        return self.set_error_state(AlertTypeLEDM.SHAID_OOI_Too_EARLY_65800, color=color)

    def printer_error_65541(self):
        """
        Simulate a Printer Error condition
        """
        return self.set_error_state(AlertTypeLEDM.PRINTER_ERROR_65541)

    def media_too_short_to_auto_duplex_65572(self, color):
        """
        Simulate a Media Too Short To Auto Duplex condition
        """
        return self.set_error_state(AlertTypeLEDM.MEDIA_TOO_SHORT_TO_AUTO_DUPLEX_65572, color=color)

    def startup_failure_65599(self, color):
        """
        Simulate a Startup Failure condition
        """
        return self.set_error_state(AlertTypeLEDM.STARTUP_FAILURE_65599, color=color)

    def close_door_cover_65725(self):
        """
        Simulate a Close Door Cover condition
        """
        return self.set_error_state(AlertTypeLEDM.CLOSE_DOOR_COVER_65725)

    def printhead_cartridge_missing_66207(self, color):
        """
        Simulate a Printhead Cartridge Missing condition
        """
        return self.set_error_state(AlertTypeLEDM.PRINTHEAD_CARTRIDGE_MISSING_66207, color=color)

    def printhead_failure_66211(self, color):
        """
        Simulate a Printhead Failure condition
        """
        return self.set_error_state(AlertTypeLEDM.PRINTHEAD_FAILURE_66211, color=color)

    def incompatible_printhead_66213(self, color):
        """
        Simulate an Incompatible Printhead condition
        """
        return self.set_error_state(AlertTypeLEDM.INCOMPATIBLE_PRINTHEAD_66213, color=color)

    def hp_protected_printheads_installed_66230(self, color):
        """
        Simulate an HP Protected Printheads Installed condition
        """
        return self.set_error_state(AlertTypeLEDM.PROTECTED_PRINTHEAD_66230, color=color)

    def shared_select_address_error_66209(self):
        """
        Simulate a Shared Select Address Error condition
        """
        return self.set_error_state(AlertTypeLEDM.SHARED_SELECT_ADDRESS_ERROR_66209)

    def fill_tanks_66333(self, color):
        """
        Simulate a fill tanks condition
        """
        return self.set_error_state(AlertTypeLEDM.FILL_TANKS_66333, color=color)

    def defective_memory_66038(self, color):
        """
        Simulate a Defective Memory condition
        """
        return self.set_error_state(AlertTypeLEDM.DEFECTIVE_MEMORY_66038, color=color)

    def cartridge_out(self, color):
        """
        Simulate a Cartridge Out condition
        """
        return self.set_error_state(AlertTypeLEDM.CARTRIDGE_OUT, color=color)

    def antitheft_enabled_supplydetected(self, color):
        """
        Simulate an Anti-Theft Enabled Supply Detected condition
        """
        return self.set_error_state(AlertTypeLEDM.ANTI_THEFT_ENABLED_SUPPLY_DETECTED, color=color)

    def incompatible_cartridge(self, color):
        """
        Simulate an Incompatible Cartridge condition
        """
        return self.set_error_state(AlertTypeLEDM.INCOMPATIBLE_CARTRIDGE, color=color)

    def unauthorized_cartridge(self, color):
        """
        Simulate an Unauthorized Cartridge condition
        """
        return self.set_error_state(AlertTypeLEDM.UNAUTHORIZED_CARTRIDGE, color=color)

    def cartridge_missing(self, color):
        """
        Simulate a Cartridge Missing condition
        """
        return self.set_error_state(AlertTypeLEDM.CARTRIDGE_MISSING, color=color)

    def all_cartridge_missing(self,color):
        """
        Simulate an All Cartridge Missing condition
        """
        return self.set_error_state(AlertTypeLEDM.ALL_CARTRIDGE_MISSING, color=color)

    def used_counterfeit_cartridge(self, color):
        """
        Simulate a Used Counterfeit Cartridge condition
        """
        return self.set_error_state(AlertTypeLEDM.USED_COUNTERFEIT_CARTRIDGE, color=color)

    def incompatible_cartridge(self, color):
        """
        Simulate an Incompatible Cartridge condition
        """
        return self.set_error_state(AlertTypeLEDM.INCOMPATIBLE_CARTRIDGE, color=color)
    
    def cartridge_wrong_slot(self, color):
        """
        Simulate a Cartridge Wrong Slot condition
        """
        return self.set_error_state(AlertTypeLEDM.CARTRIDGE_WRONG_SLOT, color=color)
    
    def unauthorized_supply_65926(self, color):
        """
        Simulate an Unauthorized Supply condition
        """
        return self.set_error_state(AlertTypeLEDM.UNAUTHORIZED_SUPPLY_65926, color=color)

    def counterfeit_cartridges_installed_66043(self, color):
        """
        Simulate a Counterfeit Cartridges Installed condition
        """
        return self.set_error_state(AlertTypeLEDM.COUNTERFEIT_CARTRIDGES_INSTALLED_66043, color=color)
