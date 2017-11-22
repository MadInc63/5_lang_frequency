import re
import argparse
from collections import Counter


def parser_arg():
    parser = argparse.ArgumentParser()
    parser.add_argument("file_path",
                        help="file path to find top 10 words")
    args = parser.parse_args()
    return args.file_path


def load_data(file_path):
    with open(file_path, 'r') as text_file:
        text_from_book = text_file.read()
    return text_from_book


def convert_to_lowercase(normal_text):
    lowercase_text = normal_text.lower()
    return lowercase_text


def get_most_frequent_words(text):
    found_words_in_text = re.findall(r'\w+', text)
    word_counting_in_text = Counter(found_words_in_text).most_common(10)
    return word_counting_in_text


if __name__ == '__main__':
    try:
        file_path = parser_arg()
        load_text_from_file = load_data(file_path)
        text_to_lowercase = convert_to_lowercase(load_text_from_file)
        most_frequent_words = get_most_frequent_words(text_to_lowercase)
        for most_word in most_frequent_words:
            word, count = most_word
            print('The word "{}" occurs {} times in text'
                  .format(word, count))
    except (IOError, FileNotFoundError):
        print('No such file or directory')
