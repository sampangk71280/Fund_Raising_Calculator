# FRC - order the products from most to least expensive

# To do
# make expense list
# use lambda function
# sort

expense_list = [['White Mug', 1.0], ['Printing', 0.75], ['Packaging', 0.50]]

# Sort by cost...
expense_list.sort(key=lambda x: x[1], reverse=1)

# Output
print("**** Items by Cost <Most Expensive to Least Expensive ****")
for item in expense_list:
    print("{}: ${:.2f}".format(item[0], item[1]))

print()

# Sort alphabetically
expense_list.sort(key=lambda x: x[0])

print("**** Items <Alphabetical> *****")
for item in expense_list:
    print("{}: ${:.2f}".format(item[0], item[1]))