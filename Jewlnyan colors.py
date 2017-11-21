#John Heitz
#11/14/17
#A color thing
guesses=0
color="Rubinyan red"
while guesses<100:
    guess=input ("Choose one of  the colors of the jewlnyans:")
    if guess==color:
        print ("Yes it was Rubinyan red")
        break
    else:
        print("Try again")
    guesses=guesses+1
