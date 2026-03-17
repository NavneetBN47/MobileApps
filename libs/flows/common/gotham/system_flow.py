from MobileApps.libs.flows.common.gotham.system_preferences import SystemPreferences
from time import sleep
import logging
import random

class SystemFlow(object):

    def __init__(self, driver):
        '''
        This is initial method for class.
        :parameter:
        :return:
        '''
        self.driver = driver
        self.sp = SystemPreferences(driver)

    def select_printer_on_win_settings(self,value_name=False):          
        self.sp.verify_ps_big_plus_btn()
        self.sp.click_ps_big_plus_btn()
        self.sp.verify_ps_progress_bar()
        if value_name:
            self.sp.click_ps_printer_list_item_by_name(value_name)    
            self.sp.click_ps_add_device_btn() 
            self.sp.verify_ps_printer_ready_text()
        else:
            self.sp.click_ps_printer_list_item()
            printer_info=self.sp.get_printer_info_text()
            self.sp.click_ps_add_device_btn()
            return printer_info          

    def get_app_on_win_settings(self):
        self.select_printer_on_win_settings()
        for _ in range(2):
            if self.sp.verify_ps_get_app_btn() is False:
                self.select_printer_on_win_settings()
            else:
                self.sp.click_ps_get_app_btn()
                break

    def launch_app_on_settings(self):
        self.sp.verify_ps_open_printer_app_btn()
        self.sp.click_ps_open_printer_app_btn()

    def launch_app_on_win_settings(self):
        printer_info=self.select_printer_on_win_settings()
        if self.sp.verify_ps_popup_add_btn() :
            self.sp.click_ps_popup_add_btn()
        for _ in range(2):
            if self.sp.verify_ps_open_printer_app_btn(raise_e=False) is False:
                printer_info=self.select_printer_on_win_settings()
            else:
                self.sp.click_ps_open_printer_app_btn()
                break
        return printer_info

    def search_app_on_mircosoft_store(self, search_app):
        self.sp.verify_ms_display()
        self.sp.click_ms_apps_item()
        self.sp.edit_ms_search_box(search_app)

    def launch_app_on_mircosoft_store(self):
        if self.sp.verify_ms_retry_btn():
            self.sp.click_ms_retry_btn()
        if self.sp.click_ms_open_btn() is False:
            self.sp.click_ms_get_btn()
            self.sp.verify_ms_progress_ring()
            self.sp.click_ms_open_btn()

    def launch_app_on_win_start(self):
        if self.sp.verify_win_start_display() is False:
            self.sp.extend_win_start_list()
        self.sp.click_win_app_head_letter()
        self.sp.click_win_h_app_letter()
        self.sp.click_win_hp_app_item()

    def launch_app_on_toast_message(self):
        self.sp.verify_win_toast_message()
        sleep(2)
        self.sp.click_toast_message_launch_btn()

    def install_app_on_123_hp_web(self, printer_num):
        self.sp.verify_123_hp_webpage()
        self.sp.enter_printer_name(printer_num)
        if self.sp.verify_printer_name_list():
            self.sp.select_a_printer()
            self.sp.click_web_next_btn()
        self.sp.verify_install_hp_smart_webpage()
        self.sp.click_web_install_hp_smart_btn()
        if self.sp.verify_open_ms_dialog():
            self.sp.click_web_open_ms_btn()

    def change_pc_region_to_flip_region(self, region=None):
        """
        Change PC region to one of the Flip region (HongKong/Singapore)
        """
        logging.info("Set PC region to SGP/HK")
        region_list =[104, 215]
        if region is None:
            self.driver.ssh.send_command('Set-WinHomeLocation -GeoId {}'.format(random.choice(region_list)))
        else:
            self.driver.ssh.send_command('Set-WinHomeLocation -GeoId {}'.format(region))

    def change_pc_region_to_non_hpc_region(self):
        """
        Change PC region to Vatican City region 
        """
        logging.info("Set PC region to Vatican City")
        self.driver.ssh.send_command('Set-WinHomeLocation -GeoId 253')

    def change_pc_region_to_us_region(self):
        """
        Change PC region to one of the United States region
        """
        logging.info("Set PC region to United States")
        self.driver.ssh.send_command('Set-WinHomeLocation -GeoId 244')
           
    def microsoft_login(self, username=None, password=None):
        """
        Login microsoft account
        """
        if self.sp.verify_ms_username_dialog():
            # Enter microsoft username
            self.sp.edit_ms_username(username)
            self.sp.click_ms_next_btn()    
        elif self.sp.verify_ms_continue_dialog():
            # The microsoft account is logged in
            self.sp.click_ms_account_item()
            self.sp.click_ms_continue_btn()
        # Enter microsoft password
        self.sp.verify_ms_password_dialog()
        self.sp.edit_ms_password(password)
        self.sp.click_ms_sign_in_btn()
        if self.sp.verify_ms_last_dialog():
            self.sp.click_ms_next_btn()

    def reset_system_time(self, add_years=1, time_back=True):
        if time_back:
            current_time = self.driver.ssh.send_command('(Get-Date).Year')['stdout'].strip()
            sleep(2)
            change_time = self.driver.ssh.send_command('Set-date -Date (Get-Date).AddYears(-{})'.format(add_years))['stdout']     
            sleep(2)
            check_time = str(int(current_time)-int(add_years))
        else:
            current_time = self.driver.ssh.send_command('(Get-Date).Year')['stdout'].strip()
            sleep(2)
            change_time = self.driver.ssh.send_command('Set-date -Date (Get-Date).AddYears(+{})'.format(add_years))['stdout']     
            sleep(2)
            check_time = str(int(current_time)+int(add_years))
        assert check_time in change_time

    def settings_and_store_cleanup(self):
        """
        Clean up Win Settings \ Microsoft Store.
        """
        self.driver.ssh.send_command('Stop-Process -Name "*SystemSettings*"')
        sleep(2)
        self.driver.ssh.send_command('Stop-Process -Name "*Store*"')
        sleep(2)
