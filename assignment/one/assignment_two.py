mark1 = int(input("Enter the first mark :"))
mark2 = int(input("Enter the second mark :"))
mark3 = int(input("Enter the third mark :"))
passing_mark = 100
final_mark = mark1 + mark2 + mark3

if final_mark >= passing_mark:
    print("Pass")
else:
    print("Fail")
