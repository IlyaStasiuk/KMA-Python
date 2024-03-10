def output_to_console(text: object) -> object:
    """
    Outputs text to the console.
    """
    print(text)

def write_to_file_builtin(filename, text):
    """
    Writes to a file using built-in Python functionalities.
    """
    with open(filename, 'a') as file:
        file.write(text + '\n')
