class Pif:
    def __init__(self):
        self.content = []

    def add(self, token, position):
        self.content.append((token, position))

    def __str__(self):
        result = ""
        for pair in self.content:
            result += pair[0] + "->" + str(pair[1]) + "\n"
        return result
