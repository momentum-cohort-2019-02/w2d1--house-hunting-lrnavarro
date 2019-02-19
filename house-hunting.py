print("How many months will it take to buy a house? ")


annual_salary = int(input("Enter your annual salary: ") )
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: ") )
total_cost = int(input("Enter the cost of your dream home: ") )

current_savings = 0
portion_down_payment = (total_cost) * 0.25
r = 0.04 # current_savings*r/12
total_months = 0
monthly_savings = (annual_salary/12)*portion_saved

# At the end of each month, your savings will be increased by the return on your investment, plus a percentage of your monthly salary (annual salary / 12)

while current_savings < portion_down_payment:
    current_savings += monthly_savings + current_savings*r/12
    total_months += 1

print("Number of months: " + str(total_months) )

