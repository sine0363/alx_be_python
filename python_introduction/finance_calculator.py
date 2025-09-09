users_income = int(input("Enter your monthly income: "))
users_expenses = int(input("Enter your total monthly expenses: "))

monthly_savings = users_income-users_expenses

projected_savings = round(monthly_savings  * 12 + (monthly_savings* 12 * 0.05),0)

print("Your monthly savings are",f"${monthly_savings},",".")
print("Projected savings after one year, with interest is",f"${projected_savings}")