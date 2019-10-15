##Node class
## 10.10.2019
## Anil Timbil, Sean King
## This module defines the Node class that we use in our game grid.
## Each node is able to store payoffs for two players, mark off their
## payoffs for nash finding purposes.

class Node():
  #initilize
  def __init__(self, values): 
    self.p1, self.p2 = values.split(",")
    self.selectP1 = False
    self.selectP2 = False

  #In case we need to change the players payoff.
  def setPlayers(self, values):
    splitVal = values.split(",")
    self.p1 = splitVal[0]
    self.p2 = splitVal[1]

  # Returns the payoff of Player 1 as an int type.
  def getP1(self):
      return int(self.p1)

  # Returns the payoff of Player 2 as an int type.
  def getP2(self):
      return int(self.p2)

  # Sets the select variable to true or false for player 1.
  def setSelectP1(self, answer):
      self.selectP1 = answer

  # Sets the select variable to true or false for player 2.
  def setSelectP2(self, answer):
      self.selectP2 = answer

  # Gets the select variable of Player 1 for nash finding purposes.
  def getSelectP1(self):
      return self.selectP1

  # Gets the select variable of Player 2 for nash finding purposes.
  def getSelectP2(self):
      return self.selectP2

  # Checks if a node is the nash equlibrium in a game. 
  def isNash(self):
      return (self.selectP1 and self.selectP2)
