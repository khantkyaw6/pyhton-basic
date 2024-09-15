bill_amount = float(input("Enter the total bill amount: $"))


if bill_amount > 200:
    payment_method = "credit card"
else:
    payment_method = "cash"


if payment_method == "credit card":
    print("   a. Take out your credit card.")
    print("   b. Swipe or insert your credit card for payment.")
    print("   c. Enter your PIN or signature as required.")
    print("   d. Wait for the transaction to be approved.")
    print("   e. Collect your receipt.")
else:
    print("   a. Prepare the cash amount.")
    print("   b. Hand the cash to the server.")
    print("   c. Wait for any change to be returned.")
    print("   d. Collect your receipt.")
