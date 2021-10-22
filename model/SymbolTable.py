from model.SortedList import AlphabeticallySortedList


class SymbolTable:

    def __init__(self):
        self.symbolTable = AlphabeticallySortedList()

    def search(self, value):
        return self.symbolTable.search(value)

    def insert(self, value):
        return self.symbolTable.insert(value)

