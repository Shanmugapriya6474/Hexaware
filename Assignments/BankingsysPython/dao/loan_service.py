from exception.custom_exception import LoanNotEligibleException

class LoanService:
    def check_loan_eligibility(self, customer):
        if customer.credit_score > 700 and customer.annual_income >= 50000:
            print("Congratulations! You are eligible for a loan.")
        else:
            raise LoanNotEligibleException("Loan eligibility criteria not met.")
