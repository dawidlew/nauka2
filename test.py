import argparse
import sys

parser = argparse.ArgumentParser()

parser.add_argument("--high", type=int,
                    help="Display a hight of a tree",
                    required=True)
parser.add_argument("--savetofile",type=str,
                    help="Path to the file",
                    required=False)

args = parser.parse_args()

prompt = '> Please input directory for output file:'

if not args.savetofile:
    print prompt

else:
    file = open(args.savetofile + str(args.high) + ".txt", "w")

    file.write("hello world in the new file")

    file.close()
