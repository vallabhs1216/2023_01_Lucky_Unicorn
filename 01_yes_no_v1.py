# ask the user if they have played before
show_instructions = input("have you played this game before").lower()

# If they say yes, output 'program continues'
if show_instructions == "yes":
    print("program continues")

# If they say no, output 'display instructions'
elif show_instructions == "no":
    print("Instructions")

# If they say anything else, outputs error
else:
    print("Please answer yes / no")