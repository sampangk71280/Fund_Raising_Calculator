# FRC - ask for fixed costs

# To do
# Ask user how much profit they wish to make as a percentage or exact amount
# Get user's total
# Multiply by percentage, or find the difference

def profit_check(question, number):
    valid = False
    while not valid:
        error = "Please enter an exact number or percentage you want to raise!"

        try:
            response = input(question).lower()
            if response == dollar:
                response = int(input("How much? "))
            elif response == percent:
                response = int(input("What percentage? "))


                if number < response:
                    return response
                else:
                    print(error)
                    print()


        except ValueError:
            print(error)


# main routine
dollar = ["$", "dollar", "dollars"]
percent = ["%","percentage", "percent"]
a = profit_check("Do you want to increase the profit by percentage (%) or dollars ($)?", 0)
print(a)
