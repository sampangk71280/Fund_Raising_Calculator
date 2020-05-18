# FRC - ask for fixed costs

# To do
# Ask user how much profit they wish to make as a percentage or exact amount
# Get user's total
# Multiply by percentage, or find the difference

# function that asks
def profit_check(question, number):
    valid = False
    while not valid:
        # errpr message
        error = "Please enter an exact number or percentage you want to raise!"

        try:
            response = input(question).lower()
            # ask user how much if they reply with dollar
            if response in dollar:
                response = int(input("How much? "))
            # ask user what percent if they reply with percentage
            elif response in percent:
                response = int(input("What percentage? "))

            # response has to be higher than a minimum number
            if number < response:
                return response
            # if not, print error message
            else:
                print(error)
                print()


        except ValueError:
            print(error)


# main routine

# possible user response
dollar = ["$", "dollar", "dollars"]
percent = ["%","percentage", "percent"]
#test run
a = profit_check("Do you want to increase the profit by percentage (%) or dollars ($)?", 0)
print(a)
