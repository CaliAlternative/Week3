import random 


class Dice:
      
    def __init__(self, dice1: int, dice2: int):
          self.roll_dice1 = dice1
          self.roll_dice2 = dice2

      
    def rolldice(firstdice, seconddice):  
          list1 = [1, 2, 3, 4, 5, 6]
          firstdice = random.choice(list1)
          seconddice = random.choice(list1)
          return(firstdice, seconddice)
    

class Player:
    def __init__(self, _firstdice: int, _seconddice: int):
         super().__init__(Dice.firstdice, Dice.seconddice)
         
         _firstdice = Dice.firstdice
         _seconddice = Dice.seconddice  
           
    def winner(_firstdice, _seconddice):
        if _firstdice + _seconddice = 7:
            print("winner")
        elif _firstdice + _seconddice = 11:
            print("11 is a winner")
        elif _firstdice + _seconddice = 2:
            print("loser")
        elif _firstdice + _seconddice = 12:
            print("12 is a loser")
        else:
            print("Try again")



dice1 = 0
dice2 = 0
Dice.rolldice(dice1, dice2)
print(dice1,dice2)
print(Player.winner(dice1,dice2))


          