from model.Pif import Pif
from model.Scanner import *
from model.SymbolTable import *


class Main:

    def __init__(self):
        self.symbolTable = SymbolTable()
        self.pif = Pif()
        self.scanner = Scanner()

    def readFile(self):
        with open('token.in', 'r') as file:
            for i in range(8):
                separator = file.readline().strip()
                if separator == "space":
                    separator = " "
                self.scanner.separators.append(separator)
            for i in range(14):
                self.scanner.operators.append(file.readline().strip())
            for i in range(12):
                self.scanner.keywords.append(file.readline().strip())

    def run(self, error=None):
        self.readFile()
        print(self.scanner.separators, self.scanner.operators, self.scanner.keywords)
        fileName = "p3.txt"
        tokensList = self.scanner.keywords + self.scanner.separators + self.scanner.operators
        error = ''
        with open(fileName, 'r') as file:
            lineIndex = 0
            for line in file:
                lineIndex += 1
                tokens = self.scanner.tokenize(line.strip())
                extra = ''
                for i in range(len(tokens)):
                    if tokens[i] in tokensList:
                        if tokens[i] == ' ':
                            continue
                        self.pif.add(tokens[i], -1)
                    elif self.scanner.checkIdentifier(tokens[i]):
                        identifier = self.symbolTable.insert(tokens[i])
                        self.pif.add("Identifier", identifier)
                    elif self.scanner.isConstant(tokens[i]):
                        constant = self.symbolTable.insert(extra+tokens[i])
                        extra = ''
                        self.pif.add("Constant", constant)
                    else:
                        error += 'Error at token ' + tokens[i] + ', line ' \
                                            + str(lineIndex) + "\n"

        with open('st.out', 'w') as w:
            w.write(str(self.symbolTable))

        with open('pif.out', 'w') as w:
            w.write(str(self.pif))

        if error is None:
            print("Lexically correct")
        else:
            print(error)


main = Main()
main.run()
