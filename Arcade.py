print("Welcome to the John Heitz arcade the date is 11/21/2017. Your game choices are: Anime Quiz, Missle Launch, Norwegen Blue Parrot, Combo Lock, and Silly Sentance Generator 3000")
game=input("Choose one of the games I've listed. Please include caps: ")
if game=="Anime Quiz":
    Q1="Emenyan"
    Q1G= input("Who is the jewlnyan with the healing spirit attack:")
    if Q1==Q1G:
        print("Correct. Moving on to the next question")
        Q2="Victini"
        Q2G= input("Who is the pokemon that is number 0 in the Unava pokedex:")
        if Q2==Q2G:
            print("Correct. Moving on to the next question")
            Q3="Kabuking"
            Q3G= input("Who is the owner of Gera-Gera resort in yo kai watch psychic specters:")
            if Q3==Q3G:
                print("Correct. Moving on to the next question")
                Q4="Ghost and Fairy"
                Q4G= input("What types are Mimikyu:")
                if Q4==Q4G:
                    print("Correct. You win")
                else:
                    print("You Fail")
            else:
                print("You Fail")    
        else:
            print("You Fail")
    else:
        print("You Fail")

if game=="Missle Launch":
    import time
    name="Rubinyan"
    password="RubyBoogie"
    print("WELCOME TO MISSILE TRON. IF YOU GET THE NAME AND PASSWORD YOU WIN.")
    name_guess=input("GIVE ME YOUR NAME:")
    password_guess=input("GIVE ME YOUR PASSWORD:")
    if name==name_guess and password==password_guess:
        print("ACCESS GRANTED")
    else:
        print("YOU ARE D-")
        time.sleep(1)
        print("E-")
        time.sleep(1)
        print("D DEAD")
if game=="Norwegen Blue Parrot":
    import random
    print ("Welcome to the dead parrot guessing game")
    print("""You walk into an old smelly pet shop.
    You see a butiful parrot who has 4 identical twins
     MM    
    /OO\\
    \\   >
    /  /
    \\ / 
     mm

     MM
    /OO\\
    \\   >
    /  /
    \\ / 
     mm

     MM
    /OO\\
    \\   >
    /  /
    \\ / 
     mm

     MM
    /OO\\
    \\   >
    /  /
    \\ / 
     mm

     MM
    /OO\\
    \\   >
    /  /
    \\ / 
     mm
     
    and a sign says if you guess the age of Davey you can keep all of them along with enough parrot food for life.
    The age is between 1 and 20
    You get 5 guesses""")
    guesses=0
    age=random.randint(1,20)
    while guesses<5:
        guess = input("Choose an age: ")
        guess=int(guess)
        if guess==age:
            print ("You win")
            break
        else:
            if guess < age:
                print("Too low")
            else:
                print("Too high")
            print ("You duckish ducky duck you will never get it right")
            guesses=guesses+1
    print("Good job whats your face")
    print("The answer was " , age)
if game=="Combo Lock":
    import random
    print("WELCOME TO COMBOTRON")
    print("WE COME UP WITH A 4 DIGIT CODE FOR YOU TO CRACK. YOU GET 5 GUESSES PER NUMBER")
    Guesses_dig_1=0
    Guesses_dig_2=0
    Guesses_dig_3=0
    Guesses_dig_4=0
    Digit_1=random.randint(0,9)
    Digit_2=random.randint(0,9)
    Digit_3=random.randint(0,9)
    Digit_4=random.randint(0,9)
    print("CODE MADE SOLVE NOW")
    while Guesses_dig_1<5:
        guess_dig_1 = input("DIGIT ONE NOW:")
        guess_dig_1=int(guess_dig_1)
        Guesses_dig_1=Guesses_dig_1+1
        if guess_dig_1==Digit_1:
            print ("DIGIT ONE SOLVED")
            break
        else:
            if guess_dig_1 < Digit_1:
                print("A LITTLE HIGHER")
            else:
                print("LESS")
            print ("TRY AGAIN")
    while Guesses_dig_2<5:
        guess_dig_2 = input("DIGIT TWO NOW:")
        guess_dig_2=int(guess_dig_2)
        Guesses_dig_2=Guesses_dig_2+1
        if guess_dig_2==Digit_2:
            print ("DIGIT TWO SOLVED")
            break
        else:
            if guess_dig_2 < Digit_2:
                print("A LITTLE HIGHER")
            else:
                print("LESS")
            print ("TRY AGAIN")
    while Guesses_dig_3<5:
        guess_dig_3 = input("DIGIT THREE NOW:")
        guess_dig_3=int(guess_dig_3)
        Guesses_dig_3=Guesses_dig_3+1
        if guess_dig_3==Digit_3:
            print ("DIGIT THREE SOLVED")
            break
        else:
            if guess_dig_3 < Digit_3:
                print("A LITTLE HIGHER")
            else:
                print("LESS")
            print ("TRY AGAIN")
    while Guesses_dig_4<5:
        guess_dig_4 = input("DIGIT FOUR NOW:")
        guess_dig_4=int(guess_dig_4)
        Guesses_dig_4=Guesses_dig_4+1
        if guess_dig_4==Digit_4:
            print ("DIGIT FOUR SOLVED.")
            break
        else:
            if guess_dig_4 < Digit_4:
                print("A LITTLE HIGHER")
            else:
                print("LESS")
            print ("TRY AGAIN")
    if (Guesses_dig_1+Guesses_dig_2+Guesses_dig_3+Guesses_dig_4)>19:
        print("YOU LOSE")
    else:
        print("GOOD JOB")
if game=="Silly Sentence Generator 3000":
    print("*"*48)
    print("*Welcome to Silly Sentence Generator 3000*")
    print("*"*48)
    player_name= input("Enter your name yall: ")
    message= "Sup " +player_name+ "! lets do dis"
    print(message)
    word_1= input("Enter a name: ")
    word_2= input("Enter a verb: ")
    word_3= input("Enter a animal: ")
    word_4= input("Enter a adjective: ")
    word_5= input("Enter a food: ")
    word_6= input("Enter a job: ")
    print (word_1 + " ate " + word_5 + " while doing it " + word_4 + " and " + word_2 + " then " + word_1 + " went to do its job as a " + word_6 + ". But then got trampled by a herd of " + word_3)


    
    







    
