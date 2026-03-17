import time
from MobileApps.libs.ma_misc import ma_misc
from SAF.misc import saf_misc
from MobileApps.libs.flows.common.gotham.flow_container import FlowContainer
import pytest

pytest.app_info = "GOTHAM"
class Test_Suite_01_Scan(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, windows_test_setup, utility_web_session):
        cls = cls.__class__
        cls.driver = windows_test_setup
        cls.web_driver = utility_web_session
        cls.fc = FlowContainer(cls.driver)

    def test_01_sample(self):
        import pdb 
        pdb.set_trace()
        time.sleep(1)