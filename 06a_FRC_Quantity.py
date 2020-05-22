# FRC 6 - Quantity needed

# Functions

# Number checking function
def intcheck(question, number):
    valid = False
    while not valid:
        # Error message
        error = "Whoops! Please enter a valid number above {}!".format(number)

        try:
            response = float(input(question))

            # Returns if response is bigger than number
            if number < response:
                return response
            # If response is less than number, print out error, and keep asking until valid input
            else:
                print(error)
                print()

        except ValueError:
            print(error)

# Code borrowed from zoom call and edited to fit
# Asks the user the name and cost of variable and fixed items
def get_cost(cost_type):

    expenses = [] # holds all expenses

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

# Asks to raise by dollar or percentage
def dollar_percent(question):
    valid = False
    while not valid:
        # error message
        error = "Please choose $ or %!"

        try:
            response = input(question).lower()
            # If response is dollar or percent, continue with main routine
            if response in dollar or response in percent:
                return response
            # If response is invalid, keep asking
            else:
                print(error)

        except ValueError:
            print(error)

# Asks how much profit is wanted
def how_much(number):
    valid = False
    while not valid:

        # Asks if profit is in dollars or percentage
        raise_by = dollar_percent("Do you want to increase the profit by percentage (%) or dollars ($)?")

        keep_going = "yes"
        while keep_going == "yes":
            # If user chooses dollar...
            if raise_by in dollar:
                profit = intcheck("How much?", 0)
                return profit
            # If user chooses percentage...
            elif raise_by in percent:
                profit = intcheck("By what percentage? ", 0)
                return profit
            else:
                keep_going = "yes"
                continue

# Main Routine
total = 0
expenses = []

# possible user response
dollar = ["$", "dollar", "dollars", "d"]
percent = ["%","percentage", "percent", "p"]

# asks user how much money they want to raise
money = how_much(0)

# Gets variable costs
variable_cost = get_cost("Variable Cost")
quantity_needed = intcheck("Quantity Needed: ", 0)

# adds the total of all variable costs
for item in variable_cost:
    total += item[1]
# multiplies variable costs by quantity needed
variable_total = total * quantity_needed


# Gets fixed costs
fixed_cost = get_cost("Fixed Cost")

# Sort by cost...
expenses.sort(key=lambda x: x[1], reverse=1)

# Output
print("**** Variable Items by Cost <Most Expensive to Least Expensive> ****")
for item in variable_cost:
    print("{}: ${:.2f}".format(item[0], item[1]))

print()

print("**** Fixed Items by Cost <Most Expensive to Least Expensive> ****")
for item in fixed_cost:
    print("{}: ${:.2f}".format(item[0], item[1]))




