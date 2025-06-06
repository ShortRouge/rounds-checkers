# Check that users have entered a valid
# option based on a list
def string_checker(user_response, valid_ans):
    while True:

        # get user response is a word in the list
        user_response = user_response.lower()

        for item in valid_ans:
            # check if the user response is a word in the list
            if item == user_response:
                return item

            # check if the user response ia the same as
            # the first letter of an item in the list
            elif user_response == item[0]:
                return item

        return "invalid"


# Automated testing is below in the from (test_case, expected_value)
to_test = [
    ('Rock', 'rock'),
    ('PAPER', 'paper'),
    ('scissors', 'scissors'),
    ('R', 'rock'),
    ('P', 'paper'),
    ('S', 'scissors'),
    ('XXX', 'xxx'),
    ('x', 'xxx'),
    ('random', 'invalid'),

]

# run test
for item in to_test:
    # retrieve test case and expected value
    case = item[0]
    expected = item[1]

    # get actual value (ie: test ticket function)
    actual = string_checker(case, ["rock", "paper", "scissors", "xxx"])

    # compare actual and expected and output pass / fail
    if actual == expected:
        print(f"✅✅✅Passed! case: {case}, expected: {expected}, received: {actual}✅✅✅")
    else:
        print(f"❌❌❌ failed! case {case}, expected: {expected}, received: {actual}❌❌❌")
