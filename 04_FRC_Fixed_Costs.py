# FRC - ask user for fixed costs

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

fixed_cost = []
expenses = []

# Gets inputs and add to item_cost list
print("Fixed Costs")
item = ""
while item.lower() != "xxx":
    fixed_cost = []
    item = input("Item Name: ")

    # If the user enters the exit code, break out of the loop
    if item.lower() == "xxx":
        break

    # Get the cost (replace with number checking function)
    cost = intcheck("Item Cost: ", 0)

    # add item name and cost to 'item list'
    fixed_cost.append(item)
    fixed_cost.append(cost)

    # add item nad cost to expense lst
    expenses.append(fixed_cost)

print(expenses)