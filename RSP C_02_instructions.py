# Check that users have entered a valid
# option based on a list

def string_checker(question, valid_ans=('yes', 'no')):
    error = f"please enter a valid option from the following list: {valid_ans}"

    while True:

        # get user response is a word in the list
        user_response = input(question).lower()

        for item in valid_ans:
            # check if the user response is a word in the list
            if item == user_response:
                return item

            # check if the user response ia the same as
            # the first letter of an item in the list
            elif user_response == item[0]:
                return item

            # print error if user does not enter something that is valid
            print(error)
            print()


def instructions():
    print("""
    
*** instructions ****

to begin, choose the number of rounds (or press <enter> for
 infinite mode).

then play against the computer. you need to choose R (rock)
p (paper) s (scissors).

the rules are as follow:
o  paper beats rock
o  rock beats scissors
o  scissors beats paper

press <xxx> to end the game at anytime

Good luck
    """)

# main routine
print()
print("💎📄✂️ rock / paper / scissors game 💎📄✂️")
print()

# ask the user if they want instructions (check they say yes / no)
want_instructions = string_checker("do you want to see the instructions")

# display the instructions if the user wants to see them...
if want_instructions == "yes":
    instructions()

print()
print("program continues")
