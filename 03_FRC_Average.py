# FRC - finding average

expense_list = [['White Mug', 1.0], ['Printing', 0.75], ['Packaging', 0.5]]

total = 0

# Add costs...
for item in expense_list:
    total += item[1]

average = total / len(expense_list)
print(average)