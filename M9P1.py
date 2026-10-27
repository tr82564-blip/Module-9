# processing section
def computeTotal(quantity, unitPrice):
    extendedPrice = quantity * unitPrice

    if extendedPrice > 100000:
        extendedPrice = extendedPrice * 0.90

    return extendedPrice


totalExtPrice = 0

while True:

    # input section
    quantity = int(input("Enter quantity (-1 to stop): "))

    if quantity == -1:
        break

    unitPrice = float(input("Enter unit price: "))

    # processing section
    extendedPrice = computeTotal(quantity, unitPrice)
    totalExtPrice = totalExtPrice + extendedPrice

    # output section
    print(f"Quantity: {quantity}")
    print(f"Unit price: ${unitPrice:,.2f}")
    print(f"Extended price: ${extendedPrice:,.2f}")
    print()


# output section
print(f"Total extended price: ${totalExtPrice:,.2f}")