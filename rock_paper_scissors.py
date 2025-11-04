import random
print("_-_-_-ROCK PAPER SCISSORS-_-_-_")
Computer=("Rock","Paper","Scissors")
score=0
win_score=int(input("🔥Enter the wining score:"))

while score!=win_score:

    print("The computer has chosen already")
    pick=input("What do YOU choose?:").lower()
    chosen=random.choice(Computer)

    if chosen=="Rock" and pick=="paper":           #winning conditions
        print("😁You scored!😁")
        score+=1
        print()

    elif chosen=="Paper" and pick=="scissors":
        print("😁You scored!😁")
        score+=1
        print()

    elif chosen=="Scissors" and pick=="rock":
        print("😁You scored!😁")
        score+=1                                    #loosing conditions
        print()

    elif chosen == "Paper" and pick == "rock":
        print("🥲You lost a point🥲")
        score-= 1
        print()

    elif chosen == "Scissors" and pick == "paper":
        print("🥲You lost a point🥲")
        score-= 1
        print()

    elif chosen == "Rock" and pick == "Scissors":
        print("🥲You lost a point🥲")
        score-= 1
        print()

    else:
        print("😗Hmm...tie!😗")

    print(f"⬜Your current score is {score}⬜")

print("🎉🎉🎉You win!!!🎉🎉🎉")
print("----THANKS FOR PLAYING----")