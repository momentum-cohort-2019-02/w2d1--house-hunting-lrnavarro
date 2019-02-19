print("How many months will it take to buy a house? ")


annual_salary = int(input("Enter your annual salary: ") )
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: ") )
total_cost = int(input("Enter the cost of your dream home: ") )
down_payment_percent = input("Enter the percent of your home's cost to save as down payment [0.25]: ")

if down_payment_percent == "":
    down_payment_percent = 0.25

annual_rate_of_return = input("Enter the expected annual rate of return [0.04]: ")

if annual_rate_of_return == "":
    annual_rate_of_return = 0.04

current_savings = 0
portion_down_payment = (total_cost) * float(down_payment_percent)

# r = 0.04 # current_savings*r/12

total_months = 0
monthly_savings = (annual_salary/12)*portion_saved

# At the end of each month, your savings will be increased by the return on your investment, plus a percentage of your monthly salary (annual salary / 12)

while current_savings < portion_down_payment:
    current_savings += monthly_savings + current_savings * float(annual_rate_of_return)/12
    total_months += 1

print("Number of months: " + str(total_months) )
