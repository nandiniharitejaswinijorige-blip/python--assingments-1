quantity = int(input("Production quantity: "))
material_per_unit = float(input("Material cost per unit: "))
labour_per_unit = float(input("Labour cost per unit: "))
wastage_rate = float(input("Wastage rate (%): "))
machine_cost = float(input("Total machine cost: "))
selling_price = float(input("Selling price per unit: "))
target_margin = float(input("Target profit margin (%): "))

material_cost = quantity * material_per_unit * (1 + wastage_rate / 100)
labour_cost = quantity * labour_per_unit
total_cost = material_cost + labour_cost + machine_cost
revenue = quantity * selling_price
profit = revenue - total_cost
margin = profit / revenue * 100 if revenue else 0
status = "Target achieved" if margin >= target_margin else "Target not achieved"

print(f"Material cost: {material_cost:.2f}")
print(f"Labour cost: {labour_cost:.2f}")
print(f"Machine cost: {machine_cost:.2f}")
print(f"Total cost: {total_cost:.2f}")
print(f"Revenue: {revenue:.2f}")
print(f"Profit: {profit:.2f}")
print(f"Profit margin: {margin:.2f}%")
print(status)
