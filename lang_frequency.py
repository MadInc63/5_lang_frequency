import re
import argparse
from collections import Counter


def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("file_path",
                        help="file path to find top ten words")
    return parser.parse_args()


def load_data(file_path):
    with open(file_path, 'r') as text_file:
        text_from_file = text_file.read()
    return text_from_file


def convert_to_lowercase(normal_text):
    return normal_text.lower()


def get_most_frequent_words(text):
    found_words = re.findall(r'\w+', text)
    number_of_output_word = 10
    most_common_words = Counter(found_words).most_common(number_of_output_word)
    return most_common_words


if __name__ == '__main__':
    try:
        file_path = create_parser().file_path
        load_text_from_file = load_data(file_path)
        lowercase_text = convert_to_lowercase(load_text_from_file)
        most_frequent_words = get_most_frequent_words(lowercase_text)
        print('Ten most repetitive words in the text and the number of their'
              ' repetitions:')
        for word, count in most_frequent_words:
            print('"{}" = {}'.format(word, count))
    except (IOError, FileNotFoundError):
        print('No such file or directory')
