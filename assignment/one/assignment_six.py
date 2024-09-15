first_num = int(input("Enter first number: "))
second_num = int(input("Enter second number: "))

multiply = first_num * second_num


for _ in range(2):
    multiply *= first_num * second_num


print("Final Result:", multiply)
