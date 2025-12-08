from repos.bre01.bom.generated.mpp import Mpp, Result
from utils.logger import get_logger

logger = get_logger(__name__)

def rule_rate(mpp:Mpp, risk_rating):
    res = Result()
    max_salary = 0
    try:
        for applicant in mpp.application.applicant:
            max_salary = max(max_salary, applicant.salary)
        if risk_rating > 0.8:
            res.rate = 0.2
        else:
            res.rate = 0.15
        return res
    except Exception as e:
        logger.error(e)
        res.reference = "error"
        return res

def rule_get_charges(mpp: Mpp):
    res = Result()
    try:
        charges = 0
        max_salary = 0
        for applicant in mpp.application.applicant :
            max_salary = max(max_salary, applicant.salary)
        if max_salary > 100000:
            charges = 1000.0
        else :
            charges = 500.0
        return charges
    except Exception as e:
        logger.error(e)
        res.reference = "error"
        return res