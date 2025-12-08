from datetime import date
from dataclasses import dataclass, field
from typing import Optional
from dataclasses_json import dataclass_json, config


@dataclass_json
@dataclass
class Applicant:
    name: Optional[str] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    city: Optional[str] = field(
        default=None,
        metadata={
            "name": "City",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    dob: Optional[date] = field(
        default=None,
        metadata=config(
            encoder=lambda x: x.isoformat() if x else None,
            decoder=lambda x: date.fromisoformat(x) if x else None
        )
    )
    salary: Optional[float] = field(
        default=None,
        metadata={
            "name": "Salary",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
@dataclass_json
@dataclass
class Result:
    rate: Optional[float] = field(
        default=None,
        metadata={
            "name": "Rate",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    charges: Optional[float] = field(
        default=None,
        metadata={
            "name": "Charges",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    reference: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
@dataclass_json
@dataclass
class Application:
    application_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "Application_Number",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    applicant: list[Applicant] = field(
        default_factory=list,
        metadata={
            "name": "Applicant",
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
        }
    )
@dataclass_json
@dataclass
class Mpp:
    application: Optional[Application] = field(
        default=None,
        metadata={
            "name": "Application",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    result: Optional[Result] = field(
        default=None,
        metadata={
            "name": "Result",
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )