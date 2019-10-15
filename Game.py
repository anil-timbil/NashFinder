## Game Class
## 10.10.2019
## Anil Timbil, Sean King
## This program defines a game class which is created from a text file.
## The Game class create a grid of Node classes that stores players' 
## payoffs. We can find pure nash equilibria, one mixed equilibrium,
## and strictly dominant dominated strategies.

from Node import *
from sympy.solvers import solve
from sympy import Symbol
import numpy as np

class Game():
  # Construct the grid of nodes and flag the payoffs.
  def __init__(self, txtfile): 
    self.strictDominated = []
    self.strictDominant = []
    self.weakDominant = []
    self.weakDominated = []
    self.matrix = []
    inputfile = open(txtfile, "r", encoding="utf-8")
    text = inputfile.read()
    rows = text.split("\n")
    for row in rows:
      nodeList = row.split(" : ")
      objectList = []
      for values in nodeList:
        objectList.append(Node(values))
      self.matrix.append(objectList)
    self.numCol = len(self.matrix[0])
    self.numRow = len(self.matrix)
    self.flagPayoff()

  # This function helps us mark the payoffs the way we did in the class.
  def flagPayoff(self):
      #Player 1
      for num2 in range(self.numCol):
          indexList = []
          max_val = self.matrix[0][num2].getP1()
          for num in range(self.numRow):
            new_val = self.matrix[num][num2].getP1()
            if new_val > max_val:
              max_val = new_val

          indexList = []
          for i in range(self.numRow):
            if self.matrix[i][num2].getP1() == max_val:
              indexList.append(i)

          for i in indexList:
            self.matrix[i][num2].setSelectP1(True)

      #Player 2
      for num in range(self.numRow):
          indexList = []
          max_val = self.matrix[num][0].getP2()
          for num2 in range(self.numCol):
            new_val = self.matrix[num][num2].getP2()
            if new_val > max_val:
              max_val = new_val

          indexList = []
          for i in range(self.numCol):
            if self.matrix[num][i].getP2() == max_val:
              indexList.append(i)

          for i in indexList:
            self.matrix[num][i].setSelectP2(True)

  # Finds all pure nash equilibria and returns [row index, col index, player1 payoff, player2 payoff]
  def findPureNash(self):
    nash_list = []
    for num in range(self.numRow):
      for num2 in range(self.numCol):
        if self.matrix[num][num2].isNash():
          p1 = self.matrix[num][num2].getP1()
          p2 = self.matrix[num][num2].getP2()
          nash_list.append([num, num2, p1, p2])
    return nash_list

  #Returns the mixed nash equilibrium for a 2-by-2 game.
  def findMixedNash(self):
    if self.numCol !=2 or self.numRow!=2:
      print("Matrix is not a 2-by-2 matrix.")
      return None, None
    q = self.prob_calc(0)
    p = self.prob_calc(1)
    return q,p

  #Find q and p probabilities of the nash equilibrium given a player id: 0->P1, 1->P2
  def prob_calc(self, player_id):
    if player_id == 0:
      payoff1 = self.matrix[0][0].getP1()
      payoff2 = self.matrix[0][1].getP1()
      payoff3 = self.matrix[1][0].getP1()
      payoff4 = self.matrix[1][1].getP1()
    else:
      payoff1 = self.matrix[0][0].getP2()
      payoff2 = self.matrix[0][1].getP2()
      payoff3 = self.matrix[1][0].getP2()
      payoff4 = self.matrix[1][1].getP2()

    #solve for p using solve function
    p = Symbol('p')
    if player_id ==0:
      probability = solve(payoff1*p + payoff2*(1-p) - (payoff3*p+payoff4*(1-p)), p)
    else:
      probability = solve(payoff1*p + payoff3*(1-p) - (payoff2*p+payoff4*(1-p)), p)
    return probability

  #Helper function for counting the number of selected payoffs for each strategy.
  def findStrategies(self):

    #player 1
    select_num_row = []
    for row in range(self.numRow):
      counter = 0
      for col in range(self.numCol):
        if self.matrix[row][col].getSelectP1():
          counter += 1
      select_num_row.append(counter)

    #player 2
    select_num_col = []
    for col in range(self.numCol):
      counter = 0
      for row in range(self.numRow):
        if self.matrix[row][col].getSelectP2():
          counter += 1
      select_num_col.append(counter)

    return select_num_row, select_num_col

  #Prints a list of indexes of strategies that are strictly dominated.
  def findDominated(self):
    rows, columns = self.findStrategies()

    arr_row = np.array(rows)
    result_row = np.where(arr_row == 0)
    print("Strictly dominated strategies found at the following row indices", result_row[0], sep='\n')

    arr_col = np.array(columns)
    result_col = np.where(arr_col == 0)
    print("Strictly dominated strategies found at the following column indices", result_col[0], sep='\n')

  #Prints a list of indexes of strategies that are strictly dominant.
  def findDominant(self):
    rows, columns = self.findStrategies()

    arr_row = np.array(rows)
    result_row = np.where(arr_row == self.numCol)
    print("Strictly dominant strategies found at the following row indices", result_row[0], sep='\n')

    arr_col = np.array(columns)
    result_col = np.where(arr_col == self.numRow)
    print("Strictly dominant strategies found at the following column indices", result_col[0], sep='\n')

# Used for testing the class
if __name__ == '__main__':
    new_Game = Game("game_instance_5.txt")
    new_Game.findDominant()











