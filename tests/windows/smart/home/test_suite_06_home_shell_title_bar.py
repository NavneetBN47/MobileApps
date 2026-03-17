import pytest

pytest.app_info = "GOTHAM"
class Test_Suite_06_Home_Shell_Title_Bar(object):
    @pytest.fixture(scope="class", autouse="true")
    def class_setup(cls, request, windows_smart_setup):
        cls = cls.__class__
        cls.driver, cls.fc = windows_smart_setup

        cls.home = cls.fc.fd["home"]
        cls.gotham_utility = cls.fc.fd["gotham_utility"]

        cls.stack = request.config.getoption("--stack")

    def test_01_check_minimize_icon(self):
        """
        Click minimize/maximize/close icons on title bar, verify functionality

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/19447352
        """    
        self.fc.go_home()
        self.gotham_utility.click_minimize()
        assert "HP.Smart" in self.driver.ssh.send_command('Get-Process -Name "*HP.Smart*"')["stdout"]

    def test_02_check_maximize_icon(self):
        """
        Click minimize/maximize/close icons on title bar, verify functionality

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/19447352
        """
        self.driver.launch_app()
        self.home.verify_home_screen()
        if not self.gotham_utility.verify_window_visual_state_maximized():
            self.gotham_utility.click_maximize()
        assert self.gotham_utility.verify_window_visual_state_maximized() is True 
        self.gotham_utility.click_maximize()
        assert self.gotham_utility.verify_window_visual_state_maximized() is False 

    def test_03_check_close_icon(self):
        """
        Click minimize/maximize/close icons on title bar, verify functionality

        TestRails -> https://hp-testrail.external.hp.com/index.php?/cases/view/19447352
        """
        self.gotham_utility.click_close()
        assert "HP.Smart" not in self.driver.ssh.send_command('Get-Process -Name "*HP.Smart*"')["stdout"]

        
