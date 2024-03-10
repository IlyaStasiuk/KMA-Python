from app.io.input import input_from_console, read_from_file_builtin, read_from_file_pandas
from app.io.output import output_to_console, write_to_file_builtin

def main():
    console_input = input_from_console()
    file_input_builtin = read_from_file_builtin("data/sample.txt")
    file_input_pandas = read_from_file_pandas("data/sample.csv")

    output_to_console(console_input)
    output_to_console(file_input_builtin)
    output_to_console(file_input_pandas)

    write_to_file_builtin("data/output.txt", console_input)
    write_to_file_builtin("data/output.txt", file_input_builtin)
    write_to_file_builtin("data/output.txt", file_input_pandas)


if __name__ == "__main__":
    main()
