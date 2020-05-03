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

variable_cost = []
fixed_costs = []
expenses = []
total = 0

# Gets variable and fixed costs

print("Variable Costs")
variable = ""
while variable.lower() != "xxx":
    variable_cost = []
    variable = input("Item Name: ")

    # If the user enters the exit code, break out of the loop
    if variable.lower() == "xxx":
        break

    # Get the cost
    cost = intcheck("Item Cost: ", 0)

    # add item name and cost to 'variable cost'
    variable_cost.append(variable)
    variable_cost.append(cost)
    expenses.append(variable_cost)

print("Fixed Costs")
fixed = ""
while fixed.lower() != "xxx":
    fixed_costs = []
    fixed = input("Item Name: ")

    # If the user enters the exit code, break out of the loop
    if fixed.lower() == "xxx":
        break

    # Get the cost
    cost = intcheck("Item Cost: ", 0)

    # add item name and cost to 'fixed cost'
    fixed_costs.append(fixed)
    fixed_costs.append(cost)
    expenses.append(fixed_costs)



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




