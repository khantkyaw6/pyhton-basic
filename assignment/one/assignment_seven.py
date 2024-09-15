obtained_marks = float(input("Enter the obtained marks: "))
total_marks = 100
credit_marks = 75

# Check if the obtained marks meet or exceed the credit threshold
if obtained_marks >= credit_marks:
    print("The student's mark is a credit.")
else:
    print("The student's mark is not a credit.")
