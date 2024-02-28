import random
def initial_pencil_num():
    while True:
        try:
            number = int(input('How many pencils?\n'))
            if number == 0:
                print('The number of pencils should be positive')
            elif number < 0:
                raise ValueError
            else:
                return number
        except ValueError:
            print('The number of pencils should be numeric')


def validate_players(names):
    while True:
        player = input(f'Who will be the first ({', '.join(names)})\n')
        if player not in names:
            print(f'Choose between {" and ".join(names)}')
        else:
            return player


def switch_player(current_player, players):
    return [name for name in players if name != current_player][0]


def validate_turn(player, number):
    while True:
        try:
            turn = int(input(f"{player}'s turn!\n"))
            if turn not in range(1, 4):
                raise ValueError
            elif turn > number:
                print('Too many pencils were taken')
            else:
                return turn
        except ValueError:
            print("Possible values: '1', '2' or '3'")


def bot_turn(number):
    if number == 1:
        return 1
    return random.randint(1, 3) if number % 4 == 1 else (number - 1) % 4


def main():
    players = ['John', 'Jack']
    number = initial_pencil_num()
    current_player = validate_players(players)
    print(number * '|')

    while number > 0:
        if current_player == 'Jack':
            print("Jack's turn:")
            turn = bot_turn(number)
            print(turn)
        else:
            turn = validate_turn(current_player, number)
        number -= turn
        print(number * '|')
        if number == 0:
            print(f'{switch_player(current_player, players)} won!')
        else:
            current_player = switch_player(current_player, players)


main()
