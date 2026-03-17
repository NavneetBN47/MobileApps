import pytest
from MobileApps.libs.flows.ios.smart.smart_flow import SmartFlow

class Personalize(SmartFlow):
    flow_name = "personalize"

    TILES = [
        "get_supplies", "printables", "shortcuts", "mobile_fax", "print_photos", 
        "print_documents", "camera_scan", "help_and_support", "printer_scan", "copy"
    ]

    SWITCHES = [
        "get_supplies_switch", "printables_switch", "shortcuts_switch", "mobile_fax_switch",
        "print_photos_switch", "print_documents_switch", "camera_scan_switch", "help_and_support_switch", 
        "printer_scan_switch", "copy_switch"
    ]

    MOBILE_FAX_SWITCH = "mobile_fax_switch"
########################################################################################################################
#                                                                                                                      #
#                                              ACTION  FLOWS                                                           #
#                                                                                                                      #
########################################################################################################################

    def toggle_switch_by_name(self, tile_name, on=True):
        """
        param on: bool True to toggle on, False to toggle off
        """
        self.driver.check_box(tile_name, attribute="value", uncheck=(not on))

    def toggle_all_tiles(self, on=True):
        for tile in self.get_tile_names():
            tile = "_".join([word if word != '&' else 'and' for word in tile.lower().split(" ")])
            self.driver.check_box(f"{tile}_switch", attribute="value", uncheck=(not on))

    def get_tile_names(self):
        tiles = self.driver.find_object("tile_frame", multiple=True, root_obj=self.driver.find_object("tiles_parent"))
        names_list = [tile.text for tile in tiles]
        return names_list

    def toggle_switch_by_index(self, index, on=True):
        self.driver.check_box(self.SWITCHES[index], attribute="value", uncheck=(not on))

    def get_enabled_tiles_names(self):
        enabled_tiles = []
        tile_names = self.get_tile_names()
        for index, tile in enumerate(self.TILES):
            if int(self.driver.get_attribute(f"{tile}_switch", "value")):
                enabled_tiles.append(tile_names[index])
        return enabled_tiles
        
    def toggle_tiles_to_opposite_state(self):
        for switch in self.SWITCHES:
            self.driver.click(switch)
            
########################################################################################################################
#                                                                                                                      #
#                                              VERIFICATION  FLOWS                                                     #
#                                                                                                                      #
########################################################################################################################

    def verify_personalize_screen(self):
        """
        Verify that current screen is Personalize screen
        """
        self.driver.wait_for_object("_shared_str_personalized_tiles")
        self.driver.wait_for_object("done_btn")
    
    def verify_personalize_tiles_and_switches(self):
        for tile, switch in zip(self.TILES, self.SWITCHES):
            if pytest.platform == "IOS":
                self.driver.scroll(tile)
                self.driver.scroll(switch)
            else:
                self.driver.wait_for_object(tile)
                self.driver.wait_for_object(switch)