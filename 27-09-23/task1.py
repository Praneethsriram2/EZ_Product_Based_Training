'''
Swajith is having one lakh in his bank account, rate of interest is 12% per annum. In 5th month Swajith is withdrawing 25000/- in order to buy a gift for is loved one. In 9th month 10000/- is being deposited by his 2nd loved one. End of the financial year how much will he have in his account.
NOTE:- It is simple interest not compound interest.
Write the python program for the above scene.
'''
bal=int(input("Enter Balance: "))
r=float(input("Enter Rate of interest per annam: "))
interest=0
no_of_months=0
month=0
while(True):
    ch=(input("Money want to Deposit(1) or withdrawn(2) or no operation(0): "))
    if ch=='1':
        month=int(input("Enter month: "))
        no_of_months=(month-1)-no_of_months
        money=int(input("Enter Money Deposited: "))
        interest+=((bal*r*(no_of_months/12))/100)
        bal+=money
    elif ch=='2':
        month=int(input("Enter month: "))
        no_of_months=(month-1)-no_of_months
        money=int(input("Enter Money Withdrawn: "))
        interest+=((bal*r*(no_of_months/12))/100)
        bal-=money
    else:
        no_of_months=12-(month-1)
        interest+=((bal*r*(no_of_months/12))/100)
        print(bal,interest)
        break
print(bal+interest)