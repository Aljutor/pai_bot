import math
from random import choice
import platform
from os import system

class AI:
    def __init__(self):
        self.board = [
            [0,0,0],
            [0,0,0],
            [0,0,0],
        ]

        # choise can be X or O
        human_choice = ''
        computer_choice = ''

        self.HUMAN = -1
        self.COMPUTER = +1

    def evaluate(self, state):
        if self.game_over(state, self.COMPUTER):
            score = +1
        elif self.game_over(state, self.HUMAN):
            score = -1
        else:
            score = 0

        return score


    def game_over(self, state, player):
        win_state = [
            [state[0][0], state[0][1], state[0][2]],
            [state[1][0], state[1][1], state[1][2]],
            [state[2][0], state[2][1], state[2][2]],
            [state[0][0], state[1][0], state[2][0]],
            [state[0][1], state[1][1], state[2][1]],
            [state[0][2], state[1][2], state[2][2]],
            [state[0][0], state[1][1], state[2][2]],
            [state[2][0], state[1][1], state[0][2]],
        ]

        if [player,player,player] in win_state:
            return True
        else:
            return False


    def game_over_all(self, state):
        return self.game_over(state, self.HUMAN) or self.game_over(state, self.COMPUTER)


    def empty_cells(self, state):
        cells = []

        for x, row in enumerate(state):
            for y, cell in enumerate(row):
                if cell == 0:
                    cells.append([x,y])

        return cells

    def valid_move(self, x,y):
        if [x, y] in self.empty_cells(self.board):
            return True
        else: 
            return False

    def set_move(self, x, y, player):
        if self.valid_move(x, y):
            self.board[x][y] = player
            return True
        else:
            return False

    def minimax(self, state, dept, player):
        if player == self.COMPUTER:
            best = [-1, -1, -math.inf]
        else:
            best = [-1, -1, +math.inf]

        if dept == 0 or self.game_over_all(state):
            score = self.evaluate(state)
            return [-1, -1, score]

        for cell in self.empty_cells(state):
            x, y = cell[0], cell[1]
            state[x][y] = player
            score = self.minimax(state, dept - 1, -player)
            state[x][y] = 0
            score[0], score[1] = x, y

            if player == self.COMPUTER:
                if score[2] > best[2]:
                    best = score  # max value
            else:
                if score[2] < best[2]:
                    best = score  # min value

        return best

    def render(self, state):
        print("  | A || B || C |\n-----------------")
        r = 0
        for row in state:
            r+=1
            print(r, end=' ')
            for cell in row:
                if cell == +1:
                    print('|', computer_choice, '|',end='')
                elif cell == -1:
                    print('|', human_choice, '|',end='')
                else:
                    print('|', ' ', '|',end='')
            print('\n-----------------')
        

    def clean(self):
        """
        Clears the console
        """
        osname = platform.system().lower()
        if 'windows' in osname:
            system('cls')
        else:
            system('clear')


    def aiturn(self):
        self.clean()
        print('Computer turn [{}]'.format(computer_choice))
        self.render(self.board)

        if len(self.empty_cells(self.board)) == 9:
            x = choice([0, 1, 2])
            y = choice([0, 1, 2])
        else:
            move = self.minimax(self.board, len(self.empty_cells(self.board)), self.COMPUTER)
            x, y = move[0], move[1]

        self.set_move(x, y, self.COMPUTER)

    def main(self):
        self.clean()
        global computer_choice, human_choice

        #valid moves
        moves = {
            1: [0, 0], 2: [0, 1], 3: [0, 2],
            4: [1, 0], 5: [1, 1], 6: [1, 2],
            7: [2, 0], 8: [2, 1], 9: [2, 2],
        }

        # moves = {
        #     A1: [0, 0], A2: [0, 1], A3: [0, 2],
        #     B1: [1, 0], B2: [1, 1], B3: [1, 2],
        #     C1: [2, 0], C2: [2, 1], C3: [2, 2],
        # }


        # Setting computer's choice
        human_choice = 'X'
        computer_choice = 'O'


        while not self.game_over_all(self.board) and len(self.empty_cells(self.board)) > 0:
            self.clean()
            print('Human turn [{}]'.format(human_choice))
            self.render(self.board)
            move = 0
            while move < 1 or move > 9:
                try:
                    move = int(input('Use numpad (A1..C3): '))
                    coord = moves[move]
                    try_move = self.set_move(coord[0], coord[1], self.HUMAN)

                    if try_move == False:
                        print('Bad move')
                        move = 0
                except KeyboardInterrupt:
                    print('Bye')
                    exit()
                except:
                    print('Bad choice')

            self.aiturn()

        if self.game_over(self.board, self.HUMAN):
            self.clean()
            print('Human turn [{}]'.format(human_choice))
            print('YOU WIN!')
        elif self.game_over(self.board, self.COMPUTER):
            self.clean()
            print('Computer turn [{}]'.format(computer_choice))
            self.render(self.board)
            print('YOU LOSE!')
        else:
            self.clean()
            self.render(self.board)
            print('DRAW!')

        exit()


if __name__ == '__main__':
    ai = AI()
    ai.main()