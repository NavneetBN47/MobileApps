import pytest
from MobileApps.libs.flows.windows.hpx.flow_container import FlowContainer
from MobileApps.libs.flows.windows.hpx.utility.soft_assert import SoftAssert
import time

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"

class Test_Suite_Context_Aware(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, windows_test_setup):
        cls = cls.__class__
        cls.driver = windows_test_setup
        cls.fc = FlowContainer(cls.driver)
        if request.config.getoption("--ota-test") is not None:
            time.sleep(10)
            cls.fc.fd["home"].click_to_install_signed_build()
            time.sleep(60)
            cls.fc.launch_myHP()
            time.sleep(5)
            cls.fc.ota_app_after_update()

    
    #select a device and update everyday will not be issue.(rex only)
    @pytest.mark.ota
    def test_01_upgrade_dashopenapps_C50510240(self):
        time.sleep(3)
        self.driver.ssh.send_command('schtasks /Run /TN "Run Windows Update when idle"',  raise_e=False, timeout=20)
    
    #check the drivers of system to run OTA
    @pytest.mark.ota
    def test_02_upgrade_dashopenapps_C50510240(self):
        #cmd for device HPA driver and HP enabling driver
        driver_command = ('Get-WmiObject Win32_PnPSignedDriver | Where-Object { $_.Manufacturer -like "*HP*" -and ($_.FriendlyName -eq "HP Device Health Service" -or $_.FriendlyName -eq "HP Application Enabling Services") } | Select-Object FriendlyName, DriverVersion')
        #cmd for OS version
        os_command = 'wmic os get version'
        driver_result = self.driver.ssh.send_command(driver_command)
        driver_output = driver_result.get("stdout", "")
        os_result = self.driver.ssh.send_command(os_command)
        os_output = os_result.get("stdout", "")
        print("HP Driver Information:")
        print(driver_output.strip())
        print("\nOS Version:")
        print(os_output.strip())

    #run OTA tc to check all moduule present
    @pytest.mark.require_sanity_check(["sanity"])
    @pytest.mark.ota
    def test_03_upgrade_dashopenapps_C50510239(self):
        self.fc.launch_myHP()
        self.fc.fd["navigation_panel"].verify_navigationicon_show()
        assert bool(self.fc.fd["navigation_panel"].verify_pc_device_show()) is True, "PC Device is not visible on left panel."
        self.fc.fd["navigation_panel"].navigate_to_pc_device()
        assert bool(self.fc.fd["devices"].verify_programmable_key()) is True, "HPPK is not invisible"
        assert bool(self.fc.fd["devices"].verify_battery_manager_card()) is True, "Battery manager is invisible"
        assert bool(self.fc.fd["devices"].verify_energy_consumption_card()) is True, "Energy Consumption is invisible"
        assert bool(self.fc.fd["devices"].verify_support_module_on_pc_device()) is True, "Support module is invisible"
        self.fc.close_myHP()
