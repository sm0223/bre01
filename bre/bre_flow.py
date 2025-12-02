import pyDMNrules
from utils.utils import years_difference
from datetime import datetime

from .functions.rule1 import rule_get_charges, rule_rate
from ..models.generated import Mpp
from utils.logger import get_logger
logger = get_logger(__name__)



def bre_flow(self, mpp:Mpp) :
    risk_rating_dmn = (pyDMNrules.DMN().load('decision_tables/Applicant_Risk_Rating.xlsx'));
    data = {
            'City': mpp.application.applicant[0].city,
            'Age': years_difference(mpp.application.applicant[0].dob,
                                    datetime.now()),
            'Salary': mpp.application.applicant[0].salary
    }

    (status, risk_rating) = risk_rating_dmn.decide(data)
    if 'errors' in status:
        risk_rating = 1.0
        logger.error("DMN decision errors: %s", status['errors'])
    mpp.result = rule_rate(mpp, risk_rating)
    mpp.result.charges = rule_get_charges(mpp)
    return mpp