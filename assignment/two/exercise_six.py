def GetScore():
    scores = []
    num_students = int(input("Enter number of students: "))
    for i in range(num_students):
        score = 110
        print("Score is ", score)
        while score < 0 or score > 100:
            score = int(input(f"Enter score for student {i + 1} (0-100): "))
            if score < 0 or score > 100:
                print("Invalid score! Please enter a value between 0 and 100.")
        scores.append(score)
    return scores


def Total(scores):
    return sum(scores)


def Average(scores):
    return Total(scores) / len(scores)


def Max(scores):
    return max(scores)


def Min(scores):
    return min(scores)


def Passed(scores):
    count = 0
    for score in scores:
        if score >= 50:
            count += 1
    return count


def Failed(scores):
    count = 0
    for score in scores:
        if score < 50:
            count += 1
    return count


def Menu():
    print("\nSelect an option from the menu:")
    print("1. Input students score")
    print("2. Display the number of students")
    print("3. Display Total Score")
    print("4. Display Average Score")
    print("5. Display Maximum score")
    print("6. Display Minimum score")
    print("7. Display Number of students who Passed the exam")
    print("8. Display Number of students who Failed the exam")
    print("9. Exit the program")


# Main program execution
scores = []
while True:
    Menu()
    choice = int(input("\nEnter your choice (1-9): "))

    if choice == 1:
        scores = GetScore()
    elif choice == 2:
        print("Number of students:", len(scores))
    elif choice == 3:
        print("Total score:", Total(scores))
    elif choice == 4:
        print("Average score:", Average(scores))
    elif choice == 5:
        print("Highest score:", Max(scores))
    elif choice == 6:
        print("Lowest score:", Min(scores))
    elif choice == 7:
        print("Number of students who passed:", Passed(scores))
    elif choice == 8:
        print("Number of students who failed:", Failed(scores))
    elif choice == 9:
        print("Exiting the program...")
        break
    else:
        print("Invalid choice! Please enter a number between 1 and 9.")
