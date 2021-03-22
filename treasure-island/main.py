
print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')


print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 
#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

left_right = input('''\nYou walk through the doors of treasure palace, advancing along a long corridor. 
Approaching a cross roads you can decide to go "left" or "right".\n''')

if left_right.lower() == "left":
  swim_boat = input('''\nAfter traveling left you aproach a river with a dock, you 
can either "wait" for a boat or "swim" accross. ''')
  if swim_boat.lower() == "wait":

    door = input('''\nAfter crossing the river safely by boat you walk up a staircase 
and appraoch 3 doors, one "blue", one "yellow" and one "red" door. \nWhich will you enter? ''')
    if  door.lower() == "yellow":
      print("\n\nYou Win! Now you're fake rich!")
    elif door.lower() == "red":
      print('''\nThe door slams shut behind you and walls slowly move towards you, turning you 
into a meat patty.\n\n GAME OVER''')
    elif door.lower() == "blue":
      print('''\nBlue is a nice colour huh. Too bad the door disappeared, oh look the floor too. 
And you've been consumed by piranhas.\n\nGAME OVER''')
    else:
      print("Stop trying to cheat the system.\n\nGAME OVER")
    
  else:
    print("\nA family of hippos beat you to death like the numbskull you are.\n\nGAME OVER")
else:
  print("\nA wall of flames consume you.\n\nGAME OVER")

  

