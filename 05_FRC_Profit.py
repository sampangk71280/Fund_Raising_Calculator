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
                response = input("Do you to increase the profit by percentage (%) or dollars ($)?").lower()
                if response == "%" or response == "percentage" or response == "percent":
                    profit = float(input("What percentage? "))
                elif response == "$" or "dollars" or "dollar":
                    profit = float(input("How much? "))

                if number < profit:
                    return profit
                else:
                    print(error)
                    print()

            except ValueError:
                print(error)

# Main routine
a = profit_check("Do you want to increase the profit by percentage (%) or dollars ($)?", 0)
print(a)

