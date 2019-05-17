import random
#starts programm

def start_game():
    name = input("What's your name?  ")
    print("===>HI {} WELCOME TO THE NUMBER GUESSING GAME!<===".format(name.upper()))
    number = random.randint(0, 10)
    number_of_guesses = []
    highscores = []

    while True:
        try:
            guess = int(input("What is your guess?  "))
        except ValueError:
            print("You did't guess a number, we are only guessing numbers at this point. Try again")
            continue
        if guess < 0 or guess > 10:
            print("You've chosen the number {}, and in this version of the game, we only accept numbers from 0 to 10".format(guess))
            continue
        elif guess == number:
            print("Amazing. You've guessed the correct number ({})".format(number))
            number_of_guesses.append("try")
            highscores.append(len(number_of_guesses))
            if len(number_of_guesses) == min(highscores):
                print("You have a new highscore: {} tries".format(min(highscores)))
            else:
                print("You've beat me in {} tries, but your current highscore is: {}".format(len(number_of_guesses),min(highscores)))
            try_again = input("Do you want to keep playing? Please write Y or N    ").lower()
            if try_again == "y":
                number_of_guesses = []
                number = random.randint(0, 10)
                continue
            else:
                print("Thanks for playing {}".format(name))
                break
        else:
            if guess < number:
                suggest = "higher"
            else:
                suggest = "lower"
            print("Muahhahhahah! You dind't guess! My number is {}!".format(suggest))
            number_of_guesses.append("try")
            continue

if __name__ == '__main__':
    # Kick off the program by calling the start_game function.
    start_game()
