
class AlphabeticallySortedList:

    def __init__(self):
        self.sortedList = []
        
    def __str__(self):
        return str(self.sortedList)

    def search(self, value):

        if value not in self.sortedList:
            return -1

        return self.sortedList.index(value)

    def insert(self, value):

        list_length = len(self.sortedList)
        if list_length == 0:
            self.sortedList.append(value)
            return 0  # position of first element
        
        for index in range(list_length):

            if value == self.sortedList[index]:
                return value

            if value < self.sortedList[index]:
                self.sortedList.insert(index, value)
                return index

        # if it is not any of these cases, return last pos
        self.sortedList.append(value)
        return list_length - 1


class SymbolTable:

    def __init__(self):
        self.symbolTable = AlphabeticallySortedList()

    def search(self, value):
        return self.symbolTable.search(value)

    def insert(self, value):
        return self.symbolTable.insert(value)

