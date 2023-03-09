import os
import re
from spellchecker import SpellChecker

spell = SpellChecker()


def correct_spelling(file_path):
    # create folder for corrected files if it doesn't exist
    if not os.path.exists('correct_files'):
        os.makedirs('correct_files')

    # open input file for reading
    with open(file_path, 'r') as file:
        text = file.read()

        # remove special characters and convert to lowercase
        text = re.sub(r'[^a-zA-Z0-9\s]', '', text)
        text = text.lower()

        # split text into words
        words = text.split()

        # create a new list of corrected words
        corrected_words = []
        for word in words:
            corrected_word = spell.correction(word)
            corrected_words.append(corrected_word)

        # join corrected words back into a sentence
        corrected_text = ' '.join(corrected_words)

        # print the corrected sentence
        print(corrected_text)

        # create output file path
        output_file_path = os.path.join(
            'correct_files', os.path.basename(file_path))

        # write corrected text to output file
        with open(output_file_path, 'w') as output_file:
            output_file.write(corrected_text)


# test the function with an input file
correct_spelling('test1.txt')
