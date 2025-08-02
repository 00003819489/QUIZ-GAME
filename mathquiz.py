import random

score = 0
num_questions = 5

print("🧮 Welcome to the Random Math Quiz!\n")

for i in range(num_questions):
    fnum = random.randint(1, 100)
    snum = random.randint(1, 100)
    op = random.randint(1, 4)

    if op == 1:
        print(f"{fnum} + {snum} = ?")
        n = int(input("Type your answer here: "))
        if n == fnum + snum:
            print("✅ Correct answer!\n")
            score += 1
        else:
            print(f"❌ Oops! The correct answer is {fnum + snum}\n")

    elif op == 2:
        print(f"{fnum} - {snum} = ?")
        n = int(input("Type your answer here: "))
        if n == fnum - snum:
            print("✅ Correct answer!\n")
            score += 1
        else:
            print(f"❌ Oops! The correct answer is {fnum - snum}\n")

    elif op == 3:
        print(f"{fnum} * {snum} = ?")
        n = int(input("Type your answer here: "))
        if n == fnum * snum:
            print("✅ Correct answer!\n")
            score += 1
        else:
            print(f"❌ Oops! The correct answer is {fnum * snum}\n")

    elif op == 4:
        # Avoid dividing by zero
        while snum == 0:
            snum = random.randint(1, 100)

        print(f"{fnum} / {snum} = ? (Round to 2 decimal places)")
        try:
            n = float(input("Type your answer here: "))
            correct = round(fnum / snum, 2)
            if abs(n - correct) < 0.01:
                print("✅ Correct answer!\n")
                score += 1
            else:
                print(f"❌ Oops! The correct answer is {correct}\n")
        except ValueError:
            print("❌ Invalid input!\n")

print(f"🎯 Your final score is: {score}/{num_questions}")
