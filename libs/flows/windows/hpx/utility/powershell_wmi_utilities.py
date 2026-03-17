import json
import re

class PowershellWmiUtilities(object):
    def __init__(self, ssh_client):
        self.ssh = ssh_client

    def _run_ps(self, ps_command):
        # Run a PowerShell command via SSH and return parsed output
        result = self.ssh.send_command(f'powershell -Command "{ps_command}"')
        return result["stdout"].strip()

    def get_serial_number(self):
        ps = "Get-CimInstance -ClassName Win32_BIOS | Select-Object -ExpandProperty SerialNumber"
        return self._run_ps(ps)

    def get_product_number(self):
        ps = "Get-CimInstance -ClassName Win32_ComputerSystem | Select-Object -ExpandProperty SystemSKUNumber"
        return self._run_ps(ps)

    def get_product_name(self):
        ps = "Get-CimInstance -ClassName Win32_ComputerSystem | Select-Object -ExpandProperty Model"
        return self._run_ps(ps)

    def is_grogu(self):
        ps = "Get-WmiObject -Namespace root\\HP\\InstrumentedBIOS -Class HP_BIOSSetting | Where-Object {$_.name -eq 'Feature Byte'} | Select-Object -ExpandProperty value"
        out = self._run_ps(ps)
        return "r6" in out.lower()

    def get_os_caption_and_architecture(self):
        ps = "Get-CimInstance -ClassName Win32_OperatingSystem | Select-Object Caption,OSArchitecture | ConvertTo-Json"
        out = self._run_ps(ps)
        try:
            data = json.loads(out)
            return data['Caption'], data['OSArchitecture']
        except Exception:
            return None, None

    def get_processor_name(self):
        ps = "Get-CimInstance -ClassName Win32_Processor | Select-Object -ExpandProperty Name"
        return self._run_ps(ps)

    def get_physical_memory_info(self):
        ps = "Get-CimInstance -ClassName Win32_PhysicalMemory | Select-Object Capacity,Manufacturer,ConfiguredClockSpeed | ConvertTo-Json"
        out = self._run_ps(ps)
        try:
            data = json.loads(out)
            if isinstance(data, dict):
                return [data]
            return data
        except Exception:
            return []

    def get_baseboard_product_and_version(self):
        ps = "Get-CimInstance -ClassName Win32_BaseBoard | Select-Object Product,Version | ConvertTo-Json"
        out = self._run_ps(ps)
        try:
            data = json.loads(out)
            if isinstance(data, dict):
                return data['Product'], data['Version']
            return data[0]['Product'], data[0]['Version']
        except Exception:
            return None, None

    def get_smbios_bios_version(self):
        ps = "Get-CimInstance -ClassName Win32_BIOS | Select-Object -ExpandProperty SMBIOSBIOSVersion"
        return self._run_ps(ps)

    def get_video_controller_info(self):
        ps = "Get-CimInstance -ClassName Win32_VideoController | Select-Object Caption,CurrentHorizontalResolution,CurrentVerticalResolution,CurrentRefreshRate,DriverDate,DriverVersion | ConvertTo-Json"
        out = self._run_ps(ps)
        try:
            data = json.loads(out)
            if isinstance(data, dict):
                return [data]
            return data
        except Exception:
            return []

    def get_sound_device_and_driver_info(self):
        ps_sound = "Get-CimInstance -ClassName Win32_SoundDevice | Select-Object ProductName,ConfigManagerErrorCode,PNPDeviceID | ConvertTo-Json"
        ps_driver = "Get-CimInstance -ClassName Win32_PnPSignedDriver | Select-Object DeviceID,DriverName,DriverVersion | ConvertTo-Json"
        out_sound = self._run_ps(ps_sound)
        out_driver = self._run_ps(ps_driver)
        try:
            sound_devices = json.loads(out_sound)
            drivers = json.loads(out_driver)
            if isinstance(sound_devices, dict):
                sound_devices = [sound_devices]
            if isinstance(drivers, dict):
                drivers = [drivers]
            for device in sound_devices:
                pnp_id = device.get('PNPDeviceID')
                match = next((d for d in drivers if d.get('DeviceID') == pnp_id), None)
                if match:
                    device['DriverName'] = match.get('DriverName')
                    device['DriverVersion'] = match.get('DriverVersion')
                else:
                    device['DriverName'] = None
                    device['DriverVersion'] = None
            return sound_devices
        except Exception:
            return []
