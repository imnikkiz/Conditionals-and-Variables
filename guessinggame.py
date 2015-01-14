import random

name = raw_input("Howdy what's your name?  ")

playing = True
highScore = 1000

while playing:

    print "%s, I'm thinking of a number between 1 and 100. Try to guess my number." % name
    number = random.randrange(1,101)
    print "answer:", number # shows answer for testing

    guessing = True
    count = 1

    while guessing:
        try: 
            guess = float(raw_input("What is your guess? "))      
            if guess < 1 or guess > 100:
                print "Your guess is out of the range 1-100, try again."
            elif guess > number:
                print "Your guess is too high, try again."
            elif guess < number:
                print "Your guess is too low, try again."
            else:
                print "Well done, %s!  You found my number in %d tries!" % (name, count)
                guessing = False
            
        except ValueError:
            print "Oops! That wasn't a number! Try again."
        count +=1

    highScore = min(highScore,count)
    print "Your score is: ",count
    print "Best score is: ",highScore

    answer = raw_input("Would you like to play again?  ")
    if answer[0].upper() == "N":
        playing = False 