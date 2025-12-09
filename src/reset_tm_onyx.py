from src.helpers.turing_machine_onyx import TuringMachineSimulator

# ==========================================
# CONSTANTS
# ==========================================
BLANK = TuringMachineSimulator.BLANK 
DIR_L = TuringMachineSimulator.DIR_L
DIR_R = TuringMachineSimulator.DIR_R

# I worked on this.

class ResetTuringMachineSimulator(TuringMachineSimulator):
    def run(self, input):
        print(f"Machine: {self.machine_name}")
        print(f"Input: {input}")
        print(f"Start State: {self.start_state}\n")

        tapeList = list(input+BLANK) # Concatenate the input with a blank at the end and converts it to a list
        head_pos = 0 # Position of the head.
        step = 0
        found = False # Checks if the current state reached an accept or reject it can't loop infinitly
        currentState = self.start_state

        while(1):
            if step == 75: # This accounts for TM that may not halt. 
                break
            for t in self.transitions:
                if tapeList[head_pos] == t[1] and currentState == t[0]: # checks if the character matches 
                    #the transition character and if we are in the right state
                    tape = ''.join(tapeList) 
                    tape_line = ' '.join(tape)
                    caret_position = head_pos * 2
                    caret_line = ' ' * caret_position + '^' # Points to where the head is.
                    print(f"Step: {step}")
                    print(f"State: {currentState}")
                    print(tape_line)
                    print(caret_line)
                    
                    tapeList[head_pos] = t[3]
                    if t[4] == DIR_R: # checks if we need to move the head right on the tape or reset to the start.
                        head_pos+=1
                    else:
                        head_pos = 0
                    currentState = t[2]
                    if currentState == self.accept_state or currentState == self.reject_state:
                        found = True # Checks if we reached either the accept or reject state.
                    break
            if(found):
                break
            step+=1

        
        # Displays the result
        if currentState == self.accept_state:
            print("Result: Accepted")
        elif currentState == self.reject_state:   
            print("Result: Rejected")
        else:
            print("Stuck in a infinite loop and stopped")

  




