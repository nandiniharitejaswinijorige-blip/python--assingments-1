def calculate_bill(units, fixed_charge, surcharge_rate, rebate):
    slabs = [(100, 1.5), (100, 2.5), (300, 4.0), (float("inf"), 6.0)]
    remaining_units = units
    energy_charge = 0

    for slab_limit, rate in slabs:
        slab_units = min(remaining_units, slab_limit)
        energy_charge += slab_units * rate
        remaining_units -= slab_units
        if remaining_units <= 0:
            break

    surcharge = energy_charge * surcharge_rate / 100
    return max(0, energy_charge + fixed_charge + surcharge - rebate)


months = int(input("Enter number of months: "))
threshold = float(input("Enter unusual increase threshold percentage: "))

previous_bill = None

for month in range(1, months + 1):
    print(f"\nMonth {month}")
    units = float(input("Enter units consumed: "))
    fixed_charge = float(input("Enter fixed charge: "))
    surcharge_rate = float(input("Enter surcharge rate (%): "))
    rebate = float(input("Enter rebate: "))

    bill = calculate_bill(units, fixed_charge, surcharge_rate, rebate)
    print(f"Bill: {bill:.2f}")

    if previous_bill is not None:
        if previous_bill == 0:
            increase = 0 if bill == 0 else float("inf")
        else:
            increase = (bill - previous_bill) / previous_bill * 100

        if increase > threshold:
            print(f"Unusual increase: {increase:.2f}%")

    previous_bill = bill
