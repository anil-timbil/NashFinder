##Node class
## 10.10.2019
## Anil Timbil, Sean King

class Node():
  def __init__(self, values):
    #print(values.split(","))
    self.p1, self.p2 = values.split(",")
    ##self.isNash = False
    self.selectP1 = False
    self.selectP2 = False

  def setPlayers(self, values):
    splitVal = values.split(",")
    self.p1 = splitVal[0]
    self.p2 = splitVal[1]

  def getP1(self):
      return int(self.p1)

  def getP2(self):
      return int(self.p2)

  def setSelectP1(self, answer):
      self.selectP1 = answer

  def setSelectP2(self, answer):
      self.selectP2 = answer

  def getSelectP1(self):
      return self.selectP1

  def getSelectP2(self):
      return self.selectP2

  def isNash(self):
      return (self.selectP1 and self.selectP2)
