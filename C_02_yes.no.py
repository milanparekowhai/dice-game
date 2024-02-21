# checks users enter yes (y) or no (n)
def yes_no(question, responce=None):
    while True:
        want_instructions = input("do you want to read instructions ").lower()

        from urllib import response
        if want_instructions == "yes" or response == "y":
            return "yes"
        elif response == "no" or responce == "n":
            return  "no"
        print("you did not choose a valid respone")

# Main route
while True:
    want_insrtuctions = yes_no("do you want to read the instructions")
    print(f"You chose {want_insrtuctions} ")

roll_again = yes_no("do you want to roll again ")
print(f'you said {roll_again} to roll again. ')