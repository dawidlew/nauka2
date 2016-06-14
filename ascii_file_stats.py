# coding=utf-8
import argparse
import collections
import string
import os
import sys
import mimetypes
import math
import re



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
                results[ord(letter)] = col[letter]
    return results



def prepare_list_words(path, rows=ROWS_COUNT):
    if rows:
        content = read_file_content(path)
        words = re.findall(r'\S+', content)
        wc = collections.Counter(words)

        print_sorted_list_words(wc.items(), rows=ROWS_COUNT, columns=0)


def print_sorted_list_words(data, rows=0, columns=0):
    if rows:
        lines = {}
        for count, item in enumerate(data):
            lines.setdefault(count % rows, []).append(item)
        for key, value in lines.items():
            for item in value:
                print '{:<15}: {:}'.format((item[0]), item[1]),
            print
    elif columns:
        for count, item in enumerate(data, 1):
            print item,
            if count % columns == 0:
                print
    else:
        print data

def prepare_list(path, sort_by_freq=False):
    content = read_file_content(path)
    stats_results = stat(content)

    if sort_by_freq:
        sorted_dict = sorted(stats_results.items(), key=lambda item: item[1], reverse=True)
    else:
        sorted_dict = sorted(stats_results.items())

    ascii_sorted_dict = collections.OrderedDict(sorted_dict)

    dict_len = len(ascii_sorted_dict)
    cols_count = dict_len / (ROWS_COUNT * 1.0)
    cols_cnt = int(myround(cols_count))

    collection = ascii_sorted_dict.items()
    print_sorted_list(collection, rows=ROWS_COUNT, columns=cols_cnt)


# Poniższa funkcja print_sorted_list drukuje rekordy wierszami, więc nie potrzebne jest wyliczanie liczby kolumn i elif columns- kod mozna kiedyś uproscić


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



def myround(value):
   return int(math.ceil(value))

def validate_by_size(path):
    return 0 < os.path.getsize(path) <= 102400

def validate_by_type(path):
    return mimetypes.guess_type(path)[0] == 'text/plain'


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument("--sort", type=str,
                        help="How to sort the characters? [freq]",
                        required=False)
    parser.add_argument("--words", type=str,
                        help="How many words are it? [count]",
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
            if args.sort == 'freq':
                prepare_list(path, True)
            elif args.words == 'count':
                prepare_list_words(path)
            else:
                prepare_list(path)
        else:
            print "The file isn't a text file. Please give a text file."
            sys.exit(6)
    else:
        print "File' size isn't proper (0.1-102kb). Try with another file."
        sys.exit(5)
