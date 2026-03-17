from MobileApps.libs.flows.android.jweb_doc_provider.home import Home
from MobileApps.libs.flows.android.jweb_doc_provider.doc_provider_dev_settings import DocProviderDevSettings
from MobileApps.libs.flows.android.jweb_doc_provider.weblet import Weblet
from MobileApps.libs.flows.android.jweb_doc_provider.doc_provider import DocProvider
from MobileApps.libs.flows.android.smart.local_files import LocalFiles
from MobileApps.libs.flows.web.jweb.doc_provider_plugin import DocProviderPlugin
from MobileApps.resources.const.android.const import *
from MobileApps.resources.const.web.const import *


class FlowContainer(object):
    def __init__(self, driver):
        self.driver = driver
        self.fd = {"home": Home(driver),
                   "doc_provider_dev_settings": DocProviderDevSettings(driver),
                   "doc_provider": DocProvider(driver),
                   "weblet": Weblet(driver),
                   "web_doc_provider": DocProviderPlugin(driver, context={'url': WEBVIEW_URL.JWEB}),
                   "files": LocalFiles(driver)}

    @property
    def flow(self):
        return self.fd

    def flow_load_home_screen(self):
        """
        Load to Home screen:
            -Launch app
        """
        self.driver.press_key_home()
        self.driver.wdvr.start_activity(PACKAGE.JWEB_DOC_PROVIDER, LAUNCH_ACTIVITY.JWEB_DOC_PROVIDER)
        self.fd['home'].verify_doc_provider_open()