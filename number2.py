import math
import sys
import pandas as pd

def outputStartBalance(loan,rate,payment):
    starting_balance = loan
    middle_balance = starting_balance - payment
    interest = middle_balance*rate/12/100
    ending_balance = middle_balance + interest
    return ending_balance

def interestPayment(middleBalance,rate):
    interest_payment = middleBalance * rate/12/100
    return interest_payment

loan = float(input( "Enter loan amount : " )) 
rate = float(input( "Enter annual interest rate : " )) 
payment = float(input( "Enter monthly payment : " )) 

month_list = []
starting_balance_list = []
payment_list = []
middle_balance_list = []
interest_list = []
ending_balance_list = []

month = 0
starting_balance = loan
monthly_payment = payment
middle_balance = (loan-payment)
monthly_interest = interestPayment(middle_balance,rate)
ending_balance = outputStartBalance(starting_balance,rate,monthly_payment)


for i in range(4):

    month_list.append(i+1)
    starting_balance_list.append(starting_balance)
    payment_list.append(monthly_payment)
    middle_balance_list.append(middle_balance)
    interest_list.append(monthly_interest)
    ending_balance_list.append(ending_balance)
    starting_balance = ending_balance

    if starting_balance > monthly_payment:
        monthly_payment = payment
        middle_balance = starting_balance - monthly_payment
        monthly_interest = interestPayment(middle_balance,rate)
        ending_balance = middle_balance + monthly_interest
        
    else:
        monthly_payment = starting_balance
        middle_balance = 0
        monthly_interest = 0
        ending_balance = 0
    

table = {
    "Month":month_list,
    "Starting Balance":starting_balance_list,
    "Payment":payment_list,
    "Middle Balance": middle_balance_list,
    "Interest": interest_list,
    "Ending Balance": ending_balance_list

}


df = pd.DataFrame(table)
blankIndex=[''] * len(df)
df.index=blankIndex
print(df)