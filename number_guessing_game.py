import random
number=random.randint(1,1000)
print("_"*50)
print("Guess a number between 1-1000 you MORON or")
print("--Enter 00 to quit--")
guesses=1
while True:
    guess=int(input("your guess?:"))

    if guess==00:
        break
    elif guess<number:
        print("Go Higher")
    elif guess>number:
        print("Go Lower")
    elif guess==number:
        print(f"🎉🎉🎉{guess} is right YOU WON in {guesses} guesses🎉🎉🎉")
        break
    guesses+=1
print(f"---Thanks for playing---")