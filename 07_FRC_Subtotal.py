# FRC 5 - Quantity Needed

# To do
# Ask user variable items and cost
# Ask user quantity needed

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


# Main Routine
expenses = []
variable_total = 0
fixed_subtotal = 0

# *** VARIABLE COSTS ***
# Gets variable and fixed costs
variable_cost = get_cost("Variable Cost")
# Asks the quantity of variable items needed
quantity_needed = intcheck("Quantity Needed: ", 0)
print()
# adds the total of all variable costs
for item in variable_cost:
    variable_total += item[1]
# multiplies variable costs by quantity needed
variable_subtotal = variable_total * quantity_needed



# *** FIXED COSTS ***
fixed_cost = get_cost("Fixed Cost")
# adds the total of all fixed costs
for item in fixed_cost:
    fixed_subtotal += item[1]

# prints out subtotals
print("Total Variable Cost: ${:.2f} ".format(variable_subtotal))
print("Total Fixed Costs: ${:.2f}".format(fixed_subtotal))

#prints out the total amount
total = variable_subtotal + fixed_subtotal
print("Total: ${}".format(total))