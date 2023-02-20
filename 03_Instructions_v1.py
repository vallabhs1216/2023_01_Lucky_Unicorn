

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
    return""

# Main Routine

played_before = yes_no("Have you played the game before? ")

if played_before == "no":
    instructions()

print("Program continues")
