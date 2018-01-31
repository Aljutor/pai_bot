class Matches():
    
    def __init__(self,initialAmount, maxAtTerm):
        self.amount = initialAmount
        self.max = maxAtTerm
        self.winner = None
    
    def sendUserMove(self,matches):
        try:
            matches = int(matches)

            if matches > 0 and matches <= self.max:
                self.amount -= matches
                self.makeMove()
                return True
            else:
                return False
        except:
            return False
        
    def getWin(self):
        return self.winner
    
    def getGameState(self):
        return self.amount
    
    def makeMove(self):
        if self.amount == 1:
            self.winner = 'You'
        else:
            if (self.amount - 1)%(self.max+1) == 0:
                self.amount -= 1
            else:
                if self.amount <= self.max + 1:
                    self.winner = 'Bot'
                self.amount -= (self.amount - 1)%(self.max+1)