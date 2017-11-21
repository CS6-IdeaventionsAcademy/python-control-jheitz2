# John
# 11/21/2017
# Fire Water Grass

import random
choices=["fire", "water", "grass"]
compchoice=choices[random.randint(0,2)]
choice=input("fire, water, or grass (Please no caps): ")
if choice==compchoice:
    print("Tie")
if choice=="fire" and compchoice=="water":
    print("You Lose")
if choice=="water" and compchoice=="grass":
    print("You Lose")
if choice=="grass" and compchoice=="fire":
    print("You Lose")
if choice=="water" and compchoice=="fire":
    print("You Win")
if choice=="grass" and compchoice=="water":
    print("You Win")
if choice=="fire" and compchoice=="grass":
    print("You Win")
