your_expenses = {
    "Clothes": 1100,
    "Shoes": 1000,
    "Watch": 900,
    "Mobile Recharge": 699,
    "Petrol": 1980
}

wife_expenses = {
    "Mobile Recharge": 799,
    "DTH recharge": 999,
    "Clothes": 2310,
    "Makeup": 3670,
    "Shoes": 999
}

your_total = sum(your_expenses.values())
wife_total = sum(wife_expenses.values())

print(f"Your total expenses: ₹{your_total}")
print(f"Your wife's total expenses: ₹{wife_total}")

if your_total > wife_total:
    print("You are spending more 💸")
elif wife_total > your_total:
    print("Your wife is spending more 💄💸")
else:
    print("You both spent the same!")

print("\nCategory-wise comparison (who spent more):")
common_items = set(your_expenses.keys()).intersection(wife_expenses.keys())

for item in common_items:
    you = your_expenses[item]
    wife = wife_expenses[item]
    if you > wife:
        print(f"{item}: You spent more (₹{you} vs ₹{wife})")
    elif wife > you:
        print(f"{item}: Your wife spent more (₹{wife} vs ₹{you})")
    else:
        print(f"{item}: Same expense (₹{you})")
