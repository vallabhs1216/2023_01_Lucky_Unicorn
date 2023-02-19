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

# Main Routine

show_instructions = yes_no("Have you played the game before? ")
print("You chose {}".format(show_instructions))
print()
enjoying = yes_no("Are you enjoying the game? " )
print("You said {} to enjoying the game".format(enjoying))