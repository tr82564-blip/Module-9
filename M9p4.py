# processing section
def determineRate(jobCode):

    if jobCode == "L":
        return 25

    elif jobCode == "A":
        return 30

    elif jobCode == "J":
        return 50

    else:
        return 0


totalGrossPay = 0

while True:

    # input section
    lastName = input("Enter employee last name (STOP to finish): ")

    if lastName.upper() == "STOP":
        break

    jobCode = input("Enter job code (L, A, J): ").upper()
    hoursWorked = float(input("Enter hours worked: "))

    # processing section
    payRate = determineRate(jobCode)

    if payRate == 0:
        print("Invalid job code.")
        continue

    if hoursWorked > 40:
        overtimeHours = hoursWorked - 40
        grossPay = (40 * payRate) + (overtimeHours * payRate * 1.5)

    else:
        grossPay = hoursWorked * payRate

    totalGrossPay = totalGrossPay + grossPay

    # output section
    print(f"Last name: {lastName}")
    print(f"Gross pay: ${grossPay:,.2f}")
    print()


# output section
print(f"Total gross pay: ${totalGrossPay:,.2f}")