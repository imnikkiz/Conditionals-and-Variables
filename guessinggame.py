import random

def check_guess(guess, correct):
    """ Compare guess to correct answer.
    Return False once guess is correct. 
    """

    if guess == correct:
        return False
    elif guess < 1 or guess > 100:
        print "Your guess is out of the range 1-100, try again."
    elif guess > correct:
        print "Your guess is too high, try again."
    else:
        print "Your guess is too low, try again."
    return True


def generate_guess(): 
    """ Check raw_input for valid guess format. 
    Return guess and number of guesses as a tuple.
    """ 
    count = 0

    while True:
        try: 
            guess = float(raw_input("What is your guess? > ")) 
            count += 1
            break
        except ValueError:
            print "Oops! That wasn't a number! Try again."
            count +=1

    return guess, count  # Return a tuple    

def play_game(player):
    """ Choose number randomly. Track guess and number of guesses
    until player guesses the correct number. Return number of guesses.
    """   
    print ("%s, I'm thinking of a number between 1 and 100. " 
           "Try to guess my number.") % player

    number = random.randrange(1,101) 
    total_number_of_tries = 0
    guessing = True

    while guessing:
        guess, guess_count = generate_guess()  # Unpack the returned tuple 
        total_number_of_tries += guess_count
        guessing = check_guess(guess, number)  # False = guess is correct

    print ("Well done, %s! You found my number "
           "in %d tries!") % (player, total_number_of_tries)
    return total_number_of_tries

def main():
    """ Greet player and track high score.

    Each round is instigated by play_game, and the round score is assigned to
    game_score. The highest score is tracked in main. Player may choose
    to continue playing. 
    """
    your_name = raw_input("Welcome to the guessing game! What is your name? > ")
    high_score = 1000
    playing = True    

    while playing:
        game_score = play_game(your_name)
        high_score = min(high_score, game_score)
        print "Your score is: ", game_score
        print "Best score is: ", high_score

        answer = raw_input("Would you like to play again? > ")
        if answer[0].upper() == "N":
            playing = False 


if __name__ == "__main__":
    main()
