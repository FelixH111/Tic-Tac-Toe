# -*- coding: utf-8 -*-

from Class import Game

game = Game()

print("Welcome to TicTacToe!")

round = 0

turn_go = True

while round < 999:                                  #The game runs until the players choose 
                                                    #to break.  
    if turn_go == True:
        if round%2 == 0:                            #Alternates between players during a 
            game.player = "X"                       #game and alternates between the starting
        if round%2 == 1:                            #player each consecutive game.
            game.player = "O"
    
    if turn_go == False:
        if round%2 == 1:
            game.player = "X"
        if round%2 == 0:
            game.player = "O"
    
    answer = game.ask_player()                    #Asks the player where they want to go.
    game.data[answer[0]][answer[1]] = game.player #Stores the players answer.
    game.print_board()                            #Prints how the new board looks.
    if game.checkrow() == True:                   #Checks to see if the game has been won.
        game.win()
        replay =  game.replay()                   #If the game has been won, it asks for
        if replay == True:                        #a replay. If accepted, the round resets.
            round = -1
            turn_go = not turn_go
        if replay == False:                       #If a replay is not accepted, the score is
            game.score()                          #displayed and while loop broken.
            break
    elif game.checkcolumn() == True:
        game.win()
        replay =  game.replay()
        if replay == True:
            round = -1
            turn_go = not turn_go
        if replay == False:
            game.score()
            break
    elif game.checkdiag() == True:
        game.win()
        replay =  game.replay()
        if replay == True:
            round = -1
            turn_go = not turn_go
        if replay == False:
            game.score()
            break
            
    round += 1                                    #If no-one has won this round, the counter
                                                  #goes up one and the game continues.
    if round == 9:                                #If the counter reaches 9, the game ends as 
        print("The game is a draw!")              #a draw.
        replay =  game.replay()
        if replay == True:
            round = 0
            turn_go = not turn_go
        if replay == False:
            game.score()
            break
