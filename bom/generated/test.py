import json
from dataclasses import asdict
from datetime import datetime

from repos.bre01.bom.generated.mpp import Applicant, Application, Mpp, Result

class DateTimeEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.isoformat()
        return super().default(obj)

r = Result()
a1 = Applicant()
a1.name="Shubham"
a1.city="Delhi"
a1.dob=datetime(1998,1,2)
a1.salary=150000
a2 = Applicant()
a2.name="Ayantika"
a2.city="Bangalore"
a2.dob=datetime(1999,1,2)
a2.salary=150000
apn = Application()
m1 = Mpp()
apn.applicant = [a1,a2]
apn.application_number = "101"
m1.application = apn
m1.result=r
print(json.dumps(asdict(m1),  cls=DateTimeEncoder))

