Wel = str(input("Welcome to Jiggers Toy Shop! What is your name? "))
Toy = ("\nNerf Guns: $14.36 \nDolls: $5.64 \nAction Figures: $6.56 \nBoard Games: $8.96 \nGiant Bouncy Balls: $10.12")

print("Nice to meet you " + str(Wel) + ". We have a good collection of toys for sale:", Toy)

nerf = int(input("How many nerf guns do you want to buy, " + str(Wel) + "? "))
while nerf < 0:
 print("You can't do that stupid!!!")
 nerf = int(input("How many nerf guns do you want to buy, " + str(Wel) + "? "))

doll = int(input("How many dolls do you want to buy, " + str(Wel) + "? "))
while doll < 0:
 print("You can't do that stupid!!!")
 doll = int(input("How many dolls do you want to buy, " + str(Wel) + "? "))

fig = int(input("How many action figures do you want to buy, " + str(Wel) + "? "))
while fig < 0:
 print("You can't do that stupid!!!")
 fig = int(input("How many action figures do you want to buy, " + str(Wel) + "? "))

board = int(input("How many board games do you want to buy, " + str(Wel) + "? "))
while board < 0:
 print("You can't do that stupid!!!")
 board = int(input("How many board games do you want to buy, " + str(Wel) + "? "))

ball = int(input("How many giant bouncy balls do you want to buy, " + str(Wel) + "? "))
while ball < 0:
 print("You can't do that stupid!!!")
 ball = int(input("How many giant bouncy balls do you want to buy, " + str(Wel) + "? "))

nerf_t = round((14.36 * nerf), 2)
if nerf_t > 0:
 print("That will be $" + str(nerf_t), "for the nerf guns")
doll_t = round((5.64 * doll))
if doll_t > 0:
 print("That will be $" + str(doll_t), "for the dolls")
fig_t = round((6.56 * fig), 2)
if fig_t > 0:
 print("That will be $" + str(fig_t), "for the action figures")
board_t = round((8.96 * board), 2)
if board_t > 0:
 print("That will be $" + str(board_t), "for the board games")
ball_t = round((10.12 * ball), 2)
if ball_t > 0:
 print("That will be $" + str(ball), "for the giant bouncy balls")

total = (nerf_t + doll_t + fig_t + board_t + ball_t)
round_total = round(total, 2)


print("Which makes your total $" + str(round_total))

Pay = str(input("Will that be Cash, Card, Apple Pay, or Google Pay? "))

print("Thank you", str(Wel) + ", have a nice day!")

