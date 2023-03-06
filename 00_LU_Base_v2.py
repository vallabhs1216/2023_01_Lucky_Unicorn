import random


# Functions
def yes_no(question):
    valid = False
    while not valid:
        response = input(question).lower()

        if response == "yes" or response == "y":
            return "yes"

        elif response == "no" or response == "n":
            return "no"

        else:
            print("Please answer yes / no")


def instructions():
    print("---------------------------")
    print("------ Instructions -------")
    print("---------------------------")
    print()
    print()
    print("Pick an amount from $1.00 to $10.00")
    print()
    print("By pressing <enter> the game will start. "
          "You will get a horse, zebra, donkey, or unicorn")
    print()
    print("It takes $1.00 per each round. "
          "You have the chance to win some money each round")
    print("Here is the tokens values:")
    print("- Unicorn: $5.00 (balance increases by $4.00)")
    print("- Donkey: $1.00 (balance decreases by $1.00)")
    print("- Horse: $0.50 (balance decreases by $0.50)")
    print("- Zebra: $0.50 (balance decreases by $0.50)")
    print()

    return ""


def num_check(question, low, high):
    error = "Please enter an whole number between 1 and 10 "

    valid = False
    while not valid:
        try:
            # ask the question
            response = int(input(question))

            # if the amount is too low / too high
            if low < response <= high:
                return response

            # output and error
            else:
                print(error)

        except ValueError:
            print(error)


def statement_generator(statement, decoration):

    sides = decoration * 3

    statement = "{} {} {}".format(sides, statement, sides)
    top_bottom = decoration * len(statement)

    print(top_bottom)
    print(statement)
    print(top_bottom)

    return ""


# Main Routine
statement_generator("Welcome to Lucky Unicorn game", "*")
played_before = yes_no("Have you played the game before? ")

if played_before == "no":
    instructions()

# Asks how many points they want to use
how_much = num_check("How much would you like to play with? ", 0, 10)

print(f'You will be spending ${how_much:.2f}')

balance = how_much

rounds_played = 0

play_again = input("Press <Enter> to play.").lower()
while play_again == "":

    # increases # of rounds played
    rounds_played += 1

    # Prints round number
    print()
    statement_generator(f'Round #{rounds_played}', "#")
    print()

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

    statement_generator(f'You got {chosen}. Your balance is ${balance:.2f}', "=")
    print()

    if balance < 1:
        play_again = "xxx"
        print("Sorry you have ran out of money")
    else:
        play_again = input("Press <Enter> to replay or 'xxx' to quit ")

print()
statement_generator(f'Starting Balance {how_much:.2f}', "-")
statement_generator(f'Final Balance {balance:.2f}', "-")

