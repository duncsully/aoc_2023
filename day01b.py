from utils import get_file_location
from utils import output_result

# "zero" is not included
number_words = ("one", "two", "three", "four", "five", "six", "seven", "eight", "nine")


def might_be_number_word(word: str):
    return any(word in number_word for number_word in number_words)
        

def get_digit_from_line(line: str, reverse = False):
    word = ''
    line_to_check = line if not reverse else line[::-1]
    for char in line_to_check:
        if char.isdigit():
            return int(char)
        word = word + char if not reverse else char + word
        if word in number_words:
            return number_words.index(word) + 1
        else:
            # threev: "v" is in "five" and "seven", "ev" is in "seven", 
            # but then "eev" is not in anything, though "ee" is in "three"
            while (not might_be_number_word(word)):
                word = word[1:] if not reverse else word[:-1]
        

file_location = get_file_location()

with open(file_location) as f:
    sum = 0
    for line in f:
        first_digit = get_digit_from_line(line)
        last_digit = get_digit_from_line(line, True)
        sum += first_digit * 10 + last_digit

output_result(sum)
        