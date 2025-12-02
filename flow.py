# python
from dataclasses import asdict
from typing import Dict, Any
from rules.base import BaseFlow
from rules.bre01.bre.bre_flow import bre_flow
from rules.bre01.models.generated.mpp import Mpp


class Bre01Flow(BaseFlow):
    def __init__(self, name: str = "bre01") -> None:
        super().__init__(name)

    def execute(self, payload: Dict[str, Any]) -> Dict[str, Any]:
        print(type(payload))
        print(payload)
        mpp = Mpp.from_dict(payload)

        mpp_result = bre_flow(mpp)

        return asdict(mpp_result)

