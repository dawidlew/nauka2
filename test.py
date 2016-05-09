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


def proccess(args, directory):
    os.chdir(directory)
    file = open(str(args.high) + ".txt", "w")
    file.write("hello world in the new file " + directory)
    file.close()


if not args.savetofile:
    directory = raw_input('Please input directory for output file > ')

    try:
        proccess(args, directory)
    except:
        print "[ERROR] Problem with creating directory " + directory
        sys.exit(3)
else:
    try:
        proccess(args, args.savetofile)
    except:
        print "[ERROR] Problem with creating directory " + args.savetofile
        sys.exit(3)