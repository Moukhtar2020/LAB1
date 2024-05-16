
def calculate_mortgage_payment(principal, annualInterestRate, termInYears):

    if principal < 0:
        raise ValueError("Principal must be a positive number")
    if principal > 1000000000:
        raise ValueError("Principal must be less than a billion")
    if annualInterestRate < 0:
        raise ValueError("Annual interest rate must be a positive number")
    if annualInterestRate > 25:
        raise ValueError("Rate must be between 0 and 25")
    if termInYears <= 0:
        raise ValueError(
            "Term in years must be a positive number greater than zero"
        )
    if termInYears > 40:
        raise ValueError(
            "Term in years must be less than 40 years"
        )

    # Convert annual interest rate to monthly and decimal format
    dailyInterestRate = annualInterestRate / (100 * 365)
    # Convert term from years to months
    termInDays = termInYears * 365

    # Calculate monthly payment
    if dailyInterestRate == 0:
        return principal / termInDays * 30
    else:
        return (
            principal
            * dailyInterestRate
            * (1 + dailyInterestRate) ** termInDays
            / ((1 + dailyInterestRate) ** termInDays - 1)
        ) * 30
    
    principal = 90
annualInterestRate = 20
termInYears = 39

# Call the function to calculate the monthly payment
monthly_payment = calculate_mortgage_payment(23, 25, 33)

# Print the result
print("Monthly payment:", monthly_payment)
