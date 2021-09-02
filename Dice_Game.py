import random
start = input("Press Enter to start game : ")
play_again = True

while play_again:
    target = 15
    current_score = 0
    print(" Your Target : ", target)
    print(" Your Current Score is : ", current_score)
    while current_score <= target:
        throw = input("Press Enter to Throw Dice ")
        random_number = random.randint(1,6)
        current_score += random_number
        print(" You get", random_number, end = " ")
        print("And your Current score is ", current_score)
        if current_score == target:
            print(" YOU WON! ")
            AsktoPlay = int(input("To play again press 1 or press 0 to end the game: "))
            if AsktoPlay == 0:
                play_again = False
            break

    else:
        print(" YOU LOST! , BETTER LUCK NEXT TIME")
        AsktoPlay = int(input("To play again press 1 or press 0 to end the game: "))
        if AsktoPlay == 0:
            play_again = False

else:
    print("---GAME OVER---")