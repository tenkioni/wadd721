'''
Henry Chan filename:loan table.py

The basic loan has three parameters: the annual interest rate, monthly payment, and loan balance.
As an example, consider a $300 loan at 12% annual (i.e., 1% monthly) interest, which is being paid off at $100 per month.
After the first month, the balance is $200, but after interest, it increases to $202.
After the second month, the balance is $102, but after interest, it increases to $103.02.
After the third month, the balance is 3.02, which after interest increases to $3.05.
The remainder is paid off in the fourth month.

Write a Python program that prompts for the three parameters and conveys this information in a nice table. You can assume the loan will be paid off in less than five months. For example:

	The loan amount is : 300
	The annual interest rate is: 12
	The monthly payment is: 100

		Starting            Middle              Ending
	Month	Balance   Payment   Balance   Interest  Balance
	-------------------------------------------------------
	1.	300.00	  100.00    200.00       2.00   202.00	
	2.	202.00    100.00    102.00       1.02   103.02
	3.	103.02    100.00      3.02       0.03     3.05
	4.	  3.05      3.05      0.00       0.00     0.00
Run your program with the following 3 sets of sample data:
1)300 12 100
2)1000 15 350
3)12345 33.25 3888.88

'''
import sys
try:
    loanAmount = float(input('The loan amount is :'))
    if loanAmount < 1000 or loanAmount >100000:
        raise Exception('loan amount not in the range of 1000 to 100000')

    annualInterestRate = float(input('The annual interest rate is:'))
    if annualInterestRate < 1 or annualInterestRate > 100:
        raise Exception('interest rate not between 0.1 to 100%')
    
    monthlyPayment = float(input('The monthly payment is:'))

    month = 1
    startingBalance = loanAmount
    payment = monthlyPayment
    middleBalance = startingBalance - payment
    interest = middleBalance * (annualInterestRate / 100 / 12)
    endingBalance = middleBalance + interest
    
    while startingBalance > 0:

        month = month + 1
        if month > 100:
            raise Exception('maximun payment number less than 100')
    
        startingBalance = endingBalance
        if startingBalance < payment:
            payment = startingBalance
        else: payment = monthlyPayment
        middleBalance = startingBalance - payment
        interest = middleBalance * (annualInterestRate / 100/ 12)
        endingBalance = middleBalance + interest
        
    print("%15s%20s%20s"%('Starting','Middle', 'Ending'))
    print("%5s%10s%10s%10s%10s%10s"%('Month ','Balance','Payment','Balance',
                                 'Interest','Balance'))

    print('='*55)
    month = 1
    startingBalance = loanAmount
    payment = monthlyPayment
    middleBalance = startingBalance - payment
    interest = middleBalance * (annualInterestRate / 100 / 12)
    endingBalance = middleBalance + interest

    while startingBalance > 0:
        print("%-5s%10.2f%10.2f%10.2f%10.2f%10.2f"%(str(month)+'.',startingBalance,
                                                    payment,middleBalance,
                                                    interest,endingBalance))
    
    month = month + 1
    startingBalance = endingBalance
    if startingBalance < payment:
        payment = startingBalance
    else: payment = monthlyPayment
    middleBalance = startingBalance - payment
    interest = middleBalance * (annualInterestRate / 100/ 12)
    endingBalance = middleBalance + interest

except Exception as exception:
    sys.stderr.write(str(exception))


