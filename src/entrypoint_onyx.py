from src.helpers.argument_input_onyx import parse_inputs
from src.reset_tm_onyx import ResetTuringMachineSimulator


# Note on how to run the code
# You do python .\main.py .\input\reset_tm_ab_equal.csv [input string] (This is what I did on windows terminal)
# For linux terminal: python3 main.py input/reset_tm_ab_equal.csv [input string]

def main():
    """
    Entry point for the project2_toc package.
    """
    args = parse_inputs()
    resetTM = ResetTuringMachineSimulator(args.file)

    # Program 3 (TM with a reset direciton)
    resetTM.run(args.input_string)

    
