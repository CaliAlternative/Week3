import random 


class Dice:
      
    def __init__(self, firstdice: int, seconddice: int):
          self.firstdice = firstdice
          self.seconddice = seconddice

     
    def rolldice(self,firstdice,seconddice):  
          list1 = [1, 2, 3, 4, 5, 6]
          firstdice = random.choice(list1)
          seconddice = random.choice(list1)
          return(firstdice, seconddice)
    

class Player(Dice):

    def __init__(self, firstdice, seconddice):
         super().__init__(firstdice, seconddice)
         
         firstdice = self.firstdice
         seconddice = self.seconddice  
           
    def winner(self,firstdice, seconddice):
        firstdice = self.firstdice
        seconddice = self.seconddice
        if self.firstdice + self.seconddice == 7:
            print("winner")
        elif firstdice + seconddice == 11:
            print("11 is a winner")
        elif firstdice + seconddice == 2:
            print("loser")
        elif firstdice + seconddice == 12:
            print("12 is a loser")
        else:
            print("Try again")


dice1 = 0
dice2 = 0
Dice()
Dice.rolldice(dice1, dice2)
print(dice1,dice2)
print(Player.winner(dice1,dice2))
print(help(Dice))
          
