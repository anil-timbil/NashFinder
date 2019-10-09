from Node import *
class Game():
  def __init__(self, txtfile):
    self.strictDominated = []
    self.strictDominant = []
    self.weakDominant = []
    self.weakDominated = []
    inputfile = open(txtfile, "r", encoding="utf-8")
    text = inputfile.read()
    rows = text.split("/n")
    for row in rows:
      nodeList = row.split(" : ")
      for node in nodeList:
        = new Node(nodeList[])

  def findPureNash(self):
      numCol = len(matrix[0])
      numRow = len(matrix)

      for num2 in range(numCol):
          indexList = []
          for num in range(numRow):
              


  def findMixedNash(self):

  def findStrategies(self):


  def deleteDominated(self):
      return deleted

  def bestResponse(self):
