# FRC 9 - Loop entire program

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

# Code borrowed from zoom call and edited to fit
# Asks the user the name and cost of variable and fixed items
def get_cost(cost_type):

  expenses = []  # holds all expenses

  # Input Heading...
  print("***** {} ******".format(cost_type))

  expense_name = ""
  while expense_name.lower() != "xxx":
      # holds each 'row' of our price breakdown
      single_expense = []

      # Get Item name...
      expense_name = not_blank("Item Name: ", "Please don't leave it blank!", "yes")

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
  return (expenses)

# Makes sure that users don't leave answer blank
def not_blank(question, error_msg, num_ok):
    error = error_msg

    valid = False
    while not valid:
        response = input(question)
        has_errors = ""

        if num_ok !="yes":
            #  look at each character in string and if it's a number, complain
            for letter in response:
                if letter.isdigit() == True:
                    has_errors = "yes"
                    break

        if response == "":
            print(error)
            continue
        elif has_errors != "":
            print(error)
            continue
        else:
            return response


print("***** Welcome to Fund Raiser Calculator! ***** \n"
      "This program allows users to input item costs and it will automatically calculate a selling price!\n"
      "To start, the program will ask how much profit you want to make. Remember to always hit <enter> after each input.\n"
      "Enter 'xxx' in 'Item Name' if all items have been inputted.")
print()

keep_going = ""
while keep_going == "":
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
    quantity_needed = intcheck("Quantity of variable items needed: ", 0)
    print()

    # *** VARIABLE COSTS ***
    # Gets variable costs
    variable_cost = get_cost("Variable Cost")
    print()
    # adds the total of all variable costs
    for item in variable_cost:
        variable_total += item[1]
    # multiplies variable costs by quantity needed
    variable_subtotal = variable_total * quantity_needed

    # *** FIXED COSTS ***
    # Gets fixed costs
    fixed_cost = get_cost("Fixed Cost")
    # adds the total of all fixed costs
    for item in fixed_cost:
        fixed_subtotal += item[1]

    # Sort by cost...
    # put in list
    variable_cost.sort(key=lambda x: x[1], reverse=1)
    fixed_subtotal.sort(key=lambda x: x[1], reverse=1)

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

    sales_needed = total + profit
    print("Sales Needed: ${:.2f}".format(sales_needed))
    print()

    # suggests selling price
    price = profit / quantity_needed
    print("Price per item: ${:.2f}".format(price))
    print()

    keep_going = input("Do you want to use the fund raiser calculator again? Press <enter> to continue or any key to quit.")
    print()


