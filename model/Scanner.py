import re


class Scanner:

    def __init__(self):
        self.keywords = []
        self.separators = []
        self.operators = []

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

    def isPartOfOperator(self, key):
        for operator in self.operators:
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
        tokens = []
        while index < len(line):
            if self.isPartOfOperator(line[index]):
                if token:
                    tokens.append(token)
                token, index = self.getOperatorToken(line, index)
                tokens.append(token)
                token = ''  # reset token

            elif line[index] == '\'':
                if token:
                    tokens.append(token)
                token, index = self.getStringToken(line, index)
                tokens.append(token)
                token = ''  # reset token

            elif line[index] in self.separators:
                if token:
                    tokens.append(token)
                token, index = line[index], index + 1
                tokens.append(token)
                token = ''  # reset token

            else:
                token += line[index]
                index += 1
        if token:
            tokens.append(token)
        return tokens
