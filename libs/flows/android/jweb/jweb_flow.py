from abc import ABCMeta
from MobileApps.libs.flows.android.android_flow import AndroidFlow

class JwebFlow(AndroidFlow):
    __metaclass__ = ABCMeta
    project = "jweb"