name = str(input("Enter employee's name: "))
hours = float(input("Enter number of hours worked in a week: "))
rate = float(input("Enter hourly pay rate: "))
federalWithholding = float(input("Enter federal tax withholding rate: "))
stateWithholding = float(input("Enter state tax withholding rate: "))
grossPay = hours * rate
totalFedWithholding = federalWithholding * hours * rate
totalStateWithholding = stateWithholding * hours * rate
netPay = grossPay - totalFedWithholding - totalStateWithholding

print("\nEmployee Name:", name)
print("Hours Worked:", hours)
print("Pay Rate: $" + "%.2f" % rate)
print("Gross Pay: $" + str(grossPay))
print("Deductions:")
print("\tFederal Withholding (" + str(federalWithholding * 100) + "%): $" + str(totalFedWithholding))
print("\tState Withholding (" + str(stateWithholding * 100) + "%): $" + "%.2f" % totalStateWithholding)
print("\tTotal Deduction: $" + "%.2f" % (totalStateWithholding + totalFedWithholding))
print("Net Pay: ${0:.2f}".format(netPay))
# Console output:
# Enter employee's name: Smith
# Enter number of hours worked in a week: 10
# Enter hourly pay rate: 9.75
# Enter federal tax withholding rate: 0.20
# Enter state tax withholding rate: 0.09
#
# Employee Name: Smith
# Hours Worked: 10.0
# Pay Rate: $9.75
# Gross Pay: $97.5
# Deductions:
#     Federal Withholding (20.0%): $19.5
#     State Withholding (9.0%): $8.77
#     Total Deduction: $28.27
# Net Pay: $69.22
#
# Process finished with exit code 0