import pandas as pd

def input_from_console():
    """
    Inputs text from the console.
    """
    return input("Enter some text: ")

def read_from_file_builtin(filename):
    """
    Reads from a file using built-in Python functionalities.
    """
    with open(filename, 'r') as file:
        return file.read()

def read_from_file_pandas(filename):
    """
    Reads from a file using the Pandas library.
    """
    return pd.read_csv(filename).to_string()
