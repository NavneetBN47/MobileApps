from MobileApps.libs.flows.web.hp_id.hp_id import HPID
from MobileApps.libs.flows.web.ows.olex_123_and_psw.traffic_director import TrafficDirector
from MobileApps.resources.const.web.const import *
from MobileApps.libs.flows.web.ows.olex_123_and_psw.power_on_country_language_step import CountryLanguageTrafficDirector
from MobileApps.libs.flows.web.ows.olex_123_and_psw.load_paper import LoadPaperTrafficDrector
from MobileApps.libs.flows.web.ows.olex_123_and_psw.load_ink import InstallInkTrafficDirector
from MobileApps.libs.flows.web.ows.olex_123_and_psw.semi_calibration_print import PrintCalibrationTrafficDirector
from MobileApps.libs.flows.web.ows.olex_123_and_psw.semi_calibration_scan import ScanCalibrationTrafficDirector
from MobileApps.libs.flows.web.ows.olex_123_and_psw.printer_use_td_step import PrinterUseTrafficDirector
from MobileApps.libs.flows.web.ows.olex_123_and_psw.setup_checklist_td_step import SetupChecklistTrafficDirector
from MobileApps.libs.flows.web.ows.olex_123_and_psw.hp_software_td_step import PrinterConnectionTrafficDirector
from MobileApps.libs.flows.web.ows.olex_123_and_psw.hp_software_td_step import FinishSetupBusinessTrafficDirector
from MobileApps.libs.flows.web.ows.olex_123_and_psw.hp_software_td_step import UnsupportedOSTrafficDirector
from MobileApps.libs.flows.web.ows.olex_123_and_psw.connect_usb import ConnectUSBTrafficDirector
from MobileApps.libs.flows.web.ows.olex_123_and_psw.driver_download import DriverDownloadTrafficDirector
import time

class TrafficDirectorLiveUI(object):

    def __init__(self, driver, printer_profile):
        self.driver = driver
        self.fd = {"hpid": HPID(driver),
                   "traffic_director" : TrafficDirector(driver, printer_profile),
                   "Country_Language_td":CountryLanguageTrafficDirector(driver),
                   "Load_paper_td": LoadPaperTrafficDrector(driver),
                   "load_ink_td": InstallInkTrafficDirector(driver),
                   "print_calibration": PrintCalibrationTrafficDirector(driver),
                   "scan_calibration": ScanCalibrationTrafficDirector(driver),
                   "printer_use": PrinterUseTrafficDirector(driver),
                   "setup_checklist": SetupChecklistTrafficDirector(driver),
                   "connect_usb": ConnectUSBTrafficDirector(driver),
                   "driver_download": DriverDownloadTrafficDirector(driver),
                   "hp_software": PrinterConnectionTrafficDirector(driver),
                   "finish_setup_business": FinishSetupBusinessTrafficDirector(driver),
                   "unsupported_os": UnsupportedOSTrafficDirector(driver)}
        
        self.power_on_select_language = {"moreto": 2, "victoria":2, "marconi_base":2, "marconi_hi":2, "kebin":2}
        self.load_paper = {"moreto": 4, "victoria_base":5, "victoria_plus":5, "marconi_base":3, "marconi_hi":3, "kebin":3, "trillium":6}
        self.load_paper_animations_card = {"moreto":5, "victoria_base":4, "victoria_plus":4, "marconi_base":5, "marconi_hi":5, "kebin":6, "trillium":6}
        self.install_ink = {"moreto": 5, "victoria_base":4, "victoria_plus":4, "marconi_base":4, "marconi_hi":4, "kebin":4, "trillium":5}
        self.install_ink_animation_card = {"moreto": 5, "victoria_base":4, "victoria_plus":4, "marconi_base":4, "marconi_hi":4,"kebin":4, "trillium":4}
        self.alignment_step = {"moreto":5, "victoria_base":4, "victoria_plus":4, "marconi_base":5, "marconi_hi":2, "kebin":2,"trillium":6}
        self.alignment_animations_card = {"moreto":5, "victoria_base":5, "victoria_plus":5, "marconi_base":5, "marconi_hi":1, "kebin":1, "trillium":4}
    
    def navigate_power_on_country_language_step(self):
        self.fd["Country_Language_td"].verify_web_page()
        self.fd["traffic_director"].verify_veneer_stepper()
        self.fd["traffic_director"].verify_current_live_ui_step_in_sidebar(step='1')
        self.fd["Country_Language_td"].verify_header_title()
        self.fd["Country_Language_td"].verify_power_on_card_content()
        self.fd["Country_Language_td"].verify_country_language_card()
        self.fd["traffic_director"].verify_footer_live_ui_steps()
        self.fd["traffic_director"].click_next_btn()

    def _verify_cards(self, fd_key, image_method, instruction_method, count):
        fd_obj = self.fd[fd_key]
        for i in range(count):
            getattr(fd_obj, image_method)(i)
            getattr(fd_obj, instruction_method)(i)

    def _verify_animation_cards(self, fd_key, step_method, instruction_method, card_count, spec_json_animation, step_key):
        fd_obj = self.fd[fd_key]
        
        for i in range(card_count):
            getattr(fd_obj, step_method)(i)
            getattr(fd_obj, instruction_method)(i)
            self.fd["traffic_director"].verify_current_carousal_dot(i)
            
            if spec_json_animation: 
                self.driver.validate_response_against_spec(step_key[i], spec_json_animation)
            
            if card_count > 1 and i != card_count - 1:
                self.fd["traffic_director"].click_animation_card_next_btn()
        
        assert self.fd["traffic_director"].verify_animation_card_next_btn(raise_e=False) is False, "Mismatched Number of animation cards or next button still shows after the last animation"

    def navigate_load_paper_step(self, printer_profile, spec_animation_data):
        profile_key = self._normalize_profile(printer_profile)
        if spec_animation_data:
            step_key = self._get_step_keys(spec_animation_data, "LoadPaper")
        else:
            step_key = []
        self.fd["Load_paper_td"].verify_web_page()
        self.fd["traffic_director"].verify_veneer_stepper()
        self.fd["traffic_director"].verify_current_live_ui_step_in_sidebar(step='1')
        self._verify_cards("Load_paper_td", "verify_load_paper_card_image", "verify_load_paper_card_instruction", self.load_paper[profile_key])
        self.fd["traffic_director"].click_view_animations_button()
        self.fd["Load_paper_td"].verify_card_slider()
        self._verify_animation_cards(
            "Load_paper_td",
            "verify_animation_card_step",
            "verify_animation_card_instruction",
            self.load_paper_animations_card[profile_key],
            spec_animation_data,
            step_key
        )
        self.fd["traffic_director"].click_watch_video_modal_close_button()
        self.fd["traffic_director"].click_next_btn()

    def navigate_install_ink_step(self, printer_profile, spec_animation_data):
        profile_key = self._normalize_profile(printer_profile)
        if spec_animation_data:
            step_key = self._get_step_keys(spec_animation_data, "InkInstalled")
        else:
            step_key = []
        self.fd["load_ink_td"].verify_web_page()
        self.fd["traffic_director"].verify_veneer_stepper()
        self.fd["traffic_director"].verify_current_live_ui_step_in_sidebar(step='2')
        self._verify_cards("load_ink_td", "verify_install_ink_card_image", "verify_install_ink_card_instruction", self.install_ink[profile_key])
        self.fd["load_ink_td"].verify_install_ink_step_td()
        self.fd["traffic_director"].click_view_animations_button()
        self._verify_animation_cards(
            "load_ink_td",
            "verify_animation_card_step",
            "verify_card_instructions",
            self.install_ink_animation_card[profile_key],
            spec_animation_data,
            step_key
        )
        self.fd["traffic_director"].click_watch_video_modal_close_button()
        self.fd["traffic_director"].click_next_btn()

    def navigate_alignment_step(self, printer_profile, spec_animation_data):
        profile_key = self._normalize_profile(printer_profile)
        if spec_animation_data:
            step_key = self._get_step_keys(spec_animation_data, "Alignment")
            step_key.append(self._get_step_keys(spec_animation_data, "PrintPage")[0])
        else:
            step_key = []
        self.fd["print_calibration"].verify_web_page()
        self.fd["traffic_director"].verify_veneer_stepper()
        self.fd["traffic_director"].verify_current_live_ui_step_in_sidebar(step='3')
        self._verify_cards("print_calibration", "verify_alignment_card_image", "verify_alignment_card_instruction", self.alignment_step[profile_key])
        self.fd["print_calibration"].verify_print_alignment_step()
        self.fd["traffic_director"].click_view_animations_button()
        # For alignment, only verify carousal dot if i > 1
        self._verify_animation_cards(
            "print_calibration",
            "verify_animation_card_step",
            "verify_card_instructions",
            self.alignment_animations_card[profile_key],
            spec_animation_data,
            step_key
        )
        self.fd["traffic_director"].click_watch_video_modal_close_button()
        self.fd["traffic_director"].click_next_btn()

    def navigate_hp_software_step(self, printer_profile):
        self.fd["hp_software"].verify_web_page()
        self.fd["traffic_director"].verify_veneer_stepper()
        self.fd["traffic_director"].verify_current_live_ui_step_in_sidebar(step='4')
        self.fd["hp_software"].verify_personal_use_hp_software_page(printer_profile)

    def navigate_connect_printer_to_usb_page(self):
        self.fd["connect_usb"].verify_web_page()
        self.fd["connect_usb"].verify_connect_usb_page()
        self.fd["traffic_director"].verify_veneer_stepper()
        self.fd["traffic_director"].click_next_btn()
        self.fd["traffic_director"].click_next_btn()

    def navigate_driver_download_page(self):
        self.fd["driver_download"].verify_web_page()
        self.fd["driver_download"].verify_driver_download_card()
        self.fd["traffic_director"].verify_veneer_stepper()
        self.fd["traffic_director"].click_next_btn()
        self.fd["driver_download"].verify_web_page(sub_url="driver-after")
        self.fd["driver_download"].verify_driver_after_page()
        self.fd["driver_download"].verify_hp_support_link()

    def navigate_unsupported_os_page(self):
        self.fd["unsupported_os"].verify_web_page()
        self.fd["traffic_director"].verify_veneer_stepper()
        self.fd["traffic_director"].verify_current_live_ui_step_in_sidebar(step='7')
        self.fd["unsupported_os"].verify_unsupported_os_page()

    def _normalize_profile(self, profile):
        """Normalize printer profile to base name for dictionary lookups"""
        if profile.startswith("MarconiBase"):
            return "marconi_base"
        elif profile.startswith("MarconiHi"):
            return "marconi_hi"
        elif profile.startswith("Moreto"):
            return "moreto"
        elif profile.startswith("VictoriaBase"):
            return "victoria_base"
        elif profile.startswith("VictoriaPlus"):
            return "victoria_plus"
        elif profile.startswith("Elion"):
            return "kebin"
        elif profile.startswith("Eddington"):
            return "kebin"
        elif profile.startswith(("Trillium", "trillium")):
            return "trillium"
        else:
            raise ValueError(f"Unknown printer profile prefix in '{profile}'")
        
    def _get_step_keys(self, spec_animation_data, step):
        """Extract and return sorted step keys from spec animation data based on the given prefix"""
        step_keys = []
        for key in spec_animation_data.keys():
            if step in key:
                step_keys.append(key)
        return step_keys