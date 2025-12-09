import csv

class TuringMachineSimulator:

    # ==========================================
    # CONSTANTS
    # ==========================================
    BLANK = "_"   
    DIR_L = "L"
    DIR_R = "R"

    def __init__(self, filename):
        self.filename = filename
        self.machine_name = ""
        self.states = []
        self.sigma = []
        self.gamma = []
        self.start_state = ""
        self.accept_state = ""
        self.reject_state = ""
        
        # Structure: transition = ['state','sym','state','sym','DIR']
        self.transitions = []
        
        self.parseTM(filename)


    # Parse the TM file
    def parseTM(self, filename):
        with open(filename, newline='') as file:
            reader = csv.reader(file)
            for index, row in enumerate(reader):

                if(index == 0):
                    self.machine_name = row[0] # Get the name of the DFA
                elif(index == 1):
                    self.states =  row # Get the all of the states of the DFA
                elif (index == 2):
                    self.sigma = [symbol for symbol in row if symbol.strip() != ""] 
                    # The list comprehension removes extra spaces in the alphabet
                elif (index == 3):
                    self.gamma = [symbol for symbol in row if symbol.strip() != ""] 
                    # The list comprehension removes extra spaces in gamma
                elif (index == 4):
                    self.start_state = row[0] # Get the start state of the TM
                elif (index == 5):
                    self.accept_state = row[0]
                    # Get all the acceptState states
                    # The list comprehension removes extra spaces in the final states
                elif (index == 6):
                    self.reject_state = row[0]
                else:
                    self.transitions.append(row)

  




