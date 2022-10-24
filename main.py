
import random
import time
import keyboard

# ----- MYSTERY NUMBERS GAME ----- #

# INTRO

def game_start():

    print('Hello! Welcome to the Mystery Numbers game.\nPress SPACE to play, or press H for help!')
    while True:
        if keyboard.is_pressed('space'):
            break
        elif keyboard.is_pressed('h'):
            print('************************************** HELP ********************************************')
            print('Mystery Numbers is simple number guessing game. The game begins by the user entering a username\n'
                  'of their choosing and selecting a difficulty setting. Difficulty levels increase or decrease the\n'
                  'range of numbers used to play the game. For example \'Easy\' difficulty will make it so\n'
                  'the game will only ask the user to guess a number between 1 - 10, while \'Hard\' will ask\n'
                  'the user to guess a number between 1 - 30. If the user manages to guess the mystery number\n'
                  'correctly on the first try, they will be granted an extra attempt to their total number of\n'
                  'tries that carry over from round to round. A game will end after 5 rounds.')
            break


    user_name = input('Please enter your name!: ')
    print('\nAlright ' + user_name + ', please choose a difficulty. Hit the number on your keyboard that'
                                     ' corresponds with the difficulty setting you would like to choose.')
    print('1. Easy \n2. Medium \n3. Hard')
    while True:
        try:
            if keyboard.is_pressed('1'):
                return 1
            elif keyboard.is_pressed('2'):
                return 2
            elif keyboard.is_pressed('3'):
                return 3
        except:
            print('Please hit 1, 2, or 3 on your keyboard to choose difficulty.')


difficulty = game_start()

# FETCH RANGE OF NUMBERS THAT CORRELATES WITH DIFFICULTY SELECTED

def difficulty_numbers():

    easy = range(1, 11)
    medium = range(1, 21)
    hard = range(1, 31)

    if difficulty == 1:
        return easy
    elif difficulty == 2:
        return medium
    elif difficulty == 3:
        return hard


num_data = difficulty_numbers()

# START GAME

def game(cpu_number):

    cpu_banter = [
        'Hmmmmmm... Okay I have one!',
        'There\'s no way you\'re guessing this one...',
        'Good luck with this one!!!',
        'You really think you can outsmart me..?'
    ]

    tries = 0
    round_number = 1

    if cpu_number == range(1, 11):
        tries += 3
        print('\nOkay, I\'ll think of a number between 1 and 10.')
    elif cpu_number == range(1, 21):
        tries += 5
        print('\nOkay, I\'ll think of a number between 1 and 20.')
    else:
        tries += 7
        print('\nAre you sure you want to play on HARD? Alright.. I\'ll think of a number between 1 and 30.')

    try:

        while True:

            attempt_number = 0

            print('')
            print('\nROUND: ' + str(round_number))
            time.sleep(1)
            print('')
            print(random.choice(cpu_banter))
            time.sleep(1)
            cpu = random.choice(cpu_number)

            while True:
                print('\nYou currently have (' + str(tries) + ') tries left...')
                user_guess = input('\nType your guess and hit ENTER!: ')
                attempt_number += 1

                if int(user_guess) == cpu and attempt_number == 1:
                    print('You guessed the mystery number on your FIRST attempt!! Extra try added.')
                    tries += 1
                    round_number += 1
                    break
                elif int(user_guess) == cpu:
                    print('Congratulations! You guessed correctly.')
                    round_number += 1
                    break
                elif int(user_guess) < cpu:
                    time.sleep(1)
                    print('Too low.')
                    time.sleep(1)
                    tries -= 1
                elif int(user_guess) > cpu:
                    time.sleep(1)
                    print('Too high.')
                    time.sleep(1)
                    tries -= 1

                if round_number == 5 and tries > 0:
                    print('\nCongratulations! You won!')
                    time.sleep(1)
                    break
                elif tries < 1:
                    time.sleep(1)
                    print('\nYou ran out of attempts.. You lose!')
                    print('\nThe mystery number was ' + str(cpu))
                    break
            if round_number == 5 or tries < 1:
                break

    except:
        print('Please use numbers and wait for the prompts for your input! Restarting...')
        time.sleep(2)
        game(num_data)


# END GAME / PLAY AGAIN

while True:
    def end_game():

        print('\nWould you like to play again? Press Y for yes, or N for no.')
        while True:
            if keyboard.is_pressed('y'):
                break
            elif keyboard.is_pressed('n'):
                print('\nGoodbye!')
                time.sleep(1)
                quit()

    game(num_data)
    end_game()
