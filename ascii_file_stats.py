# coding=utf-8
import argparse
import collections
import string
import os


def read_file_content(path):
    file_h = open(path, 'r')
    content = file_h.read()
    file_h.close()
    return content

def stat(content):
    results = []
    col = collections.Counter(content)
    for letter in string.printable:
        if col[letter] > 0:
            if letter not in string.whitespace:
                print '%s : %d, %d' % (letter, col[letter], ord(letter))

                results.extend([letter, col[letter], ord(letter), os.linesep])

                results.sort()
            print results




def process(path):
    content = read_file_content(path)
    #content = read_from_url(path)
    stat(content)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument("--sort", type=str,
                        help="How to sort the characters?",
                        required=False)
    parser.add_argument("--filepath", type=str,
                        help="Path to the file",
                        required=False)
    args = parser.parse_args()

    path = args.filepath
    if path is None:
        path = raw_input('Please input path and name of the file > ')
    process(path)