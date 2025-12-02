# python
from typing import Dict, Any
from rules.base import BaseFlow

class Bre01Flow(BaseFlow):
    def __init__(self, name: str = "bre01") -> None:
        super().__init__(name)

    def execute(self, payload: Dict[str, Any]) -> Dict[str, Any]:

        return payload
def get_flow() -> Bre01Flow:
    return Bre01Flow()
