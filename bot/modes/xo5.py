import numpy as np


class TicTac5X5():

    def __init__(self, sizeOfField, inArowToWin):
        self.field = np.array([['.']*sizeOfField]*sizeOfField)
        self.he = 'x'
        self.me = 'o'
        self.inARow = inArowToWin - 1
        self.size = sizeOfField
        self.winner = '.'

    def sendUserMove(self, position):
        position = position.upper()
        x = ord(position[0]) - ord('A')
        y = int(position[1:]) - 1
        if x < self.size and y < self.size and self.field[x][y] == '.':
            self.field[x][y] = self.he
            self.makeMove()
            return True
        else:
            return False

    def getWin(self):
        if self.winner == '.':
            return None
        else:
            return self.winner

    def makeMove(self):
        validSteps = {}
        for x in range(self.size):
            for y in range(self.size):
                if self.field[x][y] != '.':
                    if self.potential([x, y], self.field[x][y]) >= ((self.inARow+1)**(self.inARow+1))*10:
                        self.winner = self.field[x][y]
                    d = 2
                    u = 2
                    l = 2
                    r = 2
                    if x < 2:
                        l = x
                    if self.size - x <= 2:
                        r = self.size - x - 1
                    if y < 2:
                        u = y
                    if self.size - y <= 2:
                        d = self.size - y - 1
                    for i in range(x-l, x+r+1):
                        for j in range(y-u, y+d+1):
                            if self.field[i][j] == '.':
                                validSteps[(i, j)] = self.potential(
                                    [i, j], self.me)
        if validSteps:
            el = max(validSteps, key=validSteps.get)
            self.field[el[0]][el[1]] = self.me
            if self.potential([el[0], el[1]], self.field[el[0]][el[1]]) >= ((self.inARow+1)**(self.inARow+1))*10:
                self.winner = self.field[el[0]][el[1]]
        else:
            self.winner = 'Draw'

    def potentialOfLine(self, line, me, mid):
        if len(line) < self.inARow + 1:
            return 0
        he = 'x' if me == 'o' else 'o'
        line[mid] = me
        possible = False
        count = 1
        potential = 0
        for i in range(1, mid+1):
            if line[mid-i] != he:
                count += 1
            else:
                break
        for i in range(1, len(line)-mid):
            if line[mid+i] != he:
                count += 1
            else:
                break
        if count >= self.inARow + 1:
            for i in range(1, mid+1):
                if line[mid-i] == me:
                    potential += 1
                else:
                    break
            for i in range(len(line)-mid):
                if line[mid+i] == me:
                    potential += 1
                else:
                    break
            if potential == 1:
                potential = 0
        return potential**(self.inARow+1)

    def potential(self, position, me):
        x, y = position
        he = 'x' if me == 'o' else 'o'
        l = self.inARow
        r = self.inARow
        u = self.inARow
        d = self.inARow
        if x < self.inARow:
            l = x
        if self.size - x <= self.inARow:
            r = self.size - x - 1
        if y < self.inARow:
            d = y
        if self.size - y <= self.inARow:
            u = self.size - y - 1
        row = []
        line = []
        diag1 = []
        diag2 = []
        minLeftUp = l if l < u else u
        minLeftDown = l if l < d else d
        minRightUp = r if r < u else u
        minRightDown = r if r < d else d
        for j in range(x-l, x+r+1):
            line.append(self.field[j][y])
        for j in range(y-d, y+u+1):
            row.append(self.field[x][j])
        for j in range(-minLeftUp, minRightDown+1):
            diag1.append(self.field[x+j][y-j])
        for j in range(-minLeftDown, minRightUp+1):
            diag2.append(self.field[x+j][y+j])
        winPotential = self.potentialOfLine(row, me, d) + self.potentialOfLine(
            line, me, l) + self.potentialOfLine(diag1, me, minLeftUp) + self.potentialOfLine(diag2, me, minLeftDown)
        losePotential = self.potentialOfLine(row, he, d) + self.potentialOfLine(
            line, he, l) + self.potentialOfLine(diag1, he, minLeftUp) + self.potentialOfLine(diag2, he, minLeftDown)
        if winPotential >= (self.inARow+1)**(self.inARow+1):
            return winPotential*10
        if losePotential > winPotential:
            return losePotential
        else:
            return winPotential+1

    def getGameState(self):
        output = np.rot90(self.field, axes=(0, 1))
        string = '```\n   ' + \
            ' '.join([chr(x - 1 + ord('A')) for x in range(1, self.size+1)])
        nums = []
        for k in range(self.size, 0, -1):
            if k < 10:
                nums.append(str(k) + ' ')
            else:
                nums.append(str(k))
        string = string + '\n' + ('\n'.join([str(nums[x]) + '|' + '|'.join(
            [k for k in output[x]]) for x in range(self.size)])) + '\n```'
        return string
