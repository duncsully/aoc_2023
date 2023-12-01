from utils import get_file_location
from utils import output_result

file_location = get_file_location()

with open(file_location) as f:
    sum = 0
    for line in f:
        first_digit = 0
        last_digit = 0
        for char in line:
            if char.isdigit():
                first_digit = int(char)
                break
        for char in reversed(line):
            if char.isdigit():
                last_digit = int(char)
                break
        sum += first_digit * 10 + last_digit

output_result(sum)
        