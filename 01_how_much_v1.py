# Functions


# Main routine goes here

error = "Please enter an whole number between 1 and 10"

valid = False
while not valid:
    try:
        # ask the question
        response = int(input("how many points would you like to use? "))

        # if the amount is too low / too high
        if 0 < response <= 10:
            print("You have chosen to play using {} points".format(response))

        # output and error
        else:
            print(error)

    except ValueError:
        print(error)