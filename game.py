"""A number-guessing game."""
import random

name = raw_input("please enter your name: ")
print "Welcome to the guessing game {}, have fun" .format(name)

# make counter
#counter = 1
#num = random.randint(1, 100)
#user_guess = None
choice = 'y'
while choice == 'y':
    num = random.randint(1, 100)
    user_guess = None
    counter = 1
    while num != user_guess:
        try:
            user_guess = int(raw_input("Please enter your guess: "))
            if user_guess < 1 or user_guess > 100:
                print "Bad guess, select number between 1 -100"
                continue

            #Comparing user input:
            if user_guess < num:
                print "Your guess is too low, try again"
            elif user_guess > num:
                print "Your guess is too high. Try again."
            elif user_guess == num:
                print "Well done. {}! You found the number in {} tries.".format(name, counter)
            #choice = raw_input("Would you like to play again? Enter 'y' or 'n': ")
#while choice == 'y':
            counter = counter + 1
            if counter == 5:
                print "Too many tries"
                break
        except:
            print "Please enter a valid integer"
            continue
    choice = raw_input("Would you like to play again? Enter 'y' or 'n': ")
