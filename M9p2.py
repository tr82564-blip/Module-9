# processing section
def computeAverage(hitCount, atBats):
    if atBats == 0:
        return 0

    battingAverage = hitCount / atBats
    return battingAverage


playerCount = 0

while True:

    # input section
    lastName = input("Enter player's last name (STOP to finish): ")

    if lastName.upper() == "STOP":
        break

    hitCount = int(input("Enter number of hits: "))
    atBats = int(input("Enter number of at bats: "))

    # processing section
    battingAverage = computeAverage(hitCount, atBats)
    playerCount = playerCount + 1

    # output section
    print(f"Last name: {lastName}")
    print(f"Batting average: {battingAverage:.3f}")
    print()


# output section
print(f"Total players entered: {playerCount}")