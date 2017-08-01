import sys
import re
from pprint import pprint

def load_data(filepath):
    pass


def get_most_frequent_words(text):
    pass


if __name__ == '__main__':
    dictionary = {}
    text_chunk = u''
    with open('text.txt', 'r', encoding='utf-8') as file_descriptor:
        while True:
            buff = file_descriptor.read(100)
            if not buff:
                break
            text_chunk = text_chunk + buff
            while True:
                re_match = re.match('\S+\s+', text_chunk)
                if re_match:
                    word = re_match.group(0).strip()
                    text_chunk = text_chunk[len(re_match.group(0)):]
                    if word in dictionary:
                        dictionary[word] += 1
                    else:
                        dictionary[word] = 1
                else:
                    break
    file_descriptor.close()
    print(dictionary)
