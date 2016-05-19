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

def file(path):
    file_h = open(path, 'r')
    col = collections.Counter(file_h.read())
    file_h.close()
    stat(col)

def stat(col):
    for letter in string.printable:
        if col[letter] > 0:
            if letter not in string.whitespace:
                # (lista i pózniej sortowanie i dopiero wyswietlenie- osobna funkcja i zwrot) + osobna funkcja na czytanie pliku- rozdzielić to na na więcej

                print ord(letter)
                print '%s : %d' % (letter, col[letter])


if not args.filepath:
    path = raw_input('Please input path and name of the file > ')
    file(path)
else:
    file(args.filepath)
