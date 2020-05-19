# FRC - ask for fixed costs

# To do
# Ask user how much profit they wish to make as a percentage or exact amount
# Get user's total
# Multiply by percentage, or find the difference

# function that asks
def profit_check(question, number):
    valid = False
    while not valid:
        # error messages
        number_error = "Please enter an exact number or percent you want to raise!"
        number_zero = "Please choose a higher number than {}".format(number)
        error = "Please choose % or $!"

        try:
            # keeps asking user if they want $ or % until they give a valid response
            percent_error = "yes"
            while percent_error == "yes":
                response = input(question).lower()
                # ask user how much if they reply with dollar
                if response in dollar:
                    response = float(input("How much? "))
                    break
                # ask user what percent if they reply with percentage
                elif response in percent:
                    response = float(input("What percentage? "))
                    break
                # if user inputs nothing or letters, prints out error message
                else:
                    print(error)
                    percent_error = "yes"
                    continue

            # response has to be higher than a minimum number
            if number < response:
                return response
            elif response == number:
                print(number_zero)
            # if not, print error message
            elif number > response:
                print(number_error)

        except ValueError:
            print(number_error)

# main routine

# possible user response
dollar = ["$", "dollar", "dollars"]
percent = ["%","percentage", "percent"]
# test run
a = profit_check("Do you want to increase the profit by percentage (%) or dollars ($)?", 0)
print(a)
