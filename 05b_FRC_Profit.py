# FRC 5 - separate one component into two

# to do
# make a function that asks dollar or percentage
# loop how much until a valid raise_by is given

# function that asks to raise by dollar or percentage
def dollar_percent(question):
    valid = False
    while not valid:
        # error message
        error = "Please choose $ or %!"

        try:
            response = input(question).lower()
            # if response is dollar or percent, continue with main routine
            if response in dollar or response in percent:
                return response
            # if response is invalid, keep asking
            else:
                print(error)

        except ValueError:
            print(error)

# number checker for price
def intcheck(question, number):
    valid = False
    while not valid:
            # error message
            error = "Whoops! Please enter a valid number above {}!".format(number)

            try:
                response = float(input(question))
                # if the number is above low, return the number
                if number < response:
                    return response
                # if it's below low, print error until a valid response is given
                else:
                    print(error)
                    print()

            except ValueError:
                print(error)

# function that checks that the number given is valid and higher than minimum
def how_much(number):
    valid = False
    while not valid:

        raise_by = dollar_percent("Do you want to increase the profit by percentage (%) or dollars ($)?")

        keep_going = "yes"
        while keep_going == "yes":
            if raise_by in dollar:
                profit = intcheck("How much?", 0)
                break
            # ask user what percent if they reply with percentage
            elif raise_by in percent:
                profit = intcheck("By what percentage? ", 0)
                break
            else:
                keep_going = "yes"
                continue

<<<<<<< HEAD
        # raise_by has to be higher than a minimum number
        if number < profit:
            return profit
        elif number == profit:
            print(number_zero)
            # if not, print error message
        elif number > profit:
            print(number_error)

=======
>>>>>>> c9ad0572ef84f17f9db4677353ffbbc2a6505a1b

dollar = ["$", "dollar", "dollars", "d"]
percent = ["%", "percentage", "percent", "p"]
money = how_much(0)



