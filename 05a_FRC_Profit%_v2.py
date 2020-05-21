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


# number checker for price
def intcheck(item, low):
    valid = False
    while not valid:
            error = "Whoops! Please enter a valid number above 0!"

            try:
                response = float(input("Item Cost: $ "))
                if low < response:
                    return response
                else:
                    print (error)
                    print ()

            except ValueError:
                print(error)

# code borrowed from zoom call and edited to fit
# asks the user the name and cost of variable and fixed items
def get_cost(cost_type):
    expenses = [] # if expense list is here, fixed and variable cost listed correctly, but expenses is zero
                 # without it, fixed and variable list has the same items, but average is printed out
    # Input Heading...
    print("***** {} ******".format(cost_type))

    expense_name = ""
    while expense_name.lower() != "xxx":
        # holds each 'row' of our price breakdown
        single_expense = []

        # Get Item name...
        expense_name = input("Item Name: ")

        # If the user enters the exit code, break the loop
        if expense_name.lower() == "xxx":
            break

        # Get Item Cost and check it's valid via # checking function
        cost = intcheck("Item Cost: $ ", 0)

        # Add both the item name and cost to the mini list
        single_expense.append(expense_name)
        single_expense.append(cost)

        # Add the mini lists to the master list
        expenses.append(single_expense)

    print()  # puts space between lists / output
    return(expenses)

# Main Routine
total = 0 # total cost of items
expenses = []

# possible user response
dollar = ["$", "dollar", "dollars", "d", "D"]
percent = ["%","percentage", "percent", "p", "D"]

# asks user how much money they want to raise
how_much = profit_check("Do you want to increase the profit by percentage (%) or dollars ($)?", 0)

# Gets variable and fixed costs
variable_cost = get_cost("Variable Cost")
fixed_cost = get_cost("Fixed Cost")

# Sort by cost...
expenses.sort(key=lambda x: x[1], reverse=-1 )

# Output
print("**** Variable Items by Cost <Most Expensive to Least Expensive> ****")
for item in variable_cost:
    print("{}: ${:.2f}".format(item[0], item[1]))

print()

print("**** Fixed Items by Cost <Most Expensive to Least Expensive> ****")
for item in fixed_cost:
    print("{}: ${:.2f}".format(item[0], item[1]))

print()

# Add costs...
for item in expenses:
    total += item[1]

average = total / len(expenses)
print("Average: ${:.2f}".format(average))

