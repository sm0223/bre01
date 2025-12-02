from ...models.generated import Mpp, Result

def rule_rate(mpp:Mpp, risk_rating):
    res = Result()
    max_salary = 0
    try:
        for applicant in mpp.application.applicant:
            max_salary = max(max_salary, applicant.salary)
        if risk_rating > 0.8:
            res.rate = 1000.0
        else:
            res.rate = 500.0
        return res
    except Exception as e:
        res.reference = "error"
        return res

def rule_get_charges(mpp: Mpp):
    res = Result()
    try:
        charges = 0.0
        max_salary = 0
        for applicant in mpp.application.applicant :
            max_salary = max(max_salary, applicant.salary)
        if max_salary > 100000:
            charges = 1000.0
        else :
            charges = 500.0
        return charges
    except Exception as e:
        res.reference = "error"
        return res