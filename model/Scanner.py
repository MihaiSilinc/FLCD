import re


keywords = []
separators = []
operators = []


class Scanner:

    def __init__(self) -> None:
        self.cases = []

    @staticmethod
    def readFile():
        with open('Token.in', 'r') as file:
            for i in range(8):
                separator = file.readline().strip()
                if separator == "space":
                    separator = " "
                separators.append(separator)
            for i in range(12):
                operators.append(file.readline().strip())
            for i in range(9):
                keywords.append(file.readline().strip())

    @staticmethod
    def getStringToken(line, index):
        token = ''
        quotes = 0
        while index < len(line) and quotes < 2:
            if line[index] == '\'':
                quotes += 1
            token += line[index]
            index += 1
        return token, index

    @staticmethod
    def isPartOfOperator(key):
        for operator in operators:
            if key in operator:
                return True
        return False

    def getOperatorToken(self, line, index):
        token = ''
        while index < len(line) and self.isPartOfOperator(line[index]):
            token += line[index]
            index += 1
        return token, index

    @staticmethod
    def checkIdentifier(token):
        return re.match(r'^[a-z]([a-zA-Z]|[0-9])*$', token) is not None

    @staticmethod
    def isConstant(token):
        return re.match(r'^(0|[+-]?[1-9][0-9]*)$|^\'.\'$|^\'.*\'$', token) is not None

    def tokenize(self, line):
        token = ''
        index = 0
        tokenList = []
        while index < len(line):
            if self.isPartOfOperator(line[index]):
                if token:
                    tokenList.append(token)
                token, index = self.getOperatorToken(line, index)
                tokenList.append(token)
                token = ''

            # elif line[index] == '\'':
            #     if token:
            #         tokenList.append(token)

            elif line[index] in separators:
                return
            else:
                token += line[index]
                index += 1
        if token:
            tokenList.append(token)
        return tokenList
