import math
import random
import pandas as pd
from matplotlib import pyplot as plt
def gatherhingDatas(inputVal,playingRockAfterScissors,playingPaperAfterScissors,playingScissorsAfterScissors,
                    playingScissorsAfterRock,playingPaperAfterRock,playingRockAfterRock,
                    playingRockAfterPaper,playingScissorsAfterPaper,playingPaperAfterPaper,counter):
    playingRockAfterScissors = playingRockAfterScissors
    playingPaperAfterScissors = playingPaperAfterScissors
    playingScissorsAfterScissors = playingScissorsAfterScissors
    playingScissorsAfterRock = playingScissorsAfterRock
    playingPaperAfterRock = playingPaperAfterRock
    playingRockAfterRock = playingRockAfterRock
    playingRockAfterPaper = playingRockAfterPaper
    playingScissorsAfterPaper = playingScissorsAfterPaper
    playingPaperAfterPaper = playingPaperAfterPaper
    counter = counter




    for i in range(0,30000):
        # 0 --> Rock
        # 1 --> Paper
        # 2 --> Scissors
        counter += 1
        df = pd.DataFrame()
        PrimitiveAIChoose = random.randint(0, 2)
        """ 
        print("AI maked his decision")
        print("Take your choose Rock Paper or Scissors")
        """
        playerInput = random.randint(0,2)
        #print("Player maked his decision")
        if(playerInput == 2 and PrimitiveAIChoose == 0):
            playingRockAfterScissors += 1
        if(playerInput == 2 and PrimitiveAIChoose == 1):
            playingPaperAfterScissors += 1
        if(playerInput == 2 and PrimitiveAIChoose == 2):
            playingScissorsAfterScissors += 1
        if(playerInput == 0 and PrimitiveAIChoose == 2):
            playingScissorsAfterRock += 1
        if(playerInput == 0 and PrimitiveAIChoose == 1):
            playingPaperAfterRock += 1
        if(playerInput == 0 and PrimitiveAIChoose == 0):
            playingRockAfterRock += 1
        if (playerInput == 1 and PrimitiveAIChoose == 0):
            playingRockAfterPaper += 1
        if (playerInput == 1 and PrimitiveAIChoose == 2):
            playingScissorsAfterPaper += 1
        if (playerInput == 1 and PrimitiveAIChoose == 1):
            playingPaperAfterPaper += 1
    list = [playingRockAfterScissors,playingPaperAfterScissors,playingScissorsAfterScissors,
            playingScissorsAfterRock,playingPaperAfterRock,playingRockAfterRock
            ,playingRockAfterPaper,playingScissorsAfterPaper,playingPaperAfterPaper]
    df = pd.DataFrame(list,index=['playingRockAfterScissors','playingPaperAfterScissors','playingScissorsAfterScissors','playingScissorsAfterRock',
                            'playingPaperAfterRock','playingRockAfterRock','playingRockAfterPaper','playingScissorsAfterPaper','playingPaperAfterPaper'],
                      columns=['Playing Time'])
    Scissors = df.iloc[0:3]
    Rock = df.iloc[3:6]
    Paper = df.iloc[6:9]
    """ 
    print("Scissors = ",Scissors)
    print("Rock = ",Rock)
    print("Paper = ",Paper)

    print("Mean For Scissors: ",Scissors['Playing Time'].mean())
    print("Variance For Scissors: ",Scissors['Playing Time'].var())
    print("Mean For Rock: ", Rock['Playing Time'].mean())
    print("Variance For Rock: ", Rock['Playing Time'].var())
    print("Mean For Paper: ", Paper['Playing Time'].mean())
    print("Variance For Paper: ", Paper['Playing Time'].var())
    """
    myInput = inputVal
    if (myInput == "Scis"):
        innerProb = ((playingPaperAfterScissors+1)+(playingRockAfterScissors+1)+(playingScissorsAfterScissors+1))/counter
        print("Inner Prob ", innerProb)
        propForScissors = calculate_probability(innerProb,Scissors['Playing Time'].mean(),Scissors['Playing Time'].var())
        propForRock = calculate_probability(((playingPaperAfterRock+playingRockAfterRock+playingScissorsAfterRock)/counter), Rock['Playing Time'].mean(), Rock['Playing Time'].var())/100
        propForPaper = calculate_probability(((playingPaperAfterPaper+playingRockAfterPaper+playingScissorsAfterPaper)/counter), Paper['Playing Time'].mean(), Paper['Playing Time'].var())/100
        print("propForScissors:  ",propForScissors)
        print("propForRock: ",propForRock)
        print("propForPaper: ",propForPaper)
        if (propForScissors > propForRock and propForScissors > propForPaper):
            print("Scissors Oyna")
            print("TIE")
            secondInput = input("Do you want to play again? Yes|No")
            if (secondInput == "Yes"):
                myinput = input("Rock Paper or Scis.... Exit to exiting the game")
                gatherhingDatas(myinput,playingRockAfterScissors,playingPaperAfterScissors,playingScissorsAfterScissors,playingScissorsAfterRock,playingPaperAfterRock,playingRockAfterRock,playingRockAfterPaper,playingScissorsAfterPaper,playingPaperAfterPaper,counter)
            else:
                print("Exiting from the game...")
        if (propForRock > propForScissors and propForRock > propForPaper):
            print("Rock Oyna")
            print("GAME OVER")
            secondInput = input("Do you want to play again? Yes|No")
            if (secondInput == "Yes"):
                myinput = input("Rock Paper or Scis.... Exit to exiting the game")
                gatherhingDatas(myinput,playingRockAfterScissors,playingPaperAfterScissors,playingScissorsAfterScissors,playingScissorsAfterRock,playingPaperAfterRock,playingRockAfterRock,playingRockAfterPaper,playingScissorsAfterPaper,playingPaperAfterPaper,counter)
            else:
                print("Exiting from the game...")
        if (propForPaper > propForRock and propForPaper > propForScissors):
            print("Paper Oyna")
            print("WIN")
            secondInput = input("Do you want to play again? Yes|No")
            if (secondInput == "Yes"):
                myinput = input("Rock Paper or Scis.... Exit to exiting the game")
                gatherhingDatas(myinput,playingRockAfterScissors,playingPaperAfterScissors,playingScissorsAfterScissors,playingScissorsAfterRock,playingPaperAfterRock,playingRockAfterRock,playingRockAfterPaper,playingScissorsAfterPaper,playingPaperAfterPaper,counter)
            else:
                print("Exiting from the game...")
    elif (myInput == "Rock"):
        innerProb = ((playingPaperAfterRock+1)+(playingRockAfterRock+1)+(playingScissorsAfterRock+1))/counter
        print("Inner Prob ", innerProb)
        propForRock = calculate_probability(innerProb, Rock['Playing Time'].mean(), Rock['Playing Time'].var())
        propForScissors = calculate_probability((playingPaperAfterScissors+playingScissorsAfterScissors+playingRockAfterScissors)/counter,Scissors['Playing Time'].mean(),Scissors['Playing Time'].var())/100
        propForPaper = calculate_probability((playingScissorsAfterPaper+playingRockAfterPaper+playingScissorsAfterPaper)/counter, Paper['Playing Time'].mean(), Paper['Playing Time'].var())/100
        print("propForScissors:  ", propForScissors)
        print("propForRock: ", propForRock)
        print("propForPaper: ", propForPaper)
        if (propForScissors > propForRock and propForScissors > propForPaper):
            print("Scissors Oyna")
            print("WIN")
            secondInput = input("Do you want to play again? Yes|No")
            if (secondInput == "Yes"):
                myinput = input("Rock Paper or Scis.... Exit to exiting the game")
                gatherhingDatas(myinput,playingRockAfterScissors,playingPaperAfterScissors,playingScissorsAfterScissors,playingScissorsAfterRock,playingPaperAfterRock,playingRockAfterRock,playingRockAfterPaper,playingScissorsAfterPaper,playingPaperAfterPaper,counter)
            else:
                print("Exiting from the game...")
        if (propForRock > propForScissors and propForRock > propForPaper):
            print("Rock Oyna")
            print("TIE")
            secondInput = input("Do you want to play again? Yes|No")
            if (secondInput == "Yes"):
                myinput = input("Rock Paper or Scis.... Exit to exiting the game")
                gatherhingDatas(myinput,playingRockAfterScissors,playingPaperAfterScissors,playingScissorsAfterScissors,playingScissorsAfterRock,playingPaperAfterRock,playingRockAfterRock,playingRockAfterPaper,playingScissorsAfterPaper,playingPaperAfterPaper,counter)
            else:
                print("Exiting from the game...")
        if (propForPaper > propForRock and propForPaper > propForScissors):
            print("Paper Oyna")
            print("GAME OVER")
            secondInput = input("Do you want to play again? Yes|No")
            if (secondInput == "Yes"):
                myinput = input("Rock Paper or Scis.... Exit to exiting the game")
                gatherhingDatas(myinput,playingRockAfterScissors,playingPaperAfterScissors,playingScissorsAfterScissors,playingScissorsAfterRock,playingPaperAfterRock,playingRockAfterRock,playingRockAfterPaper,playingScissorsAfterPaper,playingPaperAfterPaper,counter)
            else:
                print("Exiting from the game...")

    elif (myInput == "Paper"):
        innerProb = ((playingPaperAfterPaper+1)+(playingRockAfterPaper+1)+(playingScissorsAfterPaper+1))/counter
        propForPaper = calculate_probability(innerProb, Paper['Playing Time'].mean(), Paper['Playing Time'].var())
        propForScissors = calculate_probability((playingPaperAfterScissors+playingScissorsAfterScissors+playingRockAfterScissors)/counter,Scissors['Playing Time'].mean(),Scissors['Playing Time'].var())/100
        propForRock = calculate_probability((playingScissorsAfterRock+playingRockAfterRock+playingPaperAfterRock)/counter, Rock['Playing Time'].mean(), Rock['Playing Time'].var())/100
        print("Inner Prob ", innerProb)
        print("propForScissors:  ", propForScissors)
        print("propForRock: ", propForRock)
        print("propForPaper: ", propForPaper)
        if (propForScissors > propForRock and propForScissors > propForPaper):
            print("Scissors Oyna")
            print("GAME OVER")
            secondInput = input("Do you want to play again? Yes|No")
            if (secondInput == "Yes"):
                myinput = input("Rock Paper or Scis.... Exit to exiting the game")
                gatherhingDatas(myinput,playingRockAfterScissors,playingPaperAfterScissors,playingScissorsAfterScissors,playingScissorsAfterRock,playingPaperAfterRock,playingRockAfterRock,playingRockAfterPaper,playingScissorsAfterPaper,playingPaperAfterPaper,counter)
            else:
                print("Exiting from the game...")
        if (propForRock > propForScissors and propForRock > propForPaper):
            print("Rock Oyna")
            print("WIN")
            secondInput = input("Do you want to play again? Yes|No")
            if (secondInput == "Yes"):
                myinput = input("Rock Paper or Scis.... Exit to exiting the game")
                gatherhingDatas(myinput,playingRockAfterScissors,playingPaperAfterScissors,playingScissorsAfterScissors,playingScissorsAfterRock,playingPaperAfterRock,playingRockAfterRock,playingRockAfterPaper,playingScissorsAfterPaper,playingPaperAfterPaper,counter)
            else:
                print("Exiting from the game...")
        if (propForPaper > propForRock and propForPaper > propForScissors):
            print("Paper Oyna")
            print("TIE")
            secondInput = input("Do you want to play again? Yes|No")
            if (secondInput == "Yes"):
                myinput = input("Rock Paper or Scis.... Exit to exiting the game")
                gatherhingDatas(myinput,playingRockAfterScissors,playingPaperAfterScissors,playingScissorsAfterScissors,playingScissorsAfterRock,playingPaperAfterRock,playingRockAfterRock,playingRockAfterPaper,playingScissorsAfterPaper,playingPaperAfterPaper,counter)
            else:
                print("Exiting from the game...")

    """ 
    print("playingRockAfterScissors: ",playingRockAfterScissors)
    print("playingPaperAfterScissors: ",playingPaperAfterScissors)
    print("playingScissorsAfterScissors: ",playingScissorsAfterScissors)
    print("playingScissorsAfterRock: ",playingScissorsAfterRock)
    print("playingPaperAfterRock: ",playingPaperAfterRock)
    print("playingRockAfterRock: ",playingRockAfterRock)
    print("playingRockAfterPaper: ",playingRockAfterPaper)
    print("playingScissorsAfterPaper: ",playingScissorsAfterPaper)
    print("playingPaperAfterPaper: ",playingPaperAfterPaper)


    print("PropplayingRockAfterScissors: ", playingRockAfterScissors/counter)
    print("PropplayingPaperAfterScissors: ", playingPaperAfterScissors/counter)
    print("PropplayingScissorsAfterScissors: ", playingScissorsAfterScissors/counter)
    print("PropplayingScissorsAfterRock: ", playingScissorsAfterRock/counter)
    print("PropplayingPaperAfterRock: ", playingPaperAfterRock/counter)
    print("PropplayingRockAfterRock: ", playingRockAfterRock/counter)
    print("PropplayingRockAfterPaper: ", playingRockAfterPaper/counter)
    print("PropplayingScissorsAfterPaper: ", playingScissorsAfterPaper/counter)
    print("PropplayingPaperAfterPaper: ", playingPaperAfterPaper/counter)
"""
    visualizeDatas(playingRockAfterScissors,playingPaperAfterScissors,playingScissorsAfterScissors
                   ,playingScissorsAfterRock,playingPaperAfterRock,playingRockAfterRock,playingRockAfterPaper,playingScissorsAfterPaper,playingPaperAfterPaper)

def visualizeDatas(playingRockAfterScissors,playingPaperAfterScissors,playingScissorsAfterScissors,playingScissorsAfterRock,playingPaperAfterRock,playingRockAfterRock,
                   playingRockAfterPaper,playingScissorsAfterPaper, playingPaperAfterPaper              ):
    opportunities = ['RAS', 'PAS', 'SAS', 'SAR', 'PAR','ROR',
               'RAP','SAP','PAP']
    names = [playingRockAfterScissors, playingPaperAfterScissors, playingScissorsAfterScissors,
                      playingScissorsAfterRock, playingPaperAfterRock,playingRockAfterRock,
                      playingRockAfterPaper,playingScissorsAfterPaper,playingPaperAfterPaper]

    plt.bar(opportunities, names)
    plt.title('How many times did it come after which move?')
    plt.xlabel('Possibility Options')
    plt.ylabel('Number of Plays')
    plt.show()




def calculate_probability(x, mean, stdev):
    exponent = math.exp(-((x-mean)*2 / (2 * stdev**2 )))
    return (1 / (math.sqrt(2 * math.pi) * stdev)) * exponent

def Start():
    initInput = input("Rock, Paper or Scis")
    gatherhingDatas(initInput,0,0,0,0,0,0,0,0,0,0)

Start()



