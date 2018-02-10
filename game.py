"""A number-guessing game."""
name = raw_input("please enter your name: ")
print "Welcome to the guessing game {}, have fun" .format(name)
import random

# make counter
counter = 1
num = random.randint(1, 100)
user_guess = None
while num != user_guess:
    user_guess = int(raw_input("Please enter your guess: "))

#while num != user_guess:
    if user_guess < num:
        print "Your guess is too low, try again"
    elif user_guess > num:
        print "Your guess is too high. Try again."
    else:
        print "Well done. {}! You found the number in {} tries.".format(name, counter)
    counter = counter + 1
