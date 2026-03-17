from MobileApps.libs.flows.ios.jweb_doc_provider.home import Home
from MobileApps.libs.flows.ios.jweb_doc_provider.weblet import Weblet
from MobileApps.libs.flows.ios.jweb_doc_provider.doc_provider import DocProvider
from MobileApps.libs.flows.ios.smart.files import Files
from MobileApps.libs.flows.web.jweb.doc_provider_plugin import DocProviderPlugin
from MobileApps.resources.const.web import const as w_const
from MobileApps.resources.const.ios import const as i_const

class FlowContainer(object):
    def __init__(self, driver, load_app_strings=False):
        self.driver = driver
        self.fd = {"home": Home(driver),
                   "files": Files(driver),
                   "weblet": Weblet(driver),
                   "doc_provider": DocProvider(driver),
                   "web_doc_provider": DocProviderPlugin(driver, context={'url': w_const.WEBVIEW_URL.JWEB})}

    @property
    def flow(self):
        return self.fd

    # *********************************************************************************
    #                                ACTION FLOWS                                     *
    # *********************************************************************************

    #   -----------------------         FROM HOME       -----------------------------
    def flow_load_home_screen(self):
        """
        Load to Home screen:
            -Launch JWeb Doc Provider App
        """
        for i in range(3):
            self.driver.restart_app(i_const.BUNDLE_ID.JWEB_DOC_PROVIDER)
            if self.fd['home'].verify_doc_provider_open() is True:
                return True
        return False