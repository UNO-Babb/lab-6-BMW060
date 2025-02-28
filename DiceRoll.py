#DiceRoll.py
#Name: Brennan Wood
#Date:2/28/25
#Assign/ment: Lab 6 DiceRoll

import random

def main():
  #Create an empty list with possible roll values
  rolls = [0,0,0,0,0,0,0,0,0,0,0]
  #Create two dice values ranging from 1 - 6 each
  
  for r in range(10000):
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    dice = dice1 + dice2
    rolls[dice-2] = rolls[dice-2] + 1
  
  
  #find the sum total of the two dice
  
  #print statictics for dice rolls

  spot = 2
  for count in rolls:
    chance = int(rolls[spot-2]/sum(rolls)*100)
    print(spot,":",count,"--",chance,"%")
    spot = spot + 1




if __name__ == '__main__':
  main()
