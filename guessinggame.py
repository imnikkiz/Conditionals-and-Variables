import random

name = raw_input("Howdy what's your name?  ")
print "%s, I'm thinking of a number between 1 and 100. Try to guess my number." % name
number = random.randrange(1,101)
print "answer:", number

guessing = True
count = 1

while guessing:
    # while True:
    try: 
        guess = int(raw_input("What is your guess? "))
        # break
        if guess > number:
            print "Your guess is too high, try again."
        elif guess < number:
            print "Your guess is too low, try again."
        else:
            print "Well done, %s!  You found my number in %d tries!" % (name, count)
            guessing = False
            
    except ValueError:
        print "Oops! That wasn't a number! Try again."
    
    count +=1