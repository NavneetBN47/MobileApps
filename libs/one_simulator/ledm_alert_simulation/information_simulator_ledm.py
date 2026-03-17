from MobileApps.libs.one_simulator.ledm_alert_simulation.alert_type_ledm import AlertTypeLEDM, SimulatorErrorManagerLEDM


class InformationSimulatorLEDM(SimulatorErrorManagerLEDM):

    def ready(self):
        """
        Simulate a ready state for the printer
        """
        return self.set_error_state(AlertTypeLEDM.READY)

    def single_cartridge_mode_65553(self, color):
        """
        Simulate a single cartridge mode condition
        """
        return self.set_error_state(AlertTypeLEDM.SINGLE_CARTRIDGE_MODE_65553, color=color)
    
    def single_cartridge_mode_hybrid_inksub_65771(self, color):
        """
        Simulate a single cartridge mode hybrid ink sub condition
        """
        return self.set_error_state(AlertTypeLEDM.SINGLECARTRIDGE_MODE_HYBRIDINKSUB_65771, color=color)

    def used_consumable_65554(self, color):
        """
        Simulate a used consumable condition
        """
        return self.set_error_state(AlertTypeLEDM.USED_CONSUMABLE_65554, color=color)

    def supplies_low_65557(self, color):
        """
        Simulate a supplies low condition
        """
        return self.set_error_state(AlertTypeLEDM.SUPPLIES_LOW_65557, color=color)

    def supplies_low_printing_65557(self, color):
        """
        Simulate a supplies low printing condition
        """
        return self.set_error_state(AlertTypeLEDM.SUPPLIES_LOW_PRINTING_65557, color=color)

    def genuine_hp_65561(self, color):
        """
        Simulate a genuine HP condition
        """
        return self.set_error_state(AlertTypeLEDM.GENUINE_HP_65561, color=color)

    def used_consumable_inksub_65680(self, color):
        """
        Simulate a used consumable ink sub condition
        """
        return self.set_error_state(AlertTypeLEDM.USEDCONSUMABLE_INKSUB_65680, color=color)

    def previously_used_consumable_instant_ink_sub_65680(self, color):
        """
        Simulate a previously used consumable instant ink sub condition
        """
        return self.set_error_state(AlertTypeLEDM.PREVIOUSLY_USED_CONSUMABLE_INSTANT_INK_SUB_65680, color=color)

    def supplies_low_printing_65681(self, color):
        """
        Simulate a supplies low printing condition
        """
        return self.set_error_state(AlertTypeLEDM.SUPPLIES_LOW_PRINTING_65681, color=color)

    def supplies_low_65681(self, color):
        """
        Simulate a supplies low condition
        """
        return self.set_error_state(AlertTypeLEDM.SUPPLIES_LOW_65681, color=color)

    def supplies_low_printing_instant_ink_sub_65681(self, color):
        """
        Simulate a supplies low printing instant ink sub condition
        """
        return self.set_error_state(AlertTypeLEDM.SUPPLIES_LOW_PRINTING_INSTANT_INK_SUBS_65681, color=color)

    def low_on_ink_65590_65681(self, color):
        """
        Simulate a low on ink condition
        """
        return self.set_error_state(AlertTypeLEDM.LOW_ON_INK_65590_65681, color=color)

    def instantink_xmo2_genuinecartridge_65766(self, color):
        """
        Simulate an Instant Ink XMO2 genuine cartridge condition
        """
        return self.set_error_state(AlertTypeLEDM.INSTANTINK_XMO2_GENUINECARTRIDGE_65766, color=color)

    def instantink_tradecartridge_installed_65796(self, color):
        """
        Simulate an Instant Ink trade cartridge installed condition
        """
        return self.set_error_state(AlertTypeLEDM.INSTANTINK_TRADECARTRIDGE_INSTALLED_65796, color=color)

    def instantink_subscription_successful_65767(self, color):
        """
        Simulate an Instant Ink subscription successful condition
        """
        return self.set_error_state(AlertTypeLEDM.INSTANTINK_SUBSCRIPTION_SUCCESSFUL_65767, color=color)

    def new_hp_cartridges_installed_66265(self, color):
        """
        Simulate a new HP cartridges installed condition
        """
        return self.set_error_state(AlertTypeLEDM.GENUINE_HP_66265, color=color)

    def hp_cartridges_installed_66264(self, color):
        """
        Simulate an HP cartridges installed condition
        """
        return self.set_error_state(AlertTypeLEDM.USED_CONSUMABLE_66264, color=color)

    def single_cartridge_mode_66263(self, color):
        """
        Simulate a single cartridge mode condition
        """
        return self.set_error_state(AlertTypeLEDM.SINGLE_CARTRIDGE_MODE_66263, color=color)

    def cartridges_low_66242(self, color):
        """
        Simulate a cartridges low condition
        """
        return self.set_error_state(AlertTypeLEDM.CARTRIDGE_LOW_66242, color=color)

    def genuine_hp_inklevelzero_65684(self, color):
        """
        Simulate a genuine HP ink level zero condition
        """
        return self.set_error_state(AlertTypeLEDM.GENUINE_HP_INKLEVELZERO_65684, color=color)

    def tank_low_66017(self, color):
        """
        Simulate a tank low condition
        """
        return self.set_error_state(AlertTypeLEDM.TANK_LOW_66017, color=color)

    def tanks_filled_66020(self, color):
        """
        Simulate a tanks very low condition
        """
        return self.set_error_state(AlertTypeLEDM.TANKS_FILLED_66020, color=color)

    def nonhp_supply_detected_printing_65559(self, color):
        """
        Simulate a Non-HP supply detected printing condition
        """
        return self.set_error_state(AlertTypeLEDM.NONHP_SUPPLY_DETECTED_PRINTING_65559, color=color)

    def supplies_low_65669(self, color):
        """
        Simulate a supplies low condition
        """
        return self.set_error_state(AlertTypeLEDM.SUPPLIES_LOW_65669, color=color)  

    def supplies_low_printing_65669(self, color):
        """
        Simulate a supplies low printing condition
        """
        return self.set_error_state(AlertTypeLEDM.SUPPLIES_LOW_PRINTING_65669, color=color)

    def genuine_cartridges_installed_65862(self, color):
        """
        Simulate a genuine cartridges installed condition
        """
        return self.set_error_state(AlertTypeLEDM.GENUINE_CARTRIDGES_INSTALLED_65862, color=color)

    def nonhp_supply_detected_printing_66092(self, color):
        """
        Simulate a Non-HP supply detected printing condition
        """
        return self.set_error_state(AlertTypeLEDM.NONHP_SUPPLY_DETECTED_PRINTING_66092, color=color)

    def genuinehp_65851(self, color):
        """
        Simulate a genuine HP condition
        """
        return self.set_error_state(AlertTypeLEDM.GENUINE_HP_65851, color=color)

    def setup_cartridge_for_pha_65591_65851(self, color):
        """
        Simulate a setup cartridge for PHA condition
        """
        return self.set_error_state(AlertTypeLEDM.SETUP_CARTRIDGE_FOR_PHA_65591_65851, color=color)

    def used_consumable_66216(self, color):
        """
        Simulate a used consumable condition
        """
        return self.set_error_state(AlertTypeLEDM.USED_CONSUMABLE_66216, color=color)

    def genuine_ink_cartridges_installed_66222(self, color):
        """
        Simulate a genuine ink cartridges installed condition
        """
        return self.set_error_state(AlertTypeLEDM.GENUINE_INK_CARTRIDGES_INSTALLED_66222, color=color)
    
    def cartridge_low(self, color):
        """
        Simulate a cartridge low condition
        """
        return self.set_error_state(AlertTypeLEDM.CARTRIDGE_LOW, color=color)

    def non_hp_supply_flow_66092(self, color):
        """
        Simulate a Non-HP supply flow condition
        """
        return self.set_error_state(AlertTypeLEDM.NON_HP_SUPPLY_FLOW_66092, color=color)
