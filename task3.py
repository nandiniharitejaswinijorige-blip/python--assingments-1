patient_type = input("Patient type (regular/senior): ").strip().lower()
consultation = float(input("Consultation charge: "))
diagnostic = float(input("Diagnostic charge: "))
treatment = float(input("Treatment charge: "))
eligible = input("Eligible for concession (yes/no): ").strip().lower()
payment = float(input("Payment amount: "))

subtotal = consultation + diagnostic + treatment
concession_rate = 15 if patient_type == "senior" and eligible == "yes" else 0
concession = subtotal * concession_rate / 100
bill = subtotal - concession

if payment < 0 or payment > bill:
    print("Invalid payment amount")
else:
    balance = bill - payment
    if balance == 0:
        classification = "Paid in full"
    elif payment > 0:
        classification = "Partially paid"
    else:
        classification = "Unpaid"

    print(f"Subtotal: {subtotal:.2f}")


   
    print(f"Concession: {concession:.2f}")
    print(f"Final bill: {bill:.2f}")
    print(f"Payment: {payment:.2f}")
    print(f"Balance: {balance:.2f}")
    print(f"Classification: {classification}")


output
senior
500
1200
3000
yes
3000


