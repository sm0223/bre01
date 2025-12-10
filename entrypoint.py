from datetime import datetime

from utils.general import tlogger

from bom.generated.mpp import Mpp
from policy_rules.bre_flow import bre_flow


class Bre01Flow():

    def execute(self, mpp:Mpp):
        tlogger().info("Execution Starts at Entrypoint")
        try:
            mpp_result = bre_flow(mpp) # Running the Flow function for specific policy_rules
        except Exception as e:
            mpp.result.reference = "Failed"
            tlogger().error()
        tlogger().info("Execution Ends at Entrypoint")
        return mpp_result

