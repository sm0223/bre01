# python
import logging
from dataclasses import asdict
from datetime import datetime
from typing import Dict, Any
from repos.base import BaseFlow
from repos.bre01.policy_rules.bre_flow import bre_flow
from repos.bre01.bom.generated.mpp import Mpp


class Bre01Flow(BaseFlow):
    def __init__(self, name: str = "bre01") -> None:
        super().__init__(name)

    def execute(self, payload: Dict[str, Any]) -> Dict[str, Any]:

        print("--------------Execution Starts----------------")
        print(datetime.now().time().isoformat(timespec='milliseconds'))
        mpp = Mpp.from_dict(payload) # Parsing input JSON to object
        mpp_result = bre_flow(mpp) # Running the Flow function for specific policy_rules
        print("------------------Execution Ends----------------")
        return asdict(mpp_result)

