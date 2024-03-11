import random
import string


def generate_random_char():
    all_chars = string.ascii_letters + string.digits + string.punctuation
    return random.choice(all_chars)


def scramble_string(input_str):
    # Shuffle the input characters
    char_list = list(input_str)
    random.shuffle(char_list)

    # Maintain conditions: No consecutive repeats, no leading uppercase, no trailing punctuation
    prev_char = ''
    output_chars = []
    for char in char_list:
        if char.isupper() and len(output_chars) == 0:
            output_chars.append(char.lower())
        elif char != prev_char and not (prev_char.isalpha() and char.isalpha()) and not (
                prev_char.isdigit() and char.isdigit()) and not (
                prev_char in string.punctuation and char in string.punctuation):
            output_chars.append(char)
            prev_char = char

    # Pad or truncate the output to be exactly 15 characters long
    if len(output_chars) < 15:
        additional_chars = 15 - len(output_chars)
        for _ in range(additional_chars):
            output_chars.append(generate_random_char())
    elif len(output_chars) > 15:
        output_chars = output_chars[:15]

    scrambled_line = ''.join(output_chars)
    return scrambled_line


while True:
    # Input line to scramble
    input_line = input("Enter line to scramble: ")

    if not input_line:
        break

    # Scramble the input line
    scrambled_line = scramble_string(input_line)

    # Display the scrambled line
    print("Le Scrambled:", scrambled_line)