usage = float(input("Monthly data usage in GB: "))
required_days = int(input("Required validity in days: "))
budget = float(input("Budget: "))

plans = [
    ("Basic", 199, 2, 28, 50),
    ("Standard", 399, 10, 56, 30),
    ("Premium", 599, 25, 84, 20)
]

eligible = []

for name, price, included_gb, validity, excess_rate in plans:
    excess = max(0, usage - included_gb)
    cost = price + excess * excess_rate
    if validity >= required_days and cost <= budget:
        eligible.append((cost, name, excess))

if eligible:
    cost, name, excess = min(eligible)
    print(f"Selected plan: {name}")
    print(f"Excess usage: {excess:.2f} GB")
    print(f"Total cost: {cost:.2f}")
else:
    print("No eligible plan")
