def guessing_game_functions(ulim, llim):

    import random

    name = raw_input("please enter your name: ")
    print "Welcome to the guessing game {}, have fun" .format(name)
    num = random.randint(llim, ulim)
    counter = 1
    return guess_number(num, name, counter, ulim, llim)


def guess_number(num, name, counter, ulim, llim):
    #counter = 1
    user_guess = None
    while num != user_guess:
        print counter
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
            if counter == 15:
                print "Too many tries"
                break
        except:
            print "Please enter a valid integer"
            continue
    fi_score = play_again(num, name, counter, ulim, llim)
    return fi_score


def play_again(num, name, counter, ulim, llim):
    choice = raw_input("Would you like to play again? Enter 'y' or 'n': ")
    while choice == 'y':
        guess_number(num, name, counter, ulim, llim)
    f_score = enter_range(counter, ulim, llim)
    return f_score


def enter_range(counter, ulim, llim):
    scores = 0
    if counter <= 5:
        scores = counter * 100
    if counter > 5 and counter <= 10:
        scores = counter * 50
    if counter > 10 and counter <= 15:
        scores = counter * 20
    #ask = raw_input("Please enter range of numbers from a start number to an end number: ")
    #ask_split = ask.split(',')
    #llim = ask_split[0]
    #ulim = ask_split[1]
    range_diff = (ulim - llim)
    if range_diff <= 20:
        final_score = scores * 0.33
    if range_diff > 20 and range_diff <= 50:
        final_score = scores * 0.50
    if range_diff > 50 and range_diff <= 80:
        final_score = scores * 0.75
    if range_diff > 80:
        final_score = scores * 1
    return final_score






trial = guessing_game_functions(70, 30)
print trial
