ticket_price = 20
discount_ten_percentage = 0.1
discount_twenty_percentage = 0.2
max_ticket = 25
buy_ticket = int(input("Enter your number of ticket : "))

if buy_ticket > max_ticket:
    print(f"You can not buy more than ${25} tickets")
else:
    total_price = ticket_price * buy_ticket

    if buy_ticket >= 20:
        discount = total_price * discount_ten_percentage
    elif buy_ticket >= 10:
        discount = total_price * discount_twenty_percentage
    else:
        discount = 0

    final_price = total_price - discount

    print(f"The discount price is ${discount}")
    print(f"The original price is ${total_price}")
    print(f"The final price is ${final_price}")
