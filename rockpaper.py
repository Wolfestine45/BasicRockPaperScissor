import random

player1 = input("Select rock, paper, scissor :")
player2 = random.choice(["rock","paper","scissor"])
print("player 2 selected: ",player2)

if player1 == "rock" and player2 == "paper":
   print("player 2 won")
elif player1 == "scissor" and player2 == "rock":
     print("player 2 won")
elif player1 == "paper" and player2 == "scissor":
     print("player 2 won")
elif player1 == player2:
     print("TIE")
else:
     print(" You WON ")
exit()
