import random

score = 0
num_questions = 5

print("🧮 Welcome to the Random Math Quiz!\n")

for i in range(num_questions):
    fnum = random.randint(1, 100)
    snum = random.randint(1, 100)
    op = random.randint(1, 8)

    # Determine operation
    if op == 3:
        print(f"{fnum} * {snum} = ?")
        n = int(input("Type your answer here: "))
        if n == (fnum * snum):
            print("Correct answer ✅")
            score += 1
        else:
            print(f"Oops! Wrong answer ❌. Correct answer is {fnum * snum}")

    elif op == 4:
        print(f"{fnum} / {snum} = ? (Round to 1 decimal)")
        n = float(input("Type your answer here: "))
        correct = round(fnum / snum, 1)
        if n == correct:
            print("Correct answer ✅")
            score += 1
        else:
            print(f"Oops! Wrong answer ❌. Correct answer is {correct}")

    elif op % 2 == 0:  # Even → Subtraction
        print(f"{fnum} - {snum} = ?")
        n = int(input("Type your answer here: "))
        if n == (fnum - snum):
            print("Correct answer ✅")
            score += 1
        else:
            print(f"Oops! Wrong answer ❌. Correct answer is {fnum - snum}")

    else:  # Odd → Addition
        print(f"{fnum} + {snum} = ?")
        n = int(input("Type your answer here: "))
        if n == (fnum + snum):
            print("Correct answer ✅")
            score += 1
        else:
            print(f"Oops! Wrong answer ❌. Correct answer is {fnum + snum}")

print(f"\n🎉 Your final score is {score}/{num_questions}")
