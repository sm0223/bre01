from datetime import datetime

from utils.general import years_difference
from utils.dmn_utils import get_dmn_from_pkl
from bom.generated.mpp import Mpp
from policy_rules.functions.rule1 import rule_get_charges, rule_rate

def bre_flow(mpp:Mpp) :
    risk_rating = 1.0
    try:
        # get the decision table instance from cache
        dmn = get_dmn_from_pkl("D:/projects/business_rule_engine/repos/bre01/policy_rules/decision_tables/cache/Applicant_Risk_Rating.pkl")
        #preparing the input for the DT
        data = {
                'City': mpp.application.applicant[0].city,
                'Age': years_difference(mpp.application.applicant[0].dob,
                                        datetime.now()),
                'Salary': mpp.application.applicant[0].salary
        }
        #Calling the DT
        (status, risk) = dmn.decide(data)
        # Error handling and result from DT
        if 'errors' not in status:
            risk_rating = risk["Result"]["Applicant Risk Rating"]
        else:
            print("DMN decision errors: %s", status['errors'])
    except Exception as e:
        print("Unable to load the DMN object")

    # Finally setting the result by calling rule_rate() and rule_get_charges() from rule1
    mpp.result = rule_rate(mpp, risk_rating)
    mpp.result.charges = rule_get_charges(mpp)
    mpp.result.reference = "Success"
    return mpp

