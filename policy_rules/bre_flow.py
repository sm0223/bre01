from dataclasses import asdict
from utils.utils import years_difference, get_dmn_from_pkl
from datetime import datetime

from repos.bre01.policy_rules.functions.rule1 import rule_get_charges, rule_rate
from utils.logger import get_logger
from repos.bre01.bom.generated.mpp import Mpp

logger = get_logger(__name__)

def bre_flow(mpp:Mpp) :
    risk_rating = 1.0
    try:
        # get the decision table instance from cache
<<<<<<< HEAD
        dmn = get_dmn_from_pkl("/rules/bre01/policy_rules/decision_tables/cache/Applicant_Risk_Rating.pkl")
=======
        dmn = get_dmn_from_pkl("/repos/bre01/policy_rules/decision_tables/cache/Applicant_Risk_Rating.pkl")
>>>>>>> 8084b12259451452dcae884869c811bf2efb6402
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
            logger.error("DMN decision errors: %s", status['errors'])
    except Exception as e:
        logger.error("Unable to load the DMN object")

    # Finally setting the result by calling rule_rate() and rule_get_charges() from rule1
    mpp.result = rule_rate(mpp, risk_rating)
    mpp.result.charges = rule_get_charges(mpp)
    mpp.result.reference = "Success"
    return mpp

