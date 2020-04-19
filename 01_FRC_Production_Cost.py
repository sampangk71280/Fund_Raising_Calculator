# FRC - ask user production cost

# To do
# ask user what the product is
# ask how much it costs to make
# create number checking function

item_cost = []
expenses = []

# Gets inputs and add to item_cost list
item = ""
while item.lower() != "xxx":
    item_cost = []
    item = input("Item Name: ")

    # If the user enters the exit code, break out of the loop
    if item.lower() == "xxx":
        break

    # Get the cost (replace with number checking function)
    cost = float(input("Item Cost: $"))

    # add item name and cost to 'item list'
    item_cost.append(item)
    item_cost.append(cost)

    # add item nad cost to expense lst
    expenses.append(item_cost)

print(expenses)