
"""
START

request whether the user requires an investment or a bond calculator using the following string:
    
    "Choose either 'investment' or 'bond' from the menu below to proceed:
    
    investment - to calculate the amount of interest you'll earn on your investment
    bond       - to calculate the amount you'll have to pay on a home loan"

and save as 'user_input' variable

convert user_input to all lowercase
    
elif user_input is equal to 'investment':
    request user input amount of money they are depositing and assign to 'deposit' variable
    request user input the interest rate as a percentage and assign to 'interest_rate' variable
    request user input the number of years they plan on investing and assign to 'num_years' variable
    request user input whether they want simple or compound interest and assign to 'interest' variable
    convert interest to all lowercase
    if interest variable is equal to simple:
        total_simple_interest = deposit * (1 + ((interest_rate/100)*num_years))
        print f"The total return you will get back on your investment of R{deposit} over {num_years} years with an interest rate of {interest_rate}% and simple interest will be R{total_simple_interest}."
    elif interest variable is equal to compount:
        total_compound_interest = deposit * math.pow((1 + (interest_rate/100)), num_years)
        print f"The total return you will get back on your investment of R{deposit} over {num_years} years with an interest rate of {interest_rate}% and compound interest will be R{total_compound_interest}."
elif user_input is equal to 'bond':
    request user input current value of house and assign to 'house_value' variable
    request user input interest rate and assign to 'interest_rate' variable
    request user input the number of months they plan to repay the bond and assign to 'num_months' variable
    interest_rate = interest_rate/100
    'monthly_repayment' variable = (interest_rate/12 * house_value) / (1 - (1 + (interest_rate/12))**(-num_months))
    print f"The amount you will have to pay back each month, over a repayment period of {num_months} months, with a house value of R{house_value}, and interest_rate of {interest_rate}% will be R{monthly_repayment}. "
elif user_input does not equal either 'investment' or 'bond':
    print ask the user to restart the programme and re-enter information

STOP

"""
#This programme uses a series of if/elif statments to calculate:
#       1) a total investment's value over time given either the simple or compound interest, or
#       2) the monthly repayments on a home loan

import math

user_input = input(
 """Choose either 'investment' or 'bond' from the menu below to proceed:
    
    investment - to calculate the amount of interest you'll earn on your investment
    bond       - to calculate the amount you'll have to pay on a home loan
    
    Input: """)


user_input = user_input.lower()

if user_input == 'investment':
    deposit = float(input("How much money are you depositing in your investment: R"))
    interest_rate = float(input("Please enter the interest rate as a percentage:"))
    num_years = float(input("How many years do you plan on investing?"))
    interest = input("Please enter whether you would like 'simple' or 'compound' interest?")
    interest = interest.lower()
    if interest == 'simple':
        total_simple_interest = deposit * (1 + (interest_rate/100) * num_years)
        total_simple_interest = '%.2f' % total_simple_interest
        print(f"\nThe total return you will get back on your investment of R{deposit} over {int(num_years)} years with an interest rate of {interest_rate}% and simple interest will be R{total_simple_interest}.")
    elif interest == 'compound':
        total_compound_interest = deposit * math.pow((1 + (interest_rate/100)), num_years)
        total_compound_interest = '%.2f' % total_compound_interest
        print(f"\nThe total return you will get back on your investment of R{deposit} over {int(num_years)} years with an interest rate of {interest_rate}% and compound interest will be: R{total_compound_interest}.")
elif user_input == 'bond':
    house_value = float(input("Please enter the current value of your house: R"))
    interest_rate = float(input("Please enter the interest rate:"))
    interest_rate = interest_rate/100
    num_months = float(input("Over how many months do you intend to repay?"))
    monthly_repayment = (interest_rate/12 * house_value) / (1 - (1 + (interest_rate/12))**(-num_months))
    monthly_repayment = '%.2f' % monthly_repayment
    print(f"\nThe amount you will have to pay back each month, over a repayment period of {int(num_months)} months, with a house value of R{house_value}, and an interest rate of {interest_rate*100}%, will be R{monthly_repayment}.")
elif user_input != "investment" or user_input != "bond":
    print("Please restart the programme and enter either 'investment' or 'bond'")
    
