print("There are 2 players in this game.\nEach player will get alternate chance to pick 1 or 2 stones." )
stones=20
player = 1
while stones >0:
   print("There are %1d stones left "%stones)
   if player == 1:
      choice = int(input("Player {0} would you like to remove 1 or 2 stones ?".format(player)))
      if choice not in (1,2):
         choice = int(input("Please enter 1 or 2 "))
      if choice == 2  and stones ==1:
         choice = int(input("Please enter 1 "))
      player=2
      stones -= choice
   else:
      choice = int(input("Player {0} would you like to remove 1 or 2 stones ?".format(player)))
      if choice not in (1,2):
         choice = int(input("Please enter 1 or 2 "))
      if choice == 2  and stones==1:
         choice = int(input("Please enter 1 "))
      player = 1
      stones-=choice   
   if stones<=0:
      print("Player {0} wins".format(player))

print("Press enter to exit")
try:
   exitting=int(input())
except ValueError:
   pass
