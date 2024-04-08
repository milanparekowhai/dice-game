# Check that users have entered a valid
# option based on a list
def string_checker(question, valid_ans):
    while True:

        # Get user response and make sure its lowercase
        user_response = input(question).lower()

        for item in valid_ans:
            # check if the user response is a word in the lst
            if item == user_response:
                return item

            # check if the user response is the same as
            # the first letter of a item in the list.

            elif user_response == item[0]:

                return item

        return "invalid"


# main route goes here
yes_no = ["yes", "no"]
rps_list = ["rock", "paper", "scissors", "xxx"]


want_instuctions = string_checker("Do you want to see the instructions? "),(yes_no)




print("Too chose", want_instuctions)