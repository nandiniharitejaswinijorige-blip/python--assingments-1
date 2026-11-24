budget = float(input("Travel budget in home currency: "))
count = int(input("Number of expense categories: "))

total = 0
largest_category = ""
largest_amount = -1

for index in range(1, count + 1):
    category = input(f"Category {index}: ")
    amount = float(input("Expense amount in foreign currency: "))
    exchange_rate = float(input("Exchange rate to home currency: "))
    fee_rate = float(input("Conversion fee rate (%): "))

    converted = amount * exchange_rate
    fee = converted * fee_rate / 100
    home_amount = converted + fee
    total += home_amount

    if home_amount > largest_amount:
        largest_amount = home_amount
        largest_category = category

difference = budget - total
status = "Within budget" if difference >= 0 else "Over budget"

print(f"Total spending: {total:.2f}")
print(f"Largest category: {largest_category} ({largest_amount:.2f})")
print(f"Budget difference: {difference:.2f}")
print(status)
