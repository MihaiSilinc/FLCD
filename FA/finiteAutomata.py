class FiniteAutomata:

    def __init__(self, Q=None, Sigma=None, delta=None, q0="", F=None):

        if F is None:
            F = []
        if delta is None:
            delta = {}
        if Sigma is None:
            Sigma = []
        if Q is None:
            Q = []

        self.Q = Q # states
        self.Sigma = Sigma # alphabet
        self.delta = delta # transition function
        self.q0 = q0 # initial state
        self.F = F # final set of states

    def isDFA(self):
        for k in self.delta.keys():
            if len(self.delta[k]) > 1:
                return False
        return True

    def checkAcceptedSequence(self, sequence):
        if self.isDFA():
            currentSymbol = self.q0
            for symbol in sequence:
                if (currentSymbol, symbol) in self.delta:
                    currentSymbol = self.delta[(currentSymbol, symbol)][0]
                else:
                    return False
            return currentSymbol in self.F
        return False

    def readFA(self, file):
        with open(file) as f:
            self.Q = f.readline()[2:].strip().split(',')
            self.Sigma = f.readline()[2:].strip().split(',')
            self.q0 = f.readline()[3:].strip()
            self.F = f.readline()[2:].strip().split(',')
            self.delta = {}

            for line in f.readlines():
                parts = line.split("=")
                symbol, path = tuple(parts[0][1:].strip("()").split(','))
                dest = parts[1].strip()
                if (symbol, path) not in self.delta:
                    self.delta[(symbol, path)] = [dest]
                else:
                    self.delta[(symbol, path)].append(dest)

    def __str__(self):
        return f"states (Q) : {self.Q}\nalphabet (sigma): {self.Sigma}\ntransition function (delta): {self.delta}\n" \
               f"initial state (q0): {self.q0}\nfinal states (F): {self.F}\n"
