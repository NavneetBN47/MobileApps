
class WmiUtilities(object):

    def __init__(self, ssh_client):
        self.ssh = ssh_client

    """
        -wmic BIOS get serialnumber
    """
    def get_serial_number(self):
        result = self.ssh.send_command("wmic BIOS get serialnumber")
        out = result["stdout"].replace("SerialNumber", "")
        out = out.replace('\r', '').replace('\n', '')
        out = out.strip()
        return out

    """
        -wmic computerSystem get SystemSKUNumber
    """
    def get_product_number(self):
        result = self.ssh.send_command("wmic computerSystem get SystemSKUNumber")
        out = result["stdout"].replace("SystemSKUNumber", "")
        out = out.replace("\r", "").replace("\n", "")
        out = out.strip()
        return out

    """
        -wmic computerSystem get Model
    """
    def get_product_name(self):
        result = self.ssh.send_command("wmic computerSystem get Model")
        out = result["stdout"].replace("Model", "")
        out = out.replace("\r", "").replace("\n", "")
        out = out.strip()
        return out

    """
        -wmic ComputerSystem get OEMStringArray to judge if grogu machne
    """
    def is_grogu(self):
        result = self.ssh.send_command("Get-WmiObject -Namespace root\\HP\\InstrumentedBIOS -Class HP_BIOSSetting | where-object name -eq 'Feature Byte'| select value", raise_e=False)
        if result:
            out = result["stdout"].strip().replace("value", "").strip().replace("-----", "").strip()
            print(out)
            if "r6" in out: 
                return True 
            else: 
                return False
        else:
            return False

    """
        -wmic os get Caption,OSArchitecture
    """
    def get_os_caption_and_architecture(self):
        """
        Get the Windows OS Caption and OSArchitecture using wmic.
        Returns:
            (caption, architecture): Tuple of strings.
        """
        result = self.ssh.send_command('wmic os get Caption,OSArchitecture /format:csv')
        lines = result["stdout"].strip().splitlines()
        # Skip header, find the first non-header line with data
        for line in lines[1:]:
            parts = line.split(',')
            if len(parts) >= 3:
                # Format: Node,Caption,OSArchitecture
                caption = parts[1].strip()
                architecture = parts[2].strip()
                return caption, architecture
        return None, None
    
    """
        -wmic cpu get Name
    """
    def get_processor_name(self):
        """
        Get the processor name using WMI.
        Returns:
            name (str): The processor name, or None if not found.
        """
        result = self.ssh.send_command('wmic cpu get Name')
        out = result["stdout"].replace("Name", "").replace('\r', '').replace('\n', '').strip()
        return out if out else None

    """
        -wmic memorychip get Capacity,Manufacturer,ConfiguredClockSpeed
    """
    def get_physical_memory_info(self):
        """
        Get Capacity, Manufacturer, and ConfiguredClockSpeed for each physical memory module.
        Returns:
            List of dicts: [{'Capacity': ..., 'Manufacturer': ..., 'ConfiguredClockSpeed': ...}, ...]
        """
        result = self.ssh.send_command('wmic memorychip get Capacity,Manufacturer,ConfiguredClockSpeed /format:csv')
        lines = result["stdout"].strip().splitlines()
        if len(lines) < 2:
            return []
        headers = [h.strip() for h in lines[0].split(',')]
        memory_info = []
        for line in lines[1:]:
            if not line.strip():
                continue
            parts = [p.strip() for p in line.split(',')]
            if len(parts) != len(headers):
                continue
            info = dict(zip(headers, parts))
            memory_info.append(info)
        return memory_info
    
    """
        - wmic baseboard get Product,Version
    """
    def get_baseboard_product_and_version(self):
        """
        Get the motherboard (baseboard) Product and Version using WMI.
        Returns:
            (product, version): Tuple of strings, or (None, None) if not found.
        """
        result = self.ssh.send_command('wmic baseboard get Product,Version /format:csv')
        lines = result["stdout"].strip().splitlines()
        # Skip header, find the first non-header line with data
        for line in lines[1:]:
            parts = line.split(',')
            if len(parts) >= 3:
                # Format: Node,Product,Version
                product = parts[1].strip()
                version = parts[2].strip()
                return product, version
        return None, None
    
    """
        - wmic bios get SMBIOSBIOSVersion
    """
    def get_smbios_bios_version(self):
        """
        Get the SMBIOS BIOS Version using WMI.
        Returns:
            smbios_version (str): The SMBIOS BIOS Version, or None if not found.
        """
        result = self.ssh.send_command('wmic bios get SMBIOSBIOSVersion /format:csv')
        lines = result["stdout"].strip().splitlines()
        # Skip header, find the first non-header line with data
        for line in lines[1:]:
            parts = line.split(',')
            if len(parts) >= 2:
                # Format: Node,SMBIOSBIOSVersion
                smbios_version = parts[1].strip()
                return smbios_version
        return None
    
    """
        - wmic path Win32_VideoController get Caption,CurrentHorizontalResolution,CurrentVerticalResolution,CurrentRefreshRate,DriverDate,DriverVersion
    """
    def get_video_controller_info(self):
        """
        Get video controller info: Caption, CurrentHorizontalResolution, CurrentVerticalResolution,
        CurrentRefreshRate, DriverDate, DriverVersion using WMI.
        Returns:
            List of dicts: [{'Caption': ..., 'CurrentHorizontalResolution': ..., ...}, ...]
        """
        result = self.ssh.send_command(
            'wmic path Win32_VideoController get Caption,CurrentHorizontalResolution,CurrentVerticalResolution,CurrentRefreshRate,DriverDate,DriverVersion /format:csv'
        )
        lines = result["stdout"].strip().splitlines()
        if len(lines) < 2:
            return []
        headers = [h.strip() for h in lines[0].split(',')]
        video_info = []
        for line in lines[1:]:
            if not line.strip():
                continue
            parts = [p.strip() for p in line.split(',')]
            if len(parts) != len(headers):
                continue
            info = dict(zip(headers, parts))
            video_info.append(info)
        return video_info
    
    """
        - wmic sounddev get ProductName,ConfigManagerErrorCode,PNPDeviceID
    """
    def get_sound_device_and_driver_info(self):
        """
        Get sound device info and its driver info by matching PNPDeviceID with DeviceID.
        Returns:
            List of dicts: [{
                'ProductName': ...,
                'ConfigManagerErrorCode': ...,
                'PNPDeviceID': ...,
                'DriverName': ...,
                'DriverVersion': ...
            }, ...]
        """
        # Step 1: Get sound devices
        sound_result = self.ssh.send_command(
            'wmic sounddev get ProductName,ConfigManagerErrorCode,PNPDeviceID /format:csv'
        )
        sound_lines = sound_result["stdout"].strip().splitlines()
        if len(sound_lines) < 2:
            return []
        sound_headers = [h.strip() for h in sound_lines[0].split(',')]
        sound_devices = []
        for line in sound_lines[1:]:
            if not line.strip():
                continue
            parts = [p.strip() for p in line.split(',')]
            if len(parts) != len(sound_headers):
                continue
            sound_devices.append(dict(zip(sound_headers, parts)))

        # Step 2: Get signed drivers
        driver_result = self.ssh.send_command(
            'wmic path Win32_PnPSignedDriver get DeviceID,DriverName,DriverVersion /format:csv'
        )
        driver_lines = driver_result["stdout"].strip().splitlines()
        if len(driver_lines) < 2:
            return sound_devices  # Return sound devices without driver info if none found
        driver_headers = [h.strip() for h in driver_lines[0].split(',')]
        drivers = []
        for line in driver_lines[1:]:
            if not line.strip():
                continue
            parts = [p.strip() for p in line.split(',')]
            if len(parts) != len(driver_headers):
                continue
            drivers.append(dict(zip(driver_headers, parts)))

        # Step 3: Match PNPDeviceID with DeviceID and add driver info
        for device in sound_devices:
            pnp_id = device.get('PNPDeviceID')
            for driver in drivers:
                if driver.get('DeviceID') == pnp_id:
                    device['DriverName'] = driver.get('DriverName')
                    device['DriverVersion'] = driver.get('DriverVersion')
                    break
            else:
                device['DriverName'] = None
                device['DriverVersion'] = None

        return sound_devices