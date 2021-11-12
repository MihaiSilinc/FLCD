from finiteAutomata import FiniteAutomata

class Console:

    def __init__(self):
        self.finiteAutomata = FiniteAutomata()

    def displayMenu(self):
        print("1.Display FA")
        print("2.Read from file")
        print("3.Check if DFA")
        print("4.Check if sequence is accepted by FA")

    def readFromFile(self):
        filename = "fa.in"
        self.finiteAutomata.readFA(filename)

    def displayFiniteAutomata(self):
        print(self.finiteAutomata)

    def checkDFA(self):
        print(self.finiteAutomata.isDFA() is True)

    def checkAccepted(self):
        sequence = input("Write the sequence separated by spaces >>>")
        seq = sequence.split(' ')
        print(self.finiteAutomata.checkAcceptedSequence(seq) is True)

    def run(self):
        options = {'1':self.displayFiniteAutomata,
                   '2':self.readFromFile,
                   '3':self.checkDFA,
                   '4':self.checkAccepted}

        while True:
            self.displayMenu()
            option = input(">>")
            if option in options.keys():
                options[option]()
            elif option == "q":
                break
            else:
                print("Invalid option")

c = Console()
c.run()