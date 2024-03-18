   # generates an integer between 0 and 6
# to simulate a roll of die
import random


def yes_no(question):
    while True:
        response = input(question).lower()
        if response == "yes" or response == "y":
            return "yes"
        elif response == "no" or response == "n":
            return "no"
        print("you did not choose a valid response")


def roll_die():
    result = random.randint(1, 6)
    return result

# rolls two dice and returns total and whether we
# had a double roll


def two_rolls():

    double_score = "no"

    # roll two dice
    roll_1 = roll_die()
    roll_2 = roll_die()

    # check if we have a double score opportunity
    if roll_1 == roll_2:
        double_score = "yes"

    # Find the total points (so far)
    user_points = roll_1 + roll_2

    # show the user the result
    print(f"Die 1: {roll_1} \t Die 2:  {roll_2}")
    return user_points, double_score

# Main Routine starts here


print("press <enter> to begin this round: ")
input()

# Get initial dice rolls for user
user_first = two_rolls()
user_points = user_first[0]
double_points = user_first[1]

# tell the user if they are eligabile for double points
if double_points == "no":
    double_feedback = ""
else:
    double_feedback = "If you win this round, you gain double points!"
# output initail move results
print(f"You rolled a total of {user_points}.  {double_feedback}")
print()


# Get initail dice rolls for computer
computer_first = two_rolls()
computer_points = user_first[0]

print(f"the computer rolled a total of {computer_points}.")
# Loop (while both user / computer have <= 13 points)...
while computer_points <= 13 and user_points <= 13:
    # ask user if they want to roll, update
    # points / status
    print()
    roll_again = yes_no("Do you want to roll the dice (type 'no' and 'yes' to roll to pass): ")
    if roll_again == "yes":
        user_move = roll_die()
        user_points += user_move
        print(f"You rolled a user {user_move}.  You now have {user_points} points. ")

        print("\npress <enter> to continue...")
        input()

    # Roll die for computer amd update points
    computer_move = roll_die()
    computer_points += computer_move
    print(f"the computer rolled a {computer_move}.  The computer"
          f" now has {computer_points}.")

    print()
    if user_points > computer_points:
        result = f"😊😊😊you are ahead😁😁😁! "

        print(f"***round update****: {result} ")
        print(f"User score: {user_points} \t | \t computer score: {computer_points}")
        print()
            if computer_points > user_points :
        result = "🤢🤢🤢 The computer is ahead 😫😫😫"

# Outside loop - double user points if they won and are eligible
# show round results

if user_points < computer_points:
    print("Sorry - 😑 you lost this round and no points "
          "have been added to your total score.   The computer's score has "
          f"increased by {computer_points} points.")
# currently dose not include double points!
else:
    print(f'yay! You won the round and {user_points} points have '
          f'been added to your score')
