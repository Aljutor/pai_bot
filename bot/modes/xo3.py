import math
from random import choice
import platform
from os import system

import math
from random import choice
import platform
from os import system

class TicTac3X3:
    human_choice = 'X'
    computer_choice = 'O'
    def __init__(self):
        self.board = [
            [0,0,0],
            [0,0,0],
            [0,0,0],
        ]

        # choise can be X or O
        human_choice = 'X'
        computer_choice = 'O'

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
        line = ''
        line += " | 1 || 2 || 3 |\n-----------------\n"
        r = 0
        for row in state:
            line +=(chr(r + ord('A')))
            for cell in row:
                if cell == -1:
                    line += '| X |'
                elif cell == +1:
                    line += '| O |'
                else:
                    line += '|   |'
            line +=('\n-----------------\n')
            r+=1
        return line
        
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
        if len(self.empty_cells(self.board)) == 9:
            x = choice([0, 1, 2])
            y = choice([0, 1, 2])
        else:
            move = self.minimax(self.board, len(self.empty_cells(self.board)), self.COMPUTER)
            x, y = move[0], move[1]

        self.set_move(x, y, self.COMPUTER)

    def xo_bot(self, position):
        position = position.upper().split()

        try:
            if len(position) == 2:
                x = ord(position[0]) - ord('A')
                y = int(position[1])

            elif len(position) == 1:
                x = ord(position[0][0]) - ord('A')
                y = int(position[0][1:])
            else:
                return False
        except:
            return False

        move = 0
        if x == 0:
            move = x + y
        elif x == 1:
            move = x*3 + y
        else:
            move = x*3 + y
        #valid moves
        moves = {
            1: [0, 0], 2: [0, 1], 3: [0, 2],
            4: [1, 0], 5: [1, 1], 6: [1, 2],
            7: [2, 0], 8: [2, 1], 9: [2, 2],
        }

        human_choice = 'X'
        computer_choice = 'O'

        if not self.game_over_all(self.board) and len(self.empty_cells(self.board)) > 0:
            if move > 0 or move < 10:
                coord = moves[move]
                try_move = self.set_move(coord[0], coord[1], self.HUMAN)
                if try_move == False:
                    print('Bad move')
                    move = 0
            if try_move == True:
                self.aiturn()
                return True
            else:
                return False
                
    def getWin(self):
        if self.game_over_all(self.board) or len(self.empty_cells(self.board)) == 0:
            if self.game_over(self.board, self.HUMAN):
                return 'Human wins'
            elif self.game_over(self.board, self.COMPUTER):
                self.render(self.board)
                return 'Bot wins'
            else:
                self.render(self.board)
                return 'Draw'
        else:
            return None
        
    def getGameState(self):
        strr = ' '
        strr += '| 1 || 2 || 3 |' + '\n' + '-----------------' + '\n'
        r = 0
        for row in self.board:
            strr +=(chr(r + ord('A')))
            for cell in row:
                if cell == -1:
                    strr += '| X |'
                elif cell == +1:
                    strr += '| O |'
                else:
                    strr += '|   |'
            strr +=('\n-----------------\n')
            r+=1
        return strr