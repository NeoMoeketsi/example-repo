import math

print("Investment- to calculate the amount of interest you'll earn on your investment.")
# causes a line length error in Flake8. # noqa: E501
print("Bond  - to calculate the amount you'll have to pay on a home loan.")

user_choice = input(
    'Enter either "investment" or "bond" from the menu above to proceed: '
)

user_choice = user_choice.lower()
# Convert input to lowercase for case-insensitive comparison

if user_choice == "investment":
    # Use float for decimals,years as well incase of half year
    deposit_amount = float(
        input("Please enter the amount of money you will be deposting? R")
    )
    # code does not work if user inputs % themselves need to account for that
    interest_rate_input = input("Enter the interest rate (as a percentage): ")
    if "%" in interest_rate_input:
        interest_rate = float(interest_rate_input.replace("%", "")) / 100
    else:
        interest_rate = float(interest_rate_input) / 100
    investment_years = float(input("How long will you be investing for?"))
    interest_type = input("What type of interest will be used?")

    if interest_type.lower() == "simple":
        # Calculate simple interest
        total_amount = deposit_amount * (1 + (interest_rate * investment_years))
        # causes a line length error in Flake8. # noqa: E501
    elif interest_type.lower() == "compound":
        # Calculate compound interest
        total_amount = deposit_amount * math.pow((1 + interest_rate), investment_years)
        # causes a line length error in Flake8. # noqa: E501
    else:
        print("Invalid interest type. Please enter 'simple' or 'compound'.")
        exit()

    print(
        f"The total amount after {investment_years} years at {interest_rate * 100:.2f}% {interest_type} interest is: R{total_amount:.2f}"
    )
    # causes a line length error in Flake8. # noqa: E501

# bond..(not james bond) calculator
elif user_choice == "bond":
    present_value = float(input("Enter the present value of the house: "))
    # Handle potential "%" in interest rate input
    annual_interest_rate_input = input("Enter the interest rate (as a percentage): ")
    # causes a line length error in Flake8. # noqa: E501
    if "%" in annual_interest_rate_input:
        annual_interest_rate = float(annual_interest_rate_input.replace("%", "")) / 100
        # causes a line length error in Flake8. # noqa: E501
    else:
        annual_interest_rate = float(annual_interest_rate_input) / 100

    months_to_repay = int(input("Enter the number of months to repay the bond: "))
    # causes a line length error in Flake8. # noqa: E501

    # Calculate monthly interest rate
    monthly_interest_rate = (annual_interest_rate) / 12

    # Calculate monthly bond repayment
    monthly_repayment = (monthly_interest_rate * present_value) / (
        1 - (1 + monthly_interest_rate) ** (-months_to_repay)
    )

    print(f"Your monthly bond repayment will be: R{monthly_repayment:.2f}")
else:
    print("Invalid option - Please select either investment or bond.")
    exit()
