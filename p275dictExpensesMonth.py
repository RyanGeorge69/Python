expenses={
"January":2200,
"February": 2350,
"March":2600,
"April":2130,
"May":2190,
"June":1980,
"July":2400,
"August":2250,
"September":2100,
"October":2400,
"November":2150,
"December":2500,
}

extra_feb = expenses["February"] - expenses["January"]
print("Extra spent in February compared to January: $",extra_feb,)

q1_total = expenses["January"] + expenses["February"] + expenses["March"]
print("Total expenses in Q1: $",q1_total)

spent_2400 = 2400 in expenses.values()
print("Did you spend exactly $2400 in any month?",end=" ")
if spent_2400:
    print("Yes")
else:
    print("No")

expenses["June"] = 2080
print("Updated June expense to: $",expenses['June'])

expenses["April"] -= 200
print("April expense after refund: $",expenses['April'])

max_month = max(expenses, key=expenses.get)
print("Highest expense in", max_month,"$",expenses[max_month])

first_half_months = ["January", "February", "March", "April", "May", "June"]
first_half_total = sum(expenses[month] for month in first_half_months)
avg_first_half = first_half_total / len(first_half_months)
print(f"Average expense (Jan–June): ${avg_first_half:.2f}")

min_month = min(expenses, key=expenses.get)
print(f"Lowest expense in {min_month}: ${expenses[min_month]}")