import json
from SAF.misc import saf_misc
from MobileApps.libs.ma_misc import ma_misc
import MobileApps.resources.const.windows.const as w_const

class PropertyUtilities:
    def __init__(self, ssh_client):
        self.ssh = ssh_client

    def load_simulate_file(self, file_path):
        file_content = saf_misc.load_json(file_path)
        return file_content
    
    def copy_simulate_file(self):
        file_content = self.load_simulate_file(ma_misc.get_abs_path("/resources/test_data/hpx_rebranding/support/properties.json"))
        hp_support = file_content

        remote_path = "{}\\{}\\LocalState\\properties.json".format(w_const.TEST_DATA.PACKAGES_PATH, w_const.PACKAGE_NAME.HPX)
        fh = self.ssh.remote_open(remote_path, "w+")
        json.dump(hp_support, fh)      
        fh.close()

    def set_featureflags(self, flag_dict):
        file_content = self.load_simulate_file(ma_misc.get_abs_path("/resources/test_data/hpx_rebranding/support/properties.json"))
        hp_support = file_content
        for key, value in flag_dict.items():
            hp_support['@hp-af/feature-switch/overrides'][key] = value
        
        remote_path = "{}\\{}\\LocalState\\properties.json".format(w_const.TEST_DATA.PACKAGES_PATH, w_const.PACKAGE_NAME.HPX)
        fh = self.ssh.remote_open(remote_path, "w+")
        json.dump(hp_support, fh)      
        fh.close()

    def simulate_device(self):
        self.driver.ssh.send_command("C:/HPXUpdate_PRO/Release/SqliteDBSimulator.exe '@hp-af/device-info/devices' '\"[{\\\"id\\\":\\\"5CD2167ZJF\\\",\\\"deviceType\\\":\\\"PC\\\",\\\"serialNumber\\\":\\\"5CD2167ZJF\\\",\\\"description\\\":\\\"\\\",\\\"detailData\\\":{\\\"featureName\\\":\\\"pcdevice-core\\\",\\\"modelName\\\":\\\"Simulate\\\"},\\\"warranty\\\":{\\\"status\\\":\\\"Unknown\\\",\\\"endDate\\\":\\\"\\\"},\\\"firmwareVersion\\\":\\\"\\\",\\\"productNumber\\\":\\\"61K71AA#ABA\\\",\\\"friendlyName\\\":\\\"Simulate\\\",\\\"mfePath\\\":\\\"/pcdevicedetails\\\"}]\"'")