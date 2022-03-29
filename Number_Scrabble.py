# The Author is Karim Ahed Tawfik Mohammad El-Habashy, 20210503
# Numble Scrabble Game
# Date: 27 Feb 2022
# 11410120210503@stud.cu.edu.eg


import random
from itertools import permutations

def players():
    global players, player_1, player_2
    players = [str(input("Please enter the first player's name: ")), str(input("Please enter the second player's name: "))]
    player_1 = random.choice(players)
    if player_1 == players[0]:
        player_2 = players[1]
    else:
        player_2 = players[0]
    return player_1, player_2

def get_input():
    global choice
    checker = False
    while checker is False:
        in_put = input("Please choose a number available in the list above: ")
        #Checks if the input integer
        if in_put.isdigit():
            choice = int(in_put)
            has_choice = choice in num #checks if the input is available list
            if has_choice is True:
                checker = True
            else:
                print("The entered value is not available ")
                print(f'Here are the available values {num}')
        else:
           print("The entered value in invalid. Please enter an integer")

    return choice


def check_winner(check_list):
    global win
    win = False
    sequence = permutations(check_list, 3)
    for p in list(sequence):
        if p[0] + p[1] + p[2] == 15:
            win = True
    return win


def game():
    global player_1_choices, player_2_choices, num
    num = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    player_1_choices = []
    player_2_choices = []
    players()
    print(f'{player_1} will have the first round')
    for i in range(1, 10):
        if i % 2 != 0:
            print("It's Player 1's turn")
            print(num)
            get_input()
            num.remove(choice)
            player_1_choices.append(choice)
            if len(player_1_choices) >= 3:
                check_list = player_1_choices
                check_winner(check_list)
                if win is True:
                    print(f'Congratulations, {player_1} won this game!!!! YAAAAY!')
                    quit()
        else:
            print("It's Player 2's turn")
            print(num)
            get_input()
            num.remove(choice)
            player_2_choices.append(choice)
            if len(player_2_choices) >= 3:
                check_list = player_2_choices
                check_winner(check_list)
                if win is True:
                    print(f'Congratulations, {player_2} won this game!!!! YAAAAAY!')
                    quit()
    print("Draw")


game()