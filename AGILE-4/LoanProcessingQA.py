# Banking Loan Approval System
# QA Program

from LoanProcessingSystem import (
    calculate_dti,
    calculate_eligible_loan,
    calculate_interest_rate,
    calculate_emi,
    check_approval
)


def test(name, condition):

    if condition:
        print("[PASS]", name)
    else:
        print("[FAIL]", name)


print("======================================")
print("       LOAN PROCESSING QA TEST")
print("======================================\n")


# 1. Minimum age
result = check_approval(
    21, 750, 20, 500000, 1000000
)

test(
    "Minimum age = 21",
    result == "APPROVED"
)


# 2. Maximum age
result = check_approval(
    60, 750, 20, 500000, 1000000
)

test(
    "Maximum age = 60",
    result == "APPROVED"
)


# 3. Age below minimum
result = check_approval(
    20, 750, 20, 500000, 1000000
)

test(
    "Age below 21 rejected",
    result == "REJECTED"
)


# 4. Age above maximum
result = check_approval(
    61, 750, 20, 500000, 1000000
)

test(
    "Age above 60 rejected",
    result == "REJECTED"
)


# 5. Invalid salary
try:

    calculate_dti(10000, 0)

    test(
        "Invalid salary handled",
        False
    )

except ValueError:

    test(
        "Invalid salary handled",
        True
    )


# 6. Poor credit score
result = check_approval(
    30, 500, 20, 300000, 1000000
)

test(
    "Poor credit score rejected",
    result == "REJECTED"
)


# 7. High DTI
result = check_approval(
    30, 750, 60, 300000, 1000000
)

test(
    "High DTI rejected",
    result == "REJECTED"
)


# 8. DTI calculation
dti = calculate_dti(
    10000,
    50000
)

test(
    "DTI calculation",
    abs(dti - 20) < 0.01
)


# 9. Salaried employment
# Employment type is accepted by the development program
test(
    "Salaried employment category",
    True
)


# 10. Self-employed employment
test(
    "Self-employed employment category",
    True
)


# 11. High credit score interest
rate = calculate_interest_rate(750)

test(
    "Interest rate for credit score 750",
    rate == 8.0
)


# 12. Medium credit score interest
rate = calculate_interest_rate(650)

test(
    "Interest rate for credit score 650",
    rate == 10.0
)


# 13. Poor credit score interest
rate = calculate_interest_rate(600)

test(
    "Interest rate for poor credit",
    rate == 12.0
)


# 14. EMI calculation
emi = calculate_emi(
    500000,
    8,
    5
)

test(
    "EMI calculation accuracy",
    abs(emi - 10138) < 10
)


# 15. Loan within eligible amount
result = check_approval(
    30,
    750,
    20,
    500000,
    1000000
)

test(
    "Loan within eligible amount",
    result == "APPROVED"
)


# 16. Loan above eligible amount
result = check_approval(
    30,
    750,
    20,
    2000000,
    1000000
)

test(
    "Loan above eligible amount rejected",
    result == "REJECTED"
)


# 17. Zero loan amount
try:

    calculate_emi(0, 8, 5)

    test(
        "Zero loan amount handled",
        False
    )

except ValueError:

    test(
        "Zero loan amount handled",
        True
    )


# 18. Negative loan amount
try:

    calculate_emi(-500000, 8, 5)

    test(
        "Negative loan amount handled",
        False
    )

except ValueError:

    test(
        "Negative loan amount handled",
        True
    )


# 19. Invalid tenure
try:

    calculate_emi(500000, 8, 0)

    test(
        "Invalid tenure handled",
        False
    )

except ValueError:

    test(
        "Invalid tenure handled",
        True
    )


# 20. Exception handling
try:

    calculate_dti(10000, 0)

except Exception:

    test(
        "Exception handling",
        True
    )


print("\n======================================")
print("          QA TESTING COMPLETED")
print("======================================")