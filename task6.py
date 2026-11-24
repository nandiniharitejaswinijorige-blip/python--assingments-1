distance = float(input("Distance in km: "))
travel_class = input("Class (sleeper/ac/first): ").strip().lower()
passengers = int(input("Number of passengers: "))
cancelled = input("Cancelled (yes/no): ").strip().lower()

slabs = [(100, 1.0), (400, 0.8), (float("inf"), 0.6)]
remaining = distance
base_fare = 0

for limit, rate in slabs:
    slab_distance = min(remaining, limit)
    base_fare += slab_distance * rate
    remaining -= slab_distance
    if remaining <= 0:
        break

class_data = {
    "sleeper": (1.0, 20),
    "ac": (1.5, 50),
    "first": (2.0, 80)
}

if travel_class not in class_data:
    print("Invalid travel class")
else:
    multiplier, reservation_fee = class_data[travel_class]
    total = 0

    for passenger in range(1, passengers + 1):
        age = int(input(f"Age of passenger {passenger}: "))
        concession = 0.5 if age < 5 else 0.5 if age >= 60 else 0
        total += base_fare * multiplier * (1 - concession) + reservation_fee

    if cancelled == "yes":
        total *= 0.25

    print(f"Total fare: {total:.2f}")

output
150
sleeper
2
no
30
65
