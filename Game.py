from Node import *
from sympy.solvers import solve
from sympy import Symbol

class Game():
  def __init__(self, txtfile):
    self.strictDominated = []
    self.strictDominant = []
    self.weakDominant = []
    self.weakDominated = []
    self.matrix = []
    inputfile = open(txtfile, "r", encoding="utf-8")
    text = inputfile.read()
    rows = text.split("\n")
    #print(rows)
    for row in rows:
      nodeList = row.split(" : ")
      objectList = []
      for values in nodeList:
        objectList.append(Node(values))
      self.matrix.append(objectList)
    self.numCol = len(self.matrix[0])
    self.numRow = len(self.matrix)
    self.flagPayoff()

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

  def findPureNash(self):
    nash_list = []
    for num in range(self.numRow):
      for num2 in range(self.numCol):
        if self.matrix[num][num2].isNash():
          p1 = self.matrix[num][num2].getP1()
          p2 = self.matrix[num][num2].getP2()
          nash_list.append([num, num2, p1, p2])
        #Testing  
        #print(self.matrix[num][num2].getP1(),self.matrix[num][num2].getP2(), self.matrix[num][num2].getSelectP1(), self.matrix[num][num2].getSelectP2())  
    return nash_list

  def findMixedNash(self):
    if self.numCol !=2 or self.numRow!=2:
      print("Matrix is not a 2-by-2 matrix.")
      return null
    q = self.prob_calc(0)
    p = self.prob_calc(1)
    return q,p


  def prob_calc(self, player_id):
    if player_id == 0:
      #fields = {'player':getP1}
      payoff1 = int(self.matrix[0][0].getP1())
      payoff2 = int(self.matrix[0][1].getP1())
      payoff3 = int(self.matrix[1][0].getP1())
      payoff4 = int(self.matrix[1][1].getP1())
    else:
      #fields = {'player':getP2}
      payoff1 = int(self.matrix[0][0].getP2())
      payoff2 = int(self.matrix[0][1].getP2())
      payoff3 = int(self.matrix[1][0].getP2())
      payoff4 = int(self.matrix[1][1].getP2())

    #print(type(payoff1))

    p = Symbol('p')
    if player_id ==0:
      probability = solve(payoff1*p + payoff2*(1-p) - (payoff3*p+payoff4*(1-p)), p)
    else:
      probability = solve(payoff1*p + payoff3*(1-p) - (payoff2*p+payoff4*(1-p)), p)
    return probability


  #def findStrategies(self):


  #def deleteDominated(self):
  #    return deleted

  #def bestResponse(self):
