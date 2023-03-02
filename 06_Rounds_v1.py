# set the balance for testing purposes
balance = 5

rounds_played = 0

play_again = input("Press <Enter> to play.").lower()
while play_again == "":

    # increases # of rounds played
    rounds_played += 1

    # Prints round number
    print("*** Round #{} ***".format(rounds_played))
    balance -= 1
    print("Balance: ", balance)
    print()

    if balance < 1:
        play_again = "xxx"
        print("Sorry you have ran out of points")
    else:
        play_again = input("Press <Enter> to replay or 'xxx' to quit ")

print()
print("Final Balance", balance)