basic = float(input("Basic pay: "))
allowances = float(input("Allowances: "))
overtime_hours = float(input("Overtime hours: "))
overtime_rate = float(input("Overtime rate per hour: "))
incentives = float(input("Incentives: "))

gross = basic + allowances + overtime_hours * overtime_rate + incentives

slabs = [(50000, 0.05), (50000, 0.10), (float("inf"), 0.20)]
remaining = gross
deduction = 0

for limit, rate in slabs:
    taxable = min(remaining, limit)
    deduction += taxable * rate
    remaining -= taxable
    if remaining <= 0:
        break

net = gross - deduction

print(f"Basic pay: {basic:.2f}")
print(f"Allowances: {allowances:.2f}")
print(f"Overtime pay: {overtime_hours * overtime_rate:.2f}")
print(f"Incentives: {incentives:.2f}")
print(f"Gross salary: {gross:.2f}")
print(f"Deduction: {deduction:.2f}")
print(f"Net salary: {net:.2f}")

output
Basic pay: 40000.00
Allowances: 10000.00
Overtime pay: 5000.00
Incentives: 5000.00
Gross salary: 60000.00
Deduction: 3500.00
Net salary: 56500.00
