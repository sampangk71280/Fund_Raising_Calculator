# FRC 8 v2 - Selling price

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

# Asks to raise by dollar or percentage, returns whether amount is a $ or %
def dollar_percent():

    # possible user response
  dollar = ["$", "dollar", "dollars", "d"]
  percent = ["%","percentage", "percent", "p"]

  valid = False
  while not valid:
      # error message
      error = "Please choose $ or %!"

      response = input("Do you want to calculate the profit based on a dollar amount ($) or a percentage (%)? ").lower()
      # If response is dollar or percent, continue with main routine
      if response in dollar:
        return "$"
      elif response in percent:
          return "%"
      # If response is invalid, keep asking
      else:
          print(error)


# Main Routine
expenses = []
variable_total = 0
fixed_subtotal = 0
profit_dollar = 0
profit_percent = 0


# asks user how much money they want to raise
profit_type = dollar_percent()

if profit_type == "%":
  money_ask = "How much profit would you like to make (as a percentage?)"
else:
  money_ask = "How much profit would you like to make? $"

# the amount of profit wanted
money = intcheck(money_ask, 0)


# *** VARIABLE COSTS ***
# Gets variable costs
# costs have been set for testing purposes
variable_cost = [['White Mug', 1.0], ['Printing', 0.75], ['Packaging', 0.50]]
quantity_needed = intcheck("Quantity of items needed: ", 0)
print()
# adds the total of all variable costs
for item in variable_cost:
    variable_total += item[1]
# multiplies variable costs by quantity needed
variable_subtotal = variable_total * quantity_needed

# *** FIXED COSTS ***
# Gets fixed costs
# costs have been set for testing purposes
fixed_cost = [['Advertising', 100.0], ['Stall', 50.0]]
# adds the total of all fixed costs
for item in fixed_cost:
    fixed_subtotal += item[1]


# Sort by cost...
expenses.sort(key=lambda x: x[1], reverse=1)

# Output
# Variable costs
print("**** Variable Items by Cost <Most Expensive to Least Expensive> ****")
for item in variable_cost:
    print("{}: ${:.2f}".format(item[0], item[1]))
print("Quantity Needed: {:.0f} ".format(quantity_needed))
print("Total Variable Cost: ${:.2f} ".format(variable_subtotal))

print()

# Fixed costs
print("**** Fixed Items by Cost <Most Expensive to Least Expensive> ****")
for item in fixed_cost:
    print("{}: ${:.2f}".format(item[0], item[1]))
print("Total Fixed Costs: ${:.2f}".format(fixed_subtotal))
print()

# prints out total amount
total = variable_subtotal + fixed_subtotal
print("Total: ${:.2f}".format(total))

# calculates profit needed to make
if profit_type == "$":
    profit = money + total
    print("Profit: {:.2f}".format(profit))
else:
    profit = (total/100 * money) + total
    print("Profit: ${:.2f}".format(profit))

print()

# suggests selling price
price = profit / quantity_needed
print("Price per item: ${:.2f}".format(price))


