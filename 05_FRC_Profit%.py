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
            response = float(input("Profit: "))

            if number < response:
                return response
            else:
                print(error)
                print()

        except ValueError:
            print(error)

question = input("Do you to increase the profit by percentage (%) or dollars ($)?")
if question == "%":
    percent_ques = print("What percentage? ")
    percentage = profit_check("   %",0 )
if question == "$":
    profit_check("How much? ",0)
