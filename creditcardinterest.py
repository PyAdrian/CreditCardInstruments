import math
from datetime import *
def interestcalculator():
    balance_after_payment = int(input(" \n\t Enter the amount after payment from a total due: "))
    # print("balance_after_payment: " + balance_after_payment)
    year = int(input(" \t Enter the year: "))
    month = int(input("\t Enter the month: "))
    day = int(input("\t Enter the day: "))
    dateoftransactionmade = date(year,month,day)
    currentdate = date.today()
    differentcalculation =  currentdate - dateoftransactionmade
    totalnumberofdays = differentcalculation.days
    #print(totalnumberofdays)
    y = int(input(" \t Enter the year: "))
    m = int(input("\t Enter the month: "))
    d = int(input("\t Enter the day: "))
    remainingdateoftransactionmade = date(y,m,d)
    # print(remainingdateoftransactionmade)
    differentinremaining = currentdate - remainingdateoftransactionmade
    differentdays = differentinremaining.days
    # print(differentinremaining)
    remainingpayment = int(input("\t Enter the remaining balance amount to be calculated: "))
    # print(remainingpayment)
    interestratepermonth = float(input("\t Enter the interest amount: " ))/100
    remainingcalculation = (differentdays * remainingpayment * interestratepermonth * 12)/365
    # print(remainingcalculation)
    calculation = (totalnumberofdays * balance_after_payment * interestratepermonth * 12)/365
    total = float(remainingcalculation + calculation)
    print("\t " +str(total))

interestcalculator()