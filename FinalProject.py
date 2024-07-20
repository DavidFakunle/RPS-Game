# FinalProject.py


from Graphics import *
from random import randint
beginGrfx(1300,700)

######GAME SCREEN#######
setBackground("grey")
drawHeading("Rock Paper Scissors","")
########################

choice= ["Rock","Paper","Scissors"]


ai = choice[randint(0,2)]

index = choice.index(ai)



player = False 
 
choicenum =numinput("RPS Selection", "1 = Rock \n2 = Paper \n3 = Scissors")

while player == False:
  # ai = choice[index]
   if choicenum == index :
      drawString("TIED",500,350,"Lucida Console",30)
   elif choicenum== 1: #rock
      if ai == "Paper":
         drawString("You Lose Paper Covers ",500,350,"Lucida Console",30)
      else:
         drawString("You Win Rock Smashes!",500,350,"Lucida Console",30)
   elif choicenum== 2:# Paper
      if ai == "Scissors":
         drawString("You Lose Scissors Cut",500,350,"Lucida Console",30)
      else:
         drawString("You Win Paper Covers!",500,350,"Lucida Console",30)
   elif choicenum == 3: #Scissors
      if ai == "Rock":
         drawString("You Lose Rock Smashes!",500,350,"Lucida Console",30)
      else:
         drawString("You Win Scissors Cut!",500,350,"Lucida Console",30)
   else:
      drawString("Invalid",500,350,"Lucida Console",30)
   player=False








endGrfx()
