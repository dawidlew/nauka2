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

def writer(high, directory):
    os.chdir(directory)
    file = open(str(args.high) + ".txt", "w")
    file.write(directory)
    print >>file, choinka(high)
    file.close()

def wyjatek(katalog):
    print "[ERROR] Problem with creating directory " + katalog
    sys.exit(3)

def choinka(high):
    n = 3 + (high * 2)
    print args.char.center(n)
    for i in xrange(1, high):
        j = i * 2
        print ((j + 1) * args.char).center(n)
    print ('|').center(n)
    print ('^').center(n)



if not args.savetofile:
    try:
        if 3 <= args.high <= 24:
            directory = raw_input('Please input directory for output file > ')
            writer(args.high, directory)

        elif 0 <= args.high <= 2:
            sys.exit(1)

        elif args.high > 24:
            sys.exit(1)
    except:
        # wyjatek(directory)
        print "1"
else:
    try:
        if 3 <= args.high <= 24:
            writer(args.high, args.savetofile)

        elif 0 <= args.high <= 2:
            sys.exit(1)

        elif args.high > 24:
            sys.exit(1)

    except:
        # wyjatek(args.savetofile)
        print "2"
