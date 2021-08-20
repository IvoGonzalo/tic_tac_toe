logo = """
  _____ ___ ____   _____  _    ____   _____ ___  _____ 
 |_   _|_ _/ ___| |_   _|/ \  / ___| |_   _/ _ \| ____|
   | |  | | |       | | / _ \| |       | || | | |  _|  
   | |  | | |___    | |/ ___ \ |___    | || |_| | |___ 
   |_| |___\____|   |_/_/   \_\____|   |_| \___/|_____|

"""

game_over = """
   _____          __  __ ______    ______      ________ _____  
  / ____|   /\   |  \/  |  ____|  / __ \ \    / /  ____|  __ \ 
 | |  __   /  \  | \  / | |__    | |  | \ \  / /| |__  | |__) |
 | | |_ | / /\ \ | |\/| |  __|   | |  | |\ \/ / |  __| |  _  / 
 | |__| |/ ____ \| |  | | |____  | |__| | \  /  | |____| | \ \ 
  \_____/_/    \_\_|  |_|______|  \____/   \/   |______|_|  \_\
                                                               
                                                               
"""

print(logo)

print("********** WELCOME TO TIC-TAC-TOE GAME **********\n")
print("         X | 0 | X    1 | 2 | 3")
print("         - - - - -    - - - - -")
print("         X | 0 | X    4 | 5 | 6 ")
print("         - - - - -    - - - - -")
print("         X | 0 | X    7 | 8 | 9 \n")
print("THE GAME IS PLAYED WITH THE NUMERIC KEYPAD.\n")

tic_tac_toe = {
    '7': ' ', '8': ' ', '9': ' ',
    '4': ' ', '5': ' ', '6': ' ',
    '3': ' ', '2': ' ', '1': ' '
}


def print_game():
    print(tic_tac_toe['7'] + '  | ' + tic_tac_toe['8'] + ' | ' + tic_tac_toe['9'])
    print('-----------')
    print(tic_tac_toe['4'] + '  | ' + tic_tac_toe['5'] + ' | ' + tic_tac_toe['6'])
    print('-----------')
    print(tic_tac_toe['1'] + '  | ' + tic_tac_toe['2'] + ' | ' + tic_tac_toe['3'])


def play(player):

    game = str(input(f"\nIn what position are you going to put the {player}? "))

    try:
        if tic_tac_toe[game] == " ":
            tic_tac_toe[game] = player
        else:
            print("\nThis position is already filled please chose another one.\n")
            play(player)
    except KeyError:
        print("The number has to be between 1 and 9. Choose again.")
        play(player)


def check_score(score):
    if tic_tac_toe['7'] == tic_tac_toe['8'] == tic_tac_toe['9'] != ' ':
        print(f"\nTHE {tic_tac_toe['7']} WIN\n")
        print(game_over)
        return True
    elif tic_tac_toe['4'] == tic_tac_toe['5'] == tic_tac_toe['6'] != ' ':
        print(f"\nTHE {tic_tac_toe['4']} WIN\n")
        print(game_over)
        return True
    elif tic_tac_toe['1'] == tic_tac_toe['2'] == tic_tac_toe['3'] != ' ':
        print(f"\nTHE {tic_tac_toe['1']} WIN\n")
        print(game_over)
        return True
    elif tic_tac_toe['7'] == tic_tac_toe['4'] == tic_tac_toe['1'] != ' ':
        print(f"\nTHE {tic_tac_toe['7']} WIN\n")
        print(game_over)
        return True
    elif tic_tac_toe['8'] == tic_tac_toe['5'] == tic_tac_toe['2'] != ' ':
        print(f"\nTHE {tic_tac_toe['8']} WIN\n")
        print(game_over)
        return True
    elif tic_tac_toe['9'] == tic_tac_toe['6'] == tic_tac_toe['3'] != ' ':
        print(f"\nTHE {tic_tac_toe['9']} WIN\n")
        print(game_over)
        return True
    elif tic_tac_toe['7'] == tic_tac_toe['5'] == tic_tac_toe["3"] != ' ':
        print(f"\nTHE {tic_tac_toe['7']} WIN\n")
        print(game_over)
        return True
    elif tic_tac_toe['9'] == tic_tac_toe['5'] == tic_tac_toe["1"] != ' ':
        print(f"\nTHE {tic_tac_toe['9']} WIN\n")
        print(game_over)
        return True
    elif score == 9:
        print("\nIt's a tie.\n")
        print(game_over)
        return True


def play_game():
    score = 0
    current_player = "X"
    print_game()
    for i in range(10):
        play(current_player)
        score += 1
        if current_player == "X":
            current_player = "O"
        else:
            current_player = "X"
        print_game()
        if score >= 5:
            game_is_off = check_score(score)
            if game_is_off:
                break


play_game()
