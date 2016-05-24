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
    #content = read_from_url(path)
    v = stat(content)
    b = sorted(v.items())
    v = collections.OrderedDict(b)
    print str(v)
    print str(v.items())
    for key, val in v.items():
        print str(chr(key)) + ': ' + str(val)


    # for el in v:
    #     print str(chr(el)) + ': ' + str(d[el])

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