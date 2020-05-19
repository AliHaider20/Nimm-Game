players=[]
players.append(input("Player 1 name: "))
players.append(input("Player 2 name: "))
stones=20
player = players[0]
while stones >0:
   print("There are %1d stones left "%stones)
   if player == players[0]:
      choice = int(input("{0} would you like to remove 1 or 2 stones ?".format(player)))
      if choice not in (1,2):
         choice = int(input("Please enter 1 or 2 "))
      if choice == 2  and stones ==1:
         choice = int(input("Please enter 1 "))
      player=players[1]
      stones -= choice
   else:
      choice = int(input("{0} would you like to remove 1 or 2 stones ?".format(player)))
      if choice not in (1,2):
         choice = int(input("Please enter 1 or 2 "))
      if choice == 2  and stones==1:
         choice = int(input("Please enter 1 "))
      player = players[0]
      stones-=choice   
   if stones<=0:
      print("{0} wins".format(player))

print("Press enter to exit")
try:
   exitting=int(input())
except ValueError:
   pass
