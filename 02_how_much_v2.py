# Functions

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


# Main routine goes here

how_much = num_check("how many points would you like to use? ", 0, 10)

print("You will be spending {} points".fotmat(how_much))
