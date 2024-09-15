print("Welcome from the shop....")
print("We are supplying stationary and etc.")
print("Welcome from the shop....")

item = int(input("Which item do you want to buy? "))
quantity = int(input("Enter your quantity: "))
yesorno = 1
while yesorno == 1:

    if item == 1:
        amount = quantity * 500
    elif item == 2:
        amount = quantity * 400
    elif item == 3:
        amount = quantity * 100
    else:
        print("Please type the item for 1,2 or 3")
    print("You need to pay ", amount, "kyat")
    yesorno = int(input(print("Enter your yesorno: ")))
    break
