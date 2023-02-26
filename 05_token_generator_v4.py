import random

# main routine goes here

STARTING_BALANCE = 100

balance = STARTING_BALANCE
# loop to test generating tokens
for item in range(0, 100):
    chosen_num = random.randint(1, 100)

    # Adjust balance

    if 1 <= chosen_num <= 5:
        chosen = "unicorn"
        balance += 4
    elif 6 <= chosen_num <= 37:
        chosen = "donkey"
        balance -= 1
    else:
        if 38 <= chosen_num <= 69:
            chosen = "horse"
        else:
            chosen = "zebra"
        balance -= 0.5

    print("You got {}. Your balance is {}".format(chosen, balance))

print()

print("Starting Balance: {:.2f}".format(STARTING_BALANCE))
print("Final Balance: {:.2f}".format(balance))
