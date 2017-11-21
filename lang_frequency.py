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
        lowercase_text = text_file.read().lower()
    return lowercase_text


def get_most_frequent_words(text):
    words_in_text = re.findall(r'\w+', text)
    words_count = Counter(words_in_text).most_common(10)
    return words_count



if __name__ == '__main__':
    try:
        file_path = parser_arg()
        text_from_file = load_data(file_path)
        top_10_words = get_most_frequent_words(text_from_file)
        print(top_10_words)
    except (IOError, FileNotFoundError):
        print('No such file or directory')
