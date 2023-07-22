print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇

Proceed_1 = input("Go left or right?")
if Proceed_1 == "right":
  print("game over")
elif Proceed_1 == "left":
  Proceed_2 = input("swim or wait?")
  if Proceed_2 == "swim":
    print("eaten by sharks - game over")
  elif Proceed_2 == "wait":
    Proceed_3 = input("which door? red, blue, or yellow?")
    if Proceed_3 == "red":
      print("burned by fire - game over")
    elif Proceed_3 == "blue":
      print("beast - game over")
    elif Proceed_3 == "yellow":
      print("You win!")
    else:
      print("game over")
    
