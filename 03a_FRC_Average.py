# FRC - order the products from most to least expensive

# To do
# make expense list
# use lambda function
# sort


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

item_cost = []
expenses = [['White Mug', 1.0], ['Printing', 0.75], ['Packaging', 0.5]]
total = 0
# Gets inputs and add to item_cost list
item = ""
while item.lower() != "xxx":
    item_cost = []
    item = input("Item Name: ")

    # If the user enters the exit code, break out of the loop
    if item.lower() == "xxx":
        break

    # Get the cost (replace with number checking function)
    cost = intcheck("Item Cost: ", 0)

    # add item name and cost to 'item list'
    item_cost.append(item)
    item_cost.append(cost)

    # add item nad cost to expense lst
    expenses.append(item_cost)

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