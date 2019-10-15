## Main Program
## 10.10.2019
## Anil Timbil, Sean King

from Game import *

def main():

  new_Game = Game("game_instance_3.txt")
  print(new_Game.findPureNash())
  q,p=new_Game.findMixedNash()
  print("mixed nash: ", q,p)

main()
