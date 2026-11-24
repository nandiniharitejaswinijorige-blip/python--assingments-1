count = int(input("Number of items: "))
threshold = float(input("Discount threshold: "))
discount_rate = float(input("Discount rate (%): "))
max_concession = float(input("Maximum concession: "))

tax_rates = {"food": 0.05, "clothing": 0.12, "electronics": 0.18}
subtotal = 0
tax_total = 0
items = []

for index in range(1, count + 1):
    name = input(f"Item {index} name: ")
    category = input("Category (food/clothing/electronics): ").strip().lower()
    price = float(input("Unit price: "))
    quantity = int(input("Quantity: "))

    item_total = price * quantity
    tax = item_total * tax_rates.get(category, 0)
    subtotal += item_total
    tax_total += tax
    items.append((name, quantity, item_total, tax))

discount = min(subtotal * discount_rate / 100, max_concession) if subtotal >= threshold else 0
final_total = subtotal - discount + tax_total

for name, quantity, item_total, tax in items:
    print(f"{name}: quantity {quantity}, amount {item_total:.2f}, tax {tax:.2f}")

print(f"Subtotal: {subtotal:.2f}")
print(f"Discount: {discount:.2f}")
print(f"Tax: {tax_total:.2f}")
print(f"Final total: {final_total:.2f}")
