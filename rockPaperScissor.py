import random, sys

Wins = 0
Losses = 0
Ties = 0

while True:
    print('%s Wins, %s Losses, %s Ties' % (Wins, Losses, Ties))

    while True:
        print("choose your move: (r)ock, (p)aper, (s)cissor or (q)uit")

    #player move
        playerMove=input()
        if (playerMove=="r"):
            print("ROCK verses ....")
            break
        elif (playerMove=="p"):
            print("PAPER verses....")
            break
        elif (playerMove=="s"):
            print("SCISSORS verses....")
            break
        elif(playerMove=='q'):
            sys.exit()

        else:
            print("wrong choice")
            break





    #computer choice
    randomNumber=random.randint(1,3)
        #print(randomNumber)

    if (randomNumber==1):
        computerMove='r'
        print("ROCK")
    elif(randomNumber==2):
        computerMove='p'
        print("PAPER")
    else:
        computerMove='s'
        print("SCISSORS")

        #checking for win or loss
    if ( playerMove == computerMove):
        print("it is a tie")
        Ties +=1
    elif(playerMove== 'r' and computerMove=='p'):
        print("computer wins")
        Losses +=1

    elif(playerMove== 'r' and computerMove=='s'):
        print("player wins")
        Wins +=1

    elif(playerMove== 'p' and computerMove=='r'):
        print("player wins")
        Wins +=1

    elif(playerMove== 'p' and computerMove=='s'):
        print("computer wins")
        Losses +=1

    elif(playerMove== 's' and computerMove=='r'):
        print("computer wins")
        Losses +=1

    elif(playerMove== 's' and computerMove=='p'):
        print("player wins")
        Wins +=1
