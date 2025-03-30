# check for an integer more than 0 (allows <enter>)
def int_check(question):
    while True:
        error = "please enter an integer that is 1 or more"

        to_check = input(question)

        # check for infinite mode
        if to_check == "":
            return "infinite"

        try:
            response = int(to_check)

            # check that the number is more than / equal to 13
            if response < 1:
                print(error)
            else:
                return response

        except ValueError:
            print(error)


# main routine starts here

# initialise game variables
mode = "regular"
rounds_played = 0


print("💎📄✂️ rock / paper / scissors game 💎📄✂️")
print()

# Instructions

# ask user for number of rounds / infinite mode
num_rounds = int_check("how many rounds would you like? push <enter> for infinite: ")

if num_rounds == "infinite":
    mode = "infinite"
    print("you choose infinite")
    num_rounds = 5

# game loop starts here
while rounds_played < num_rounds:
    user_choice = input("choose: ")

    if user_choice == "xxx"
        break
        
    rounds_played += 1
    print("rounds played: ", rounds_played)

    # if user are infinite mode, increase number of rounds!
    if mode == "infinite":
        num_rounds += 1

    print(("num rounds: ", num_rounds))
# game loop ends here

# game history / statistics area
