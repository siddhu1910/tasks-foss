#play a simple rock paper scissors game with cpu by setting a score limit...Those who reches to the score limit first Wins the game...
import random
a=int(input("score limit: "))
count1=0
count2=0
i=0
output=["rock","paper","scissor"]
while (count1<a and count2<a):
	print("round",i+1)
	i+=1
	n=input("your choice: ")
	cpu=(random.choice(output))
	print("cpu choice: ",cpu)
	if n=="rock" and cpu=="rock":
		print("its a draw")
		print()
		print()
	if n=="rock" and cpu=="paper":
		print("you lost a point")
		count2+=1
		print()
		print()
	if n=="rock" and cpu=="scissor":
		print("you scored a point")
		count1+=1
		print()
		print()
	if n=="paper" and cpu=="rock":
		print("you lost a point")
		count2+=1
		print()
		print()
	if n=="paper" and cpu=="scissor":
		print("you lost a point")
		count2+=1
		print()
		print()
	if n=="paper" and cpu=="paper":
		print("its a draw")
		print()
		print()
	if n=="scissor" and cpu=="rock":
		print("you lost a point")
		count2+=1
		print()
		print()
	if n=="scissor" and cpu=="paper":
		print("you scored a point")
		count1+=1
		print()
		print()
	if n=="scissor" and cpu=="scissor":
		print("its a draw")
		print()
		print()
else:
	print("game is over...")
	print("your score is",count1)
	print(" cpu score is",count2)
if count1==a:
	print("you won the game...CONGRATS")
if count1==count2:
	print("the game is draw")
else:
	print("sorry you lost the game..better luck next time")	

