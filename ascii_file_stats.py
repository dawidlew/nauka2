# coding=utf-8
import argparse
import collections
import string

parser = argparse.ArgumentParser()

parser.add_argument("--sort", type=str,
                    help="How to sort the characters?",
                    required=False)
parser.add_argument("--filepath", type=str,
                    help="Path to the file",
                    required=False)

args = parser.parse_args()

def stat(path):
    file_h = open(path, 'r')
    c = collections.Counter(file_h.read())
    for letter in string.printable:
        if c[letter] > 0:
            if letter not in string.whitespace:
                # (lista i pózniej sortowanie i dopiero wyswietlenie- osobna funkcja i zwrot)
                print ord(letter)
                print '%s : %d' % (letter, c[letter])
            file_h.close()

if not args.filepath:
    path = raw_input('Please input path and name of the file > ')
    stat(path)
else:
    stat(args.filepath)
