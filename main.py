import random
import time  # For delay in each answer


def player_turn():

    while True:
        player_choice = input(
            '''
            **********************************
            
            Type your choice for start playing:

            Rock, Paper, Scissors, Lizard, Spock

            Type "rules" if you don't know them.

            **********************************\n
            '''
        ).lower()

        if player_choice == "rules":
            print(
                '''
                Just remeber what Sheldon says:

                Scissors cuts paper.
                Paper covers rock.
                Rock crushes lizard.
                Lizard poisons Spock.
                Spock smashes scissors.
                Scissors decapitates lizard.
                Lizard eats paper.
                Paper disproves Spock.
                Spock vaporizes rock.
                and as it always has...
                Rock crushes scissors.
                Now... Let's play!!
                
                '''
            )
            time.sleep(5)

        elif player_choice in ['rock', 'paper', 'scissors', 'lizard', 'spock']:
            print(f'You choose: {player_choice}\n')
            return player_choice
        else:
            print('\nSorry, your answer is not correct. Try again.\n')
            time.sleep(1)


def computer_turn():
    print('Computer is thinking...\n')
    time.sleep(2)

    choices = ['rock', 'paper', 'scissors', 'lizard', 'spock']
    computer_choice = random.choice(choices)
    print(f'Computer choose: {computer_choice.capitalize()}\n')
    return computer_choice


def check_winner(player_choice, computer_choice):
    time.sleep(2)

    win_options = {
        "rock": ["scissors", "lizard"],
        "paper": ["rock", "spock"],
        "scissors": ["paper", "lizard"],
        "lizard": ["paper", "spock"],
        "spock": ["scissors", "rock"]
    }

    if player_choice == computer_choice:
        print("Draw!")
        return
    elif computer_choice in win_options[player_choice]:
        print(f"You win!, {player_choice} beats {computer_choice}\n")
    else:
        print(f"You lose!, {computer_choice} beats {player_choice}\n")


if __name__ == "__main__":
    print(
        '''
        **********************************
        
        Welcome to the game of Rock, Paper, Scissors, Lizard, Spock!

        **********************************\n
        '''
    )

    while True:
        player_choice = player_turn()
        computer_choice = computer_turn()
        check_winner(player_choice, computer_choice)

        play_again = input(
            '''
            **********************************
            
            Do you want to play again?

            Type "yes" if you want to play again.

            Type "no" if you don't want to play again.

            **********************************\n
            '''
        ).lower()

        if play_again == "yes":
            continue
        elif play_again == "no":
            print(
                '''
                **********************************
                
                Thank you for playing!

                **********************************\n
                '''
            )
            break
        else:
            print(
                '''
                **********************************
                
                Sorry, your answer is not correct.

                Type "yes" if you want to play again.
                
                **********************************\n
                '''
            )
