# processing section
def computeMPG(milesDriven, gallonsUsed):
    if gallonsUsed == 0:
        return 0

    milesPerGallon = milesDriven / gallonsUsed
    return milesPerGallon


tripCount = 0

while True:

    # input section
    destinationCity = input("Enter destination city (STOP to finish): ")

    if destinationCity.upper() == "STOP":
        break

    milesDriven = float(input("Enter miles travelled: "))
    gallonsUsed = float(input("Enter gallons used: "))

    # processing section
    milesPerGallon = computeMPG(milesDriven, gallonsUsed)
    tripCount = tripCount + 1

    # output section
    print(f"Destination city: {destinationCity}")
    print(f"Miles travelled: {milesDriven:.2f}")
    print(f"Miles per gallon: {milesPerGallon:.2f}")
    print()


# output section
print(f"Total trips entered: {tripCount}")