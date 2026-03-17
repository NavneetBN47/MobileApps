import re
import time

class VcosmosUtilities:

    def __init__(self, ssh_client):
        self.ssh = ssh_client

    def get_the_file_path(self):
        command = """
        $path = Get-ChildItem "C:\\TestAutomation\\Clients\\" -Recurse -Filter "*CURRENT_INITIALIZATION*" | Select-Object -ExpandProperty FullName;
        if ($null -eq $path) { Write-Error "No files found matching *CURRENT_INITIALIZATION*" };
        $parentDir = (Split-Path $path -Parent | Split-Path -Leaf);
        $fileName = (Split-Path $path -Leaf).Replace("_CURRENT_INITIALIZATION", "");
        $parentDir, $fileName
        """
        result = self.ssh.send_command(command)
        if isinstance(result, dict):
            result = result.get('stdout', '').strip() 

        if result:
            try:
                parent_dir, file_name = result.split()
                return parent_dir, file_name
            except ValueError:
                print("Error: Unexpected result format. Could not split result.")
                return None, None
        else:
            print("No result returned from command.")
            return None, None

    def verify_led_values(self):
        parent_dir, file_name = self.get_the_file_path()
        if parent_dir is None or file_name is None:
            raise ValueError("Failed to retrieve valid parent_dir or file_name.")
        remote_artifact_path = f'C:\\TestAutomation\\Clients\\'+parent_dir+'\\'+file_name+'_CURRENT_INITIALIZATION\\'
        sftp_client = self.ssh.client.open_sftp()
        files = sftp_client.listdir(remote_artifact_path)
        matching_files = [f for f in files if f.startswith(file_name) and f.endswith('.log')]

        if matching_files:
            remote_file_path = remote_artifact_path + matching_files[-1]
            remote_file = sftp_client.open(remote_file_path, 'rb')
            reading_log = remote_file.read()
            pattern = b"VERIFY_LED - LED sensor values - Red:(\d+), Green:(\d+), Blue:(\d+), Clear:(\d+)"
            matches = re.findall(pattern, reading_log)

            if matches:
            # Extract the last match
                last_match = matches[-1]
                red = last_match[0].decode('utf-8')
                green = last_match[1].decode('utf-8')
                blue = last_match[2].decode('utf-8')
                clear = last_match[3].decode('utf-8')

                return red, green, blue, clear
            else:
                print("No LED values found in the log.")
                return None, None, None, None
        else:
            print("No log files found matching the pattern.")
            return None, None, None, None
  
    def clean_up_logs(self):
        parent_dir, file_name = self.get_the_file_path()
        if parent_dir is None or file_name is None:
            print("Failed to retrieve valid parent_dir or file_name.")
        # else:
        #     command = ('Remove-Item "C:\\TestAutomation\\Clients\\'+parent_dir+'\\'+file_name+'0*" -Recurse -Force')
        #     self.ssh.send_command(command)

    def get_red_green_blue_clear_value(self):
        self.ssh.send_command('cmd.exe /c "C:\\Users\\exec\\verify_rgbc.bat"', timeout=300)

    def add_charger_and_usb(self):
        self.ssh.send_command('cmd.exe /c "C:\\Users\\exec\\add_charger_and_usb.bat"', timeout=200)
        time.sleep(40)

    def remove_charger_and_usb(self):
        self.ssh.send_command('cmd.exe /c "C:\\Users\\exec\\remove_charger_and_usb.bat"', timeout=200)
        time.sleep(40)

    def add_3_5_headphone(self):
        self.ssh.send_command('cmd.exe /c "C:\\Users\\exec\\add_3_5_headphone.bat"', timeout=150)

    def remove_3_5_headphone(self):
        self.ssh.send_command('cmd.exe /c "C:\\Users\\exec\\remove_3_5_headphone.bat"', timeout=150)

    def press_mute_button(self):
        self.ssh.send_command('cmd.exe /c "C:\\Users\\exec\\press_mute_button.bat"', timeout=150)
        time.sleep(40)

    def press_decrease_brightness_button(self):
        self.ssh.send_command('cmd.exe /c "C:\\Users\\exec\\press_decrease_brightness_button.bat"', timeout=150)
        time.sleep(40)
    
    def press_f11_hppk_key(self):
        self.ssh.send_command('cmd.exe /c "C:\\Users\\exec\\press_F11_HPPK.bat"', timeout=150)
        time.sleep(40)

    def press_hppk_key0(self):
        self.ssh.send_command('cmd.exe /c "C:\\Users\\exec\\Press_HPPK_Key_0.bat"', timeout=150)
        time.sleep(40)
    
    def press_hppk_key1(self):
        self.ssh.send_command('cmd.exe /c "C:\\Users\\exec\\Press_HPPK_Key_1.bat"', timeout=150)
        time.sleep(40)

    def press_hppk_key2(self):
        self.ssh.send_command('cmd.exe /c "C:\\Users\\exec\\Press_HPPK_Key_2.bat"', timeout=150)
        time.sleep(40)

    def press_hppk_key3(self):
        self.ssh.send_command('cmd.exe /c "C:\\Users\\exec\\Press_HPPK_Key_3.bat"', timeout=150)
        time.sleep(40)  

    def introduce_pen(self):
        self.ssh.send_command('cmd.exe /c "C:\\Users\\exec\\pen_introduction.bat"', timeout=150)
        time.sleep(40)

    def restore_factory_default(self):
        self.ssh.send_command('cmd.exe /c "C:\\Users\\exec\\Restore_Factory_Default.bat"', timeout=150)
        time.sleep(40)

    def navigate_gaming_mode(self):
        self.ssh.send_command('cmd.exe /c "C:\\Users\\exec\\Navigate_Gaming_Mode.bat"', timeout=150)
        time.sleep(40)
    
    def navigate_hp_enhance_mode(self):
        self.ssh.send_command('cmd.exe /c "C:\\Users\\exec\\Navigate_HP_Enhance_Mode.bat"', timeout=150)
        time.sleep(40)

    def navigate_movie_mode(self):
        self.ssh.send_command('cmd.exe /c "C:\\Users\\exec\\Navigate_Movie_Mode.bat"', timeout=150)
        time.sleep(40)

    def navigate_native_mode(self):
        self.ssh.send_command('cmd.exe /c "C:\\Users\\exec\\Navigate_Native_Mode.bat"', timeout=150)
        time.sleep(40)
    
    def navigate_neutral_mode(self):
        self.ssh.send_command('cmd.exe /c "C:\\Users\\exec\\Navigate_Neutral_Mode.bat"', timeout=150)
        time.sleep(40)
    
    def navigate_night_mode(self):
        self.ssh.send_command('cmd.exe /c "C:\\Users\\exec\\Navigate_Night_Mode.bat"', timeout=150)
        time.sleep(40)
    
    def navigate_reading_mode(self):
        self.ssh.send_command('cmd.exe /c "C:\\Users\\exec\\Navigate_Reading_Mode.bat"', timeout=150)
        time.sleep(40)

    def set_blue_value_fifty(self):
        self.ssh.send_command('cmd.exe /c "C:\\Users\\exec\\Set_Blue_Value_Fifty.bat"', timeout=150)
        time.sleep(40)

    def set_blue_value_zero(self):
        self.ssh.send_command('cmd.exe /c "C:\\Users\\exec\\Set_Blue_Value_Zero.bat"', timeout=150)
        time.sleep(40)

    def set_red_value_fifty(self):
        self.ssh.send_command('cmd.exe /c "C:\\Users\\exec\\Set_Red_Value_Fifty.bat"', timeout=150)
        time.sleep(40)

    def set_red_value_zero(self):
        self.ssh.send_command('cmd.exe /c "C:\\Users\\exec\\Set_Red_Value_Zero.bat"', timeout=150)
        time.sleep(40)

    def set_green_value_fifty(self):
        self.ssh.send_command('cmd.exe /c "C:\\Users\\exec\\Set_Green_Value_Fifty.bat"', timeout=150)
        time.sleep(40)

    def set_green_value_zero(self):
        self.ssh.send_command('cmd.exe /c "C:\\Users\\exec\\Set_Green_Value_Zero.bat"', timeout=150)
        time.sleep(40)

    def rapid_unplug(self):
        self.ssh.send_command('cmd.exe /c "C:\\Users\\exec\\rapid_unplug.bat"', timeout=150)

    def set_brightness_value_zero(self):
        self.ssh.send_command('cmd.exe /c "C:\\Users\\exec\\Set_Brightness_Value_Zero.bat"', timeout=150)
        time.sleep(40)

    def set_brightness_value_max(self):
        self.ssh.send_command('cmd.exe /c "C:\\Users\\exec\\Set_Brightness_Value_Max.bat"', timeout=150)
        time.sleep(40)

    def openlid_closelid(self):
        self.ssh.send_command('cmd.exe /c "C:\\Users\\exec\\openlid_closelid.bat"', timeout=150)
        time.sleep(40)

    def restore_factory_default_keelung32(self):
        self.ssh.send_command('cmd.exe /c "C:\\Users\\exec\\Restore_Factory_Defaults.bat"', timeout=150)
        time.sleep(40)

    def navigate_neutral_mode_keelung32(self):
        self.ssh.send_command('cmd.exe /c "C:\\Users\\exec\\Navigate_Modes_Neutral.bat"', timeout=150)
        time.sleep(40)

    def navigate_warm_mode_keelung32(self):
        self.ssh.send_command('cmd.exe /c "C:\\Users\\exec\\Navigate_Modes_Warm.bat"', timeout=150)
        time.sleep(40)

    def navigate_cool_mode_keelung32(self):
        self.ssh.send_command('cmd.exe /c "C:\\Users\\exec\\Navigate_Modes_Cool.bat"', timeout=150)
        time.sleep(40)

    def navigate_hp_enhance_mode_keelung32(self):
        self.ssh.send_command('cmd.exe /c "C:\\Users\\exec\\Navigate_Modes_HP_Enhance.bat"', timeout=150)
        time.sleep(40)

    def navigate_native_mode_keelung32(self):
        self.ssh.send_command('cmd.exe /c "C:\\Users\\exec\\Navigate_Modes_Native.bat"', timeout=150)
        time.sleep(40)

    def navigate_srgb_d65_mode_keelung32(self):
        self.ssh.send_command('cmd.exe /c "C:\\Users\\exec\\Navigate_Modes_sRGB.bat"', timeout=150)
        time.sleep(40)

    def navigate_bt709_d65_mode_keelung32(self):
        self.ssh.send_command('cmd.exe /c "C:\\Users\\exec\\Navigate_Modes_BT709.bat"', timeout=150)
        time.sleep(40)

    def switch_to_hdmi_input_keelung32(self):
        self.ssh.send_command('cmd.exe /c "C:\\Users\\exec\\Navigate_Input_HDMI.bat"', timeout=150)
        time.sleep(40)

    def switch_to_pc_input_keelung32(self):
        self.ssh.send_command('cmd.exe /c "C:\\Users\\exec\\Navigate_Input_PC.bat"', timeout=150)
        time.sleep(40)