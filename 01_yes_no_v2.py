show_instructions = ""
while show_instructions.lower() != "xxx":
    # ask the user if they have played before
    show_instructions = input("have you played this game before? ").lower()

    # If they say yes, output 'program continues'
    # If they say no, output 'display instructions'
    # If they say anything else, outputs error

    if show_instructions == "yes" or show_instructions == "y":
        show_instructions = "yes"
        print("program continues")

    elif show_instructions == "no" or show_instructions == "n":
        print("Instructions")

    else:
        print("Please answer yes / no")