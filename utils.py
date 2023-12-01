import sys
import pyperclip

def get_file_location():
    file_location = None
    if (len(sys.argv) >= 2):
        file_location = sys.argv[1]
    else:
        file_location = input(
            "Enter input file location: ")
    return file_location

def output_result(result):
    print(result)
    pyperclip.copy(result)
