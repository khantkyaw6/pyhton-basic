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


# Main program execution
scores = GetScore()

print("Total score:", Total(scores))
print("Average score:", Average(scores))
print("Highest score:", Max(scores))
print("Lowest score:", Min(scores))
print("Number of students who passed:", Passed(scores))
print("Number of students who failed:", Failed(scores))
