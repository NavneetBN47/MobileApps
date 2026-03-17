from MobileApps.libs.flows.android.smart.smart_flow import SmartFlow
import time

class HPXLocalPhotos(SmartFlow):
    flow_name = "hpx_local_photos"

    # *********************************************************************************
    #                                ACTION FLOWS                                     *
    # *********************************************************************************

    def verify_album_name(self,timeout=10, raise_e=True):
        """
        Verify the album name is displayed.
        """
        return self.driver.wait_for_object("album_name", timeout=timeout, raise_e=raise_e)