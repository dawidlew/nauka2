# coding=utf-8
import argparse
import collections
import string
import os
import sys



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
    print str(ascii_sorted_dict)
    print str(stats_results.items())
    for key, val in ascii_sorted_dict.items():
        print str(chr(key)) + ': ' + str(val)


def size(path):
    f_size = os.path.getsize(path)
    if 0 < f_size <=100000:
        process(path)
    else:
        print "File is too big. Try with another file."
        sys.exit(5)



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
    size(path)