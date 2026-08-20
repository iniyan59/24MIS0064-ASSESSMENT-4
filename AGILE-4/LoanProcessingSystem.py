# Banking Loan Approval System
# Development Program

def calculate_dti(existing_loan, salary):
    if salary <= 0:
        raise ValueError("Salary must be greater than 0")

    return (existing_loan / salary) * 100


def calculate_eligible_loan(salary, credit_score, dti):

    if credit_score >= 750 and dti <= 40:
        return salary * 20

    elif credit_score >= 650 and dti <= 50:
        return salary * 15

    else:
        return salary * 10


def calculate_interest_rate(credit_score):

    if credit_score >= 750:
        return 8.0

    elif credit_score >= 650:
        return 10.0

    else:
        return 12.0


def calculate_emi(loan_amount, interest_rate, tenure):

    if loan_amount <= 0:
        raise ValueError("Loan amount must be greater than 0")

    if tenure <= 0:
        raise ValueError("Loan tenure must be greater than 0")

    monthly_rate = interest_rate / (12 * 100)
    months = tenure * 12

    emi = (
        loan_amount
        * monthly_rate
        * (1 + monthly_rate) ** months
        / ((1 + monthly_rate) ** months - 1)
    )

    return emi


def check_approval(age, credit_score, dti,
                   requested_loan, eligible_loan):

    if age < 21 or age > 60:
        return "REJECTED"

    if credit_score < 650:
        return "REJECTED"

    if dti > 50:
        return "REJECTED"

    if requested_loan > eligible_loan:
        return "REJECTED"

    return "APPROVED"


# -------------------------------
# MAIN PROGRAM
# -------------------------------

try:

    print("======================================")
    print("     BANKING LOAN APPROVAL SYSTEM")
    print("======================================")

    customer_id = input("Enter Customer ID: ")

    age = int(input("Enter Age: "))

    salary = float(input("Enter Monthly Salary: "))

    existing_loan = float(input("Enter Existing Loan Amount: "))

    credit_score = int(input("Enter Credit Score: "))

    employment_type = input(
        "Enter Employment Type (Salaried/Self-Employed): "
    )

    requested_loan = float(
        input("Enter Requested Loan Amount: ")
    )

    tenure = int(
        input("Enter Loan Tenure (years): ")
    )

    # Basic validation
    if age < 0:
        raise ValueError("Invalid age")

    if salary <= 0:
        raise ValueError("Invalid salary")

    if existing_loan < 0:
        raise ValueError("Invalid existing loan amount")

    if credit_score < 0:
        raise ValueError("Invalid credit score")

    if requested_loan <= 0:
        raise ValueError("Invalid requested loan amount")

    if tenure <= 0:
        raise ValueError("Invalid loan tenure")

    # Calculations

    dti = calculate_dti(
        existing_loan,
        salary
    )

    eligible_loan = calculate_eligible_loan(
        salary,
        credit_score,
        dti
    )

    interest_rate = calculate_interest_rate(
        credit_score
    )

    emi = calculate_emi(
        requested_loan,
        interest_rate,
        tenure
    )

    status = check_approval(
        age,
        credit_score,
        dti,
        requested_loan,
        eligible_loan
    )

    # Display result

    print("\n======================================")
    print("          LOAN PROCESSING RESULT")
    print("======================================")

    print("Customer ID       :", customer_id)
    print("Age               :", age)
    print("Monthly Salary    : ₹", format(salary, ".2f"))
    print("Existing Loan     : ₹", format(existing_loan, ".2f"))
    print("Credit Score      :", credit_score)
    print("Employment Type   :", employment_type)
    print("Requested Loan    : ₹", format(requested_loan, ".2f"))
    print("Loan Tenure       :", tenure, "years")

    print("--------------------------------------")

    print("Debt-to-Income Ratio :",
          format(dti, ".2f"), "%")

    print("Eligible Loan Amount : ₹",
          format(eligible_loan, ".2f"))

    print("Interest Rate        :",
          interest_rate, "%")

    print("Monthly EMI          : ₹",
          format(emi, ".2f"))

    print("Approval Status      :", status)

    print("======================================")

except ValueError as e:

    print("\nError:", e)

except Exception as e:

    print("\nUnexpected Error:", e)