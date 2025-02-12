def calculate_grade(scores):
    avg = sum(scores) / len(scores)
    if avg >= 90:
        return "A"
    elif avg >= 80:
        return "B"
    elif avg >= 70:
        return "C"
    elif avg >= 60:
        return "D"
    else:
        return "F"

if __name__ == "__main__":
    scores = [85, 90, 78, 92]
    print("Grade:", calculate_grade(scores))
