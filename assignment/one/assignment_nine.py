bill_amount = float(input("Enter the total bill amount (between $10 and $500): $"))
num_people = int(input("Enter the number of people (up to 12): "))


if bill_amount < 10 or bill_amount > 500:
    print("Bill amount must be between $10 and $500.")
elif num_people < 1 or num_people > 12:
    print("Number of people must be between 1 and 12.")
else:
    amount_per_person = bill_amount / num_people
    print(f"Each person needs to pay: ${amount_per_person:.2f}")
