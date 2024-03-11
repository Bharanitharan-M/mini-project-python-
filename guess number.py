import random
i = random.randint(1, 20)
Ans = int(input("Enter the guessed number "))
Attend = 1
while Attend < 4:
    Attend = Attend + 1
    if i!=Ans:
        if Ans < i:
            print("Guess the number that grater than "+str(Ans))
        elif Ans > i:
             print("Guess the number that less than "+str(Ans))
    else:
        print("You'r guessing is correct,The number is "+str(i))
    Ans = int(input("Enter the number "))
else:
    print("All the attend are fail")