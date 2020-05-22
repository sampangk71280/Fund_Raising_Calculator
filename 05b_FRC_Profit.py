# FRC 5 - seperate one component into two

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
                break
            # if response is invalid, keep asking
            else:
                print(error)

        except ValueError:
            print(error)

# function that checks
def how_much(number):
    valid = False
    while not valid:

        # error message
        number_error = "Please enter an exact number or percent you want to raise!"
        number_zero = "Please choose a higher number than {}".format(number)


        raise_by = dollar_percent("Do you want to increase the profit by percentage (%) or dollars ($)?")

        keep_going = "yes"
        while keep_going == "yes":
            if raise_by in dollar:
                profit = float(input("How much? "))
                break
            # ask user what percent if they reply with percentage
            elif raise_by in percent:
                profit = float(input("What percentage? "))
                break
            else:
                keep_going = "yes"
                continue

        # raise_by has to be higher than a minimum number
        if number < profit:
            return profit
        elif number == profit:
            print(number_zero)
            # if not, print error message
        elif number > profit:
            print(number_error)
                

dollar = ["$", "dollar", "dollars", "d"]
percent = ["%","percentage", "percent", "p"]
money = how_much(0)
print(money)


