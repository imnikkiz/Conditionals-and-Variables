import random

def isCorrect(num, ans):
    '''compares guess (num) to correct answer (ans); 
    returning True continues guessing loop'''

    if num < 1 or num > 100:
        print "Your guess is out of the range 1-100, try again."
        return True
    elif num > ans:
        print "Your guess is too high, try again."
        return True
    elif num < ans:
        print "Your guess is too low, try again."
        return True
    else:
        return False


def generateGuess(count): 
    '''confirms guess (raw_input) is a valid number (converts to float); 
    returns updated count and guess once a valid float''' 

    while True:
        try: 
            guess = float(raw_input("What is your guess? ")) 
            break
        except ValueError:
            print "Oops! That wasn't a number! Try again."
            count +=1
    return count, guess     


def countGuesses(ans, name):
    '''begins counting guesses; calls generateGuess, then passes guess to isCorrect;
    returns count'''

    guessing = True
    count = 0
    while guessing:
        ck_guess = generateGuess(count)
        count = ck_guess[0]
        guess = ck_guess[1]           
        guessing = isCorrect(guess, ans)  #True or False
        count +=1
    print "Well done, %s!  You found my number in %d tries!" % (name, count)
    return count


def main():
    '''greets player; generates random number; 
    tracks high score; continues play loop until player responds no'''

    your_name = raw_input("Howdy what's your name?  ")
    highScore = 1000
    playing = True
    while playing:
        print "%s, I'm thinking of a number between 1 and 100. Try to guess my number." % your_name
        number = random.randrange(1,101)
        #print "answer:", number # shows answer for testing
 
        your_score = countGuesses(number, your_name)
        highScore = min(highScore,your_score)
        print "Your score is: ",your_score
        print "Best score is: ",highScore

        answer = raw_input("Would you like to play again?  ")
        if answer[0].upper() == "N":
            playing = False 


if __name__ == "__main__":
    main()
