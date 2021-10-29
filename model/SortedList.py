
class AlphabeticallySortedList:

    def __init__(self):
        self.sortedList = []
        
    def __str__(self) -> str:
        result = "Symbol Table: \n"
        for i in range(len(self.sortedList)):
            result = result + str(i) + " -> " + str(self.sortedList[i]) + "\n"
        return result

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
                return index

            if value < self.sortedList[index]:
                self.sortedList.insert(index, value)
                return index

        # if it is not any of these cases, return last pos
        self.sortedList.append(value)
        return list_length - 1