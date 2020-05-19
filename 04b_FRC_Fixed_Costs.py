# FRC - ask for fixed costs

# To do
# ask user what the fixed costs are
# ask how much it costs to make
# create number checking function

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
    all_expenses = [] #holds entire breakdown

    # Input Heading...
    print("***** Input {} ******".format(cost_type))

    expense = ""
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
variable_cost = []
fixed_costs = []
expenses = []
total = 0

# Gets variable and fixed costs
variable_cost = get_cost("Variable Cost:")
fixed_cost = get_cost("Fixed Cost")



# Sort by cost...
expenses.sort(key=lambda x: x[1], reverse=1)

# Output
print("**** Items by Cost <Most Expensive to Least Expensive ****")
for item in expenses:
    print("{}: ${:.2f}".format(item[0], item[1]))

print()

# Add costs...
for item in expenses:
    total += item[1]

average = total / len(expenses)
print("Average: ${:.2f}".format(average))




