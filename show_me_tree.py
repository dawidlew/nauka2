import argparse
import sys
import os

parser = argparse.ArgumentParser()

parser.add_argument("--high", type=int,
                    help="Display a hight of a tree",
                    required=True)
parser.add_argument("--char", type=str,
                    help="Display a symbol of a tree",
                    default="'Brak symbolu!'",
                    required=True,
                    choices=("*", "@", "#", "o", "O", "0", "8"))
parser.add_argument("--savetofile",type=str,
                    help="Path to the file",
                    required=False)

args = parser.parse_args()

def writer(aaa, bbb):
    os.chdir(bbb)
    file = open(str(args.high) + ".txt", "w")
    file.write(bbb)
    file.close()
    print choinka()

def exit(wys):
    print '[ERROR] Unexpected height: ' + wys
    sys.exit(3)

def choinka():
    n = 3 + (args.high * 2)
    print args.char.center(n)
    for i in xrange(1, args.high):
        j = i * 2
        print ((j + 1) * args.char).center(n)
    print ('|').center(n)
    print ('^').center(n)

def wysokosc(katalog):
    if 3 <= args.high <= 24:
        writer(args.high, katalog)
    elif 0 <= args.high <= 2:
        exit(args.high)
        sys.exit(1)
    elif args.high > 24:
        exit(args.high)
        sys.exit(1)

if not args.savetofile:
    directory = raw_input('Please input directory for output file > ')
    wysokosc(directory)
else:
    wysokosc(args.savetofile)

