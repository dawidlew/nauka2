# coding=utf-8
import argparse
import collections
import string
import os
import sys
import mimetypes
import math

ROWS_COUNT = 23


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

    dict_len = len(ascii_sorted_dict)
    cols_count = dict_len / (ROWS_COUNT * 1.0)
    cols_cnt = int(myround(cols_count))

    # print "cols_cnt: %d" % cols_cnt
    # print 'ROWS_COUNT: %d' % ROWS_COUNT

    collection = ascii_sorted_dict.items()
    # print 'collection: %s' % collection

    print_sorted_list(collection, rows=ROWS_COUNT, columns=cols_cnt)

# Poniższa funkcja drukuje rekordy wierszami, więc nie potrzebne jest wyliczanie liczby kolumn i elif- kod mozna kiedyś uproscić


def print_sorted_list(data, rows=0, columns=0):
    if rows:
        lines = {}
        for count, item in enumerate(data):
            lines.setdefault(count % rows, []).append(item)
        for key, value in lines.items():
            for item in value:
                print '{}: {:<15}'.format(chr(item[0]), item[1]),
            print
    elif columns:
        for count, item in enumerate(data, 1):
            print item,
            if count % columns == 0:
                print
    else:
        print data

    #             for key, val in collection:
    #                 print '{:<10}'.format(str(chr(key)) + ': ' + str(val))




def myround(value):
   return int(math.ceil(value))

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

