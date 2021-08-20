tax_rate = 0.70
standard_deduction = 500.00
dependent_deduction = 1000.00

gross = float(input("gross income = "))
dependent = int(input("dependent = "))

net_income = gross - standard_deduction - dependent_deduction * dependent
income_tax = net_income * tax_rate
print("The income tax is " + str(round(income_tax, 2)))
