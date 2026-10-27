# processing section
def computeTuition(creditHours, districtCode):

    if districtCode == "I":
        tuitionOwed = creditHours * 250

    elif districtCode == "O":
        tuitionOwed = creditHours * 550

    else:
        tuitionOwed = -1

    return tuitionOwed


totalTuition = 0

while True:

    # input section
    lastName = input("Enter student last name (STOP to finish): ")

    if lastName.upper() == "STOP":
        break

    creditHours = int(input("Enter credit hours: "))
    districtCode = input("Enter district code (I or O): ").upper()

    # processing section
    tuitionOwed = computeTuition(creditHours, districtCode)

    if tuitionOwed == -1:
        print("Invalid district code.")
        continue

    totalTuition = totalTuition + tuitionOwed

    # output section
    print(f"Last name: {lastName}")
    print(f"Tuition owed: ${tuitionOwed:,.2f}")
    print()


# output section
print(f"Total tuition owed: ${totalTuition:,.2f}")