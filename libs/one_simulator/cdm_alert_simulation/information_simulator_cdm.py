from MobileApps.libs.one_simulator.cdm_alert_simulation.alert_type_cdm import SimulatorErrorManagerCDM, AlertTypeCDM


class InformationSimulatorCDM(SimulatorErrorManagerCDM):
    
    def ready(self):
        """Set the printer to a ready state"""
        return self.set_error_state(AlertTypeCDM.READY)

    def cartridge_very_low_65546(self, color):
        """
        Simulate a very low cartridge condition
        """
        return self.set_error_state(AlertTypeCDM.CARTRIDGE_VERY_LOW_65546, color=color)

    def single_cartridge_mode_65553(self, color):
        """
        Simulate a single cartridge mode condition
        """
        return self.set_error_state(AlertTypeCDM.SINGLE_INK_CARTRIDGE_MODE_65553, color=color)  

    def used_hp_cartridge_65554(self, color):
        """
        Simulate a used HP cartridge condition
        """
        return self.set_error_state(AlertTypeCDM.USED_HP_CARTRIDGE_65554, color=color)

    def supplies_low_65557(self, color):
        """
        Simulate a supplies low condition
        """
        return self.set_error_state(AlertTypeCDM.SUPPLIES_LOW_65557, color=color)

    def supplies_low_printing_65557(self, color):
        """
        Simulate a supplies low while printing condition
        """
        return self.set_error_state(AlertTypeCDM.SUPPLIES_LOW_PRINTING_65557, color=color)

    def loi_supply_66711(self, color):
        """
        Simulate a cartridges low condition
        """
        return self.set_error_state(AlertTypeCDM.LOI_SUPPLY_66711, color=color)

    def cartridge_expected_setup_65561(self, color):
        """
        Simulate a genuine HP cartridges condition
        """
        return self.set_error_state(AlertTypeCDM.CARTRIDGE_EXPECTED_SETUP_65561, color=color)

    def cartridges_low_66242(self, color):
        """
        Simulate a cartridges low condition
        """
        return self.set_error_state(AlertTypeCDM.CARTRIDGE_LOW_66242, color=color)

    def single_ink_cartridge_mode_66263(self, color):
        """
        Simulate a single ink cartridge mode condition
        """
        return self.set_error_state(AlertTypeCDM.SINGLE_CARTRIDGE_MODE_66263, color=color)

    def used_supply_prompt_66264(self, color):
        """
        Simulate an HP cartridges installed condition
        """
        return self.set_error_state(AlertTypeCDM.USED_SUPPLY_PROMPT_66264, color=color)

    def genuine_hp_supply_66265(self, color):
        """
        Simulate a genuine HP supply condition
        """
        return self.set_error_state(AlertTypeCDM.GENUINE_HP_SUPPLY_66265, color=color)

    def cartridges_low_66713(self, color):
        """
        Simulate a cartridges low condition
        """
        return self.set_error_state(AlertTypeCDM.LOI_SUPPLY_66713, color=color)

    def cartridge_low_66017(self, color):
        """
        Simulate a cartridge low condition
        """
        return self.set_error_state(AlertTypeCDM.CARTRIDGE_LOW_66017, color=color)

    def fulltank_66020(self, color):
        """
        Simulate a full tank condition
        """
        return self.set_error_state(AlertTypeCDM.FULLTANK_66020, color=color)

    def used_printhead_installation_66216(self, color):
        """
        Simulate a used printhead installation condition
        """
        return self.set_error_state(AlertTypeCDM.USED_PRINTHEAD_INSTALLATION_66216, color=color)

    def new_printhead_installation_66222(self, color):   
        """
        Simulate a new printhead installation condition
        """
        return self.set_error_state(AlertTypeCDM.NEW_PRINTHEAD_INSTALLATION_66222, color=color)

    def used_supply_flow_66264(self, color):
        """
        Simulate a used supply flow condition
        """
        return self.set_error_state(AlertTypeCDM.USED_SUPPLY_FLOW_66264, color=color)

    def genuine_hp_supply_flow_66265(self, color):
        """
        Simulate a genuine HP supply flow condition
        """
        return self.set_error_state(AlertTypeCDM.GENUINE_HP_SUPPLY_FLOW_66265, color=color)

    def cartridge_low_flow_65557(self,color):
        """
        Simulate a cartridge low flow condition
        """
        return self.set_error_state(AlertTypeCDM.CARTRIDGE_LOW_FLOW_65557, color=color)

    def genuinehp_supplyflow_66101(self, color):
        """
        Simulate a GenuineHP SupplyFlow 66101 error condition
        """
        return self.set_error_state(AlertTypeCDM.GENUINEHP_SUPPLYFLOW_66101, color=color)
    
    def cartridge_low_65669(self, color):
        """
        Simulate a cartridge low condition
        """
        return self.set_error_state(AlertTypeCDM.CARTRIDGE_LOW_65669, color=color)
    
    def non_hp_supply_flow_66092(self, color):
        """
        Simulate a non HP supply flow condition
        """
        return self.set_error_state(AlertTypeCDM.NON_HP_SUPPLY_FLOW_66092, color=color)

    def ids_delayed_backto_hp_66516(self, color):
        """
        Simulate an IDS delayed back to HP condition
        """
        return self.set_error_state(AlertTypeCDM.IDS_DELAYED_BACKTO_HP_66516, color=color)

    def tank_filled_66020(self, color):
        """
        Simulate a tank filled condition
        """
        return self.set_error_state(AlertTypeCDM.TANK_FILLED_66020, color=color)

    def tank_full_66437(self, color):
        """
        Simulate a tank full condition
        """
        return self.set_error_state(AlertTypeCDM.TANK_FULL_66437, color=color)

    def tank_low_66017(self, color):
        """
        Simulate a tank low condition
        """
        return self.set_error_state(AlertTypeCDM.TANK_LOW_66017, color=color)

    def ph_replacement_flow_66640(self, color):
        """
        Simulate a ph replacement flow condition
        """
        return self.set_error_state(AlertTypeCDM.PH_REPLACEMENT_FLOW_66640, color=color)
