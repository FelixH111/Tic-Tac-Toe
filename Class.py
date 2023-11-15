# -*- coding: utf-8 -*-

class Game:
    
    def __init__(self):
        data = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']] #Stores where the players have
        #gone throughout the game, with each row of the grid being a list.
        self.data = data
        self.player = "X"
        self.scoreX = 0
        self.scoreO = 0

#Asks the player what square they want, then ensures that the input is suitable (the player 
#has input a number between 1 and 3 with co-ordinates that haven't been chosen already). 
#Outputs the coordinates that the player chose.
    def ask_player(self):
        row = input(f"Player {self.player}, which row would you like? (1, 2, or 3) ")
        if row.isdigit() == False:
            print("Please input a number!")
            return self.ask_player()
        else:
            row_int = int(row)
            if row_int > 3 or row_int < 1:
                print("Please try again!")
                return self.ask_player()
        
        column = input(f"Player {self.player}, which column would you like? (1, 2, or 3) ")
        if column.isdigit() == False:
            print("Please input a number!")
            return self.ask_player()
        else:
            column_int = int(column)
            if column_int > 3 or column_int < 1:
                print("Please try again!")
                return self.ask_player()
            
        position = [row_int-1,column_int-1]
        if self.data[position[0]][position[1]] != " ":
            print("That position isn't empty, please try again!")
            return self.ask_player()
        
        return position

#Prints a single, specified line of the board.     
    def print_line(self,number):
        print("-"*13)
        print("| "+str(self.data[number][0])+" | "+str(self.data[number][1])+" | "+str(self.data[number][2]+" |" ))      
    
#Prints the whole board, using the function above.   
    def print_board(self):
        self.print_line(0)
        self.print_line(1)
        self.print_line(2)
        print("-"*13)

#Iterates through each row to check to see if a player has won. If there is only one type of 
#element in a row, and it is not " ", then a player has won and it returns true.  
    def checkrow(self):
        for i in range(0,3):
            if len(set(self.data[i])) == 1 and self.data[i][0] != " ":
                return True
            
#Iterates through, creating a list of the column values and then performs the same check as 
#checkrow to see if a player has won.   
    def checkcolumn(self):
        for i in range(3):
            list1 = []
            for j in range(3):
                list1.append(self.data[j][i])
            if len(set(list1)) == 1 and list1[0] != " ":
                return True
            
#Iterates through, creating 2 lists, each of the values of a diagonal, and then performs the 
#same check as checkrow to see if a player has won.
    def checkdiag(self):
        list1 = []
        list2 = []
        for i in range(3):
            list1.append(self.data[i][i])
            list2.append(self.data[2-i][i])
        if len(set(list1)) == 1 and list1[0] != " ": 
            return True
        elif len(set(list2)) ==1 and list2[0] != " ": 
            return True
        
#Prints a congratulations if a player has won, then updates the scores.
    def win(self):
        print(f"Well done {self.player}, you have won!")
        if self.player == "X":
            self.scoreX += 1
        if self.player == "O":
            self.scoreO += 1
        
#Asks the user if they want to play another game, checks for a correct response, then
#returns a true or false. If true, resets the data back to the start.
    def replay(self):
        answer = input("Would you like to play again? (y/n) ")
        if answer == "y":
            print("You have chosen to play again!")
            self.data = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]
            return True
        if answer == "n":
            print("No worries!")
            return False
        else:
            print("Please answer with y or n!")
            return self.replay()
 
#Prints the overall score of all the games played.
    def score(self):
        print(f"The score was Player X: {self.scoreX}, Player O: {self.scoreO}!")
        
        
        
        