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
    print("------ Instructions -------")
    print()
    print("Rules")
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


# Main Routine
played_before = yes_no("Have you played the game before? ")

if played_before == "no":
    instructions()

# Asks how many points they want to use
how_much = num_check("How much would you like to play with? ", 0, 10)

print("You will be spending {} points".format(how_much))
