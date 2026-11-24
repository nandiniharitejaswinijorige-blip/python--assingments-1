venue = float(input("Venue cost: "))
equipment = float(input("Equipment cost: "))
catering_per_person = float(input("Catering cost per person: "))
transport = float(input("Transport cost: "))
certificate_per_person = float(input("Certificate cost per person: "))
sponsorship = float(input("Sponsorship amount: "))
contribution = float(input("Contribution per participant: "))
registrations = int(input("Expected registrations: "))

variable_cost = registrations * (catering_per_person + certificate_per_person)
total_cost = venue + equipment + transport + variable_cost
participant_funds = registrations * contribution
funding_gap = max(0, total_cost - sponsorship - participant_funds)

cost_per_registration = catering_per_person + certificate_per_person
available_after_sponsorship = sponsorship - venue - equipment - transport

if contribution > cost_per_registration:
    minimum_registrations = max(
        0,
        int((venue + equipment + transport - sponsorship + 0.000001)
            / (contribution - cost_per_registration))
    )
    if (minimum_registrations * (contribution - cost_per_registration)
            < venue + equipment + transport - sponsorship):
        minimum_registrations += 1
    minimum_text = str(minimum_registrations)
else:
    minimum_text = "Not achievable with the given contribution"

print(f"Total event cost: {total_cost:.2f}")
print(f"Participant contributions: {participant_funds:.2f}")
print(f"Sponsorship: {sponsorship:.2f}")
print(f"Funding shortfall: {funding_gap:.2f}")
print(f"Minimum registrations to break even: {minimum_text}")

output
1000
500
10
300
2
1000
20
100
