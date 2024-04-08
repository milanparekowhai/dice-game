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
    roll_result = random.randint(1, 6)
    return roll_result


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
    first_points = roll_1 + roll_2

    # show the user the result
    print(f"Dice: {roll_1} \t {roll_2}: - total: {first_points}")
    return first_points, double_score


# Main Routine starts here


print("press <enter> to begin this round: ")
input()

# Get initial dice rolls for user
user_first = two_rolls()
user_points = user_first[0]
double_points = user_first[1]

# tell the user if they are eligabile for double points
if double_points == "yes":
    print("If you win this round, you gain double points!")

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
    # Tell user if they are winning, losing or if it's a tie.
    if user_points > computer_points:
        result = "😊😊😊you are ahead😁😁😁!"
    elif user_points < computer_points:
        result = "🤖🤖🤖 computer is ahead 📺📺📺"
    else:
        result = "😐 It's now a tie. 😑"

        print(f"{result} \tuser: {user_points} \t | \t computer: {computer_points}")

# Outside loop - double user points if they won and are eligible
# show round results

if user_points < computer_points:
    print("Sorry - you lost this round and no points "
          "have been added to your total score.   The computer's score has "
          f"increased by {computer_points} points.")
# currently dose not include double points!
else:
    print(f'yay! You won the round and {user_points} points have '
          f'been added to your score')
