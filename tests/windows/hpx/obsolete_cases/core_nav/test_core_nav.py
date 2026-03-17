import logging
from MobileApps.libs.ma_misc import ma_misc
from MobileApps.libs.flows.windows.hpx.flow_container import FlowContainer
import MobileApps.libs.ma_misc.conftest_misc as c_misc
import pytest
import time 
import re
from MobileApps.libs.flows.windows.hpx.system_flow import SystemFlow

pytest.app_info = "DESKTOP"
pytest.set_info = "HPX"

class Test_Suite_Core_Nav(object):

    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, windows_test_setup):
        cls = cls.__class__
        cls.driver= windows_test_setup
        cls.fc = FlowContainer(cls.driver)
        cls.sf = SystemFlow(cls.driver)
        cls.sys_config = ma_misc.load_system_config_file()
        cls.fc.launch_myHP()
        time.sleep(3)
        cls.fc.restart_myHP()

    @pytest.mark.require_sanity_check(["sanity"])
    def test_01_Verify_myHP_app_install_with_msixbundle_C32600360(self):
        time.sleep(8)
        is_install = self.fc.is_myHP_installed()
        assert is_install == True
        logging.info("App is installed = "+str(is_install))

    @pytest.mark.require_sanity_check(["sanity"])
    def test_02_verify_myHP_app_from_start_C38142203(self):
        self.sf.click_start_btn()
        self.sf.input_text_in_search_box("myHP")
        time.sleep(2)
        assert self.sf.verify_open_btn_on_HP_app() is True
        self.sf.click_myHP_app_On_Start_To_Open()
        time.sleep(10)
        assert bool(self.fc.fd["navigation_panel"].verify_welcome_module_show()) is True
        assert bool(self.fc.fd["navigation_panel"].verify_support_module_show()) is True
        assert bool(self.fc.fd["navigation_panel"].verify_pcdevice_module_show()) is True
       
    def test_03_verify_myHP_version_C38142196(self,request):
        version_json=self.driver.ssh.send_command('get-appxpackage *myHP* | select Version',  raise_e=False, timeout=10)
        app_url, zip_name = c_misc.get_package_url(request, _os="WINDOWS", project=pytest.default_info)
        result = re.search("([0-9]{1,5}\\.[0-9]{1,5}\\.[0-9]{1,5}\\.[0-9]{1,5})", str(version_json))
        install_build_version=result.group(1)
        logging.info("installed build version = "+str(install_build_version))
        pipeline_build_match=re.search("([0-9]{1,5}\\.[0-9]{1,5}\\.[0-9]{1,5}\\.[0-9]{1,5})", str(zip_name))
        pipeline_build_version=pipeline_build_match.group(1)
        logging.info("pipeline_build_match= "+str(pipeline_build_version))
        assert  install_build_version==pipeline_build_version,"build version not matched"

    def test_04_verify_top_nav_bar_C32600362(self):
        time.sleep(2)
        self.fc.fd["sanity_check"].click_bell_icon()
        self.fc.fd["sanity_check"].verify_notfication_tips_show()

        assert self.fc.fd["sanity_check"].get_notfications_tips_text() == "Notifications"
        assert self.fc.fd["sanity_check"].get_new_message_text() == "No new messages!"
        assert bool(self.fc.fd["hp_login"].verify_profile_icon_show()) is True
