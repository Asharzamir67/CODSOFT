import random
def bot():
    choose=["rock","paper","scissor"]
    bot_plan= random.choice(choose)
    return bot_plan
print("WELCOME TO THE GAME:")
rounds=int(input("how many rounds you want to play?\n"))
score=0
for i in range(rounds):
    user_move=input("CHOOSE YOUR MOVE\nROCK,PAPER OR SCISSOR\n")
    bot_move=bot()
    print("USER MOVE:",user_move)
    print("BOT MOVE:", bot_move)
    if (user_move=='rock' and bot_move== 'scissor'):
        print("USER WINS THE ROUND")
        score=score+1
        print("SCORE=",score)
    elif (user_move=='scissor' and bot_move== 'rock'):
        print("BOT WINS THE ROUND")
        score=score-1
        print("SCORE=",score)
    elif (user_move=='scissor' and bot_move== 'paper'):
        print("USER WINS")
        score=score+1
        print("SCORE=",score)
    elif (user_move=='paper' and bot_move== 'scissor'):
        print("BOT WINS")
        score=score-1
        print("SCORE=",score)
    elif (user_move=='paper' and bot_move== 'rock'):
        print("USER WINS")
        score=score+1
        print("SCORE=",score)
    elif (user_move=='rock' and bot_move== 'paper'):
        print("BOT WINS")
        score=score-1
        print("SCORE=",score)
    elif (user_move==bot_move):
        print("DRAW")
        print("SCORE=",score)
    else:
        print("invalid")