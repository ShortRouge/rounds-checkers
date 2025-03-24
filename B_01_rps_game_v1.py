# check for an integer more than 0 (allows <enter>)
def int_check(to_check):
    while True:
        error = "please enter an integer that is 1 or more"

        # check for infinite mode
        if to_check == "":
            return "infinite"

        try:
            response = int(to_check)

            # check that the number is more than / equal to 13
            if response < 1:
                # print(error)
                return "invalid"
            else:
                return response

        except ValueError:
            # print(error)
            return "invalid"


# Automated testing is below in the from (test_case, expected_value)
to_test = [
    ('xlii', 'invalid'),
    ('0.5', 'invalid'),
    ('0', 'invalid'),
    (1, 1),
    (2, 2),
    ('', 'infinite')
]

# run test
for item in to_test:
    # retrieve test case and expected value
    case = item[0]
    expected = item[1]

    # get actual value (ie: test ticket function)
    actual = int_check(case)

    # compare actual and expected and output pass / fail
    if actual == expected:
        print(f"✅✅✅Passed! case: {case}, expected: {expected}, received: {actual}✅✅✅")
    else:
        print(f"❌❌❌ failed! case {case}, expected: {expected}, received: {actual}❌❌❌")
