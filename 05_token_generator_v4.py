import random

# main routine goes here

STARTING_BALANCE = 100

balance = STARTING_BALANCE
# loop to test generating tokens
for item in range(0, 100):
    chosen_num = random.randint(1, 100)

    # Adjust balance
    # if random # is between 1 and 5
    # user gets unicorn (4 is added to balance)
    if 1 <= chosen_num <= 5:
        chosen = "unicorn"
        balance += 4
    # if random # is between 6 and 37
    # user gets donkey (1 is subtracted from balance)
    elif 6 <= chosen_num <= 37:
        chosen = "donkey"
        balance -= 1
    else:
        # if random # is between 38 and 69
        # user gets horse (0.5 is subtracted from the balance)
        if 38 <= chosen_num <= 69:
            chosen = "horse"
        # if random # has not yet been pulled
        # user gets zebra (0.5 is subtracted from the balance)
        else:
            chosen = "zebra"
        balance -= 0.5

    print("You got {}. Your balance is {}".format(chosen, balance))

print()

print("Starting Balance: {:.2f}".format(STARTING_BALANCE))
print("Final Balance: {:.2f}".format(balance))
