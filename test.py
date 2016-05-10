import argparse
import sys
import os

parser = argparse.ArgumentParser()

parser.add_argument("--high", type=int,
                    help="Display a hight of a tree",
                    required=True)
parser.add_argument("--savetofile",type=str,
                    help="Path to the file",
                    required=False)

args = parser.parse_args()


def writer(high, directory):
    os.chdir(directory)
    file = open(str(args.high) + ".txt", "w")
    file.write("hello world in the new file " + directory)
    file.close()

def wyjatek(katalog):
    print "[ERROR] Problem with creating directory " + katalog
    sys.exit(3)


if not args.savetofile:
    directory = raw_input('Please input directory for output file > ')

    try:
        writer(args.high, directory)
    except:
        wyjatek(directory)
else:
    try:
        writer(args.high, args.savetofile)
    except:
        wyjatek(args.savetofile)

