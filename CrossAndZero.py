import random

# поле
board = [[' ' for _ in range(3)] for _ in range(3)]

# игроки
PLAYER_X = 'X'
PLAYER_O = 'O'

# текущий игрок и ход
current_player = PLAYER_X
turn = 0

# отображение игрового поля
def display_board():
    for row in board:
        print('| ' + ' | '.join(row) + ' |')

# проверка хода
def is_valid_move(position):
    if not 1 <= position <= 9:
        return False
    row = (position-1) // 3
    col = (position-1) % 3
    return board[row][col] == ' '

# выполнения хода
def make_move(position, player):
    row = (position-1) // 3
    col = (position-1) % 3
    board[row][col] = player

# проверка победы
def is_winning_move(player):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] == player:
            return True
        if board[0][i] == board[1][i] == board[2][i] == player:
            return True
    if board[0][0] == board[1][1] == board[2][2] == player:
        return True
    if board[0][2] == board[1][1] == board[2][0] == player:
        return True
    return False

# определение ничьей
def is_board_full():
    for row in board:
        for cell in row:
            if cell == ' ':
                return False
    return True

# определение хода компьютера
def computer_move():
    possible_moves = []
    for i in range(1, 10):
        if is_valid_move(i):
            possible_moves.append(i)
    chosen_move = random.choice(possible_moves)
    return chosen_move

# цикл игры
while True:
    # отображение игрового поля
    display_board()

    # ход игрока
    if current_player == PLAYER_X:
        position = int(input('Введите номер хода (1-9): '))
        while not is_valid_move(position):
            position = int(input('Неверный ход. Введите номер хода (1-9): '))
        make_move(position, current_player)

    # ход компьютера
    else:
        position = computer_move()
        make_move(position, current_player)

    # проверка победы
    if is_winning_move(current_player):
        display_board()
        print(f'Игрок {current_player} выиграл!')
        break

    # проверка ничьей
    if is_board_full():
        display_board()
        print('Ничья!')
        break

    # переключение хода
    turn += 1
    current_player = PLAYER_O if current_player == PLAYER_X else PLAYER_X
