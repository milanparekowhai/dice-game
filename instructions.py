 # checks users enter yes (y) or no (n)
def yes_no():
    while True:
        response = input("do you want to read instructions ").lower()

        # checks user response, question
        # repeats if users don't enter yes / no
        if response == "yes" or response == "y":
            return "yes"
        elif response == "no" or response == "n":
            return "no"
        print("please enter yes / no")

