# Get the food charge from the user
food_charge = float(input("Enter the amount for the food: "))

# Calculate the tip amount
tip_amount = food_charge * 0.18

# Calculate the sales tax amount
sales_tax = food_charge * 0.07

# Calculate the total amount
total_amount = food_charge + tip_amount + sales_tax

# Display the calculated amounts on the screen
print("Tip amount: $" , format(tip_amount, ".2f"))
print("Sales tax: $" , format(sales_tax, ".2f"))
print("Total amount: $" , format(total_amount, ".2f"))
