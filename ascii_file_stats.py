# coding=utf-8
import argparse
import collections
import string
import os
import sys
import mimetypes

TV_rows = 23

def read_file_content(path):
    file_h = open(path, 'r')
    content = file_h.read()
    file_h.close()
    return content

def stat(content):
    results = {}
    col = collections.Counter(content)
    for letter in string.printable:
        if col[letter] > 0:
            if letter not in string.whitespace:
                # print '%s : %d, %d' % (letter, col[letter], ord(letter))
                results[ord(letter)] = col[letter]
    return results


def process(path):
    content = read_file_content(path)
    stats_results = stat(content)
    sorted_dict = sorted(stats_results.items())
    ascii_sorted_dict = collections.OrderedDict(sorted_dict)

    len_d = len(ascii_sorted_dict)
    while len_d <= TV_rows:
        for key, val in ascii_sorted_dict.items():
            character = str(chr(key)) + ': ' + str(val)
            print '{:<10}{:<10}{:<}'.format(character, character, character)
        len_d = len_d + 1


def validate_by_size(path):
    return 0 < os.path.getsize(path) <= 102400

def validate_by_type(path):
    return mimetypes.guess_type(path)[0] == 'text/plain'


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

    if validate_by_size(path):
        if validate_by_type(path):
            process(path)
        else:
            print "The file isn't a text file. Please give a text file."
            sys.exit(6)
    else:
        print "File' size isn't proper (0.1-102kb). Try with another file."
        sys.exit(5)

