import argparse
import sys

parser = argparse.ArgumentParser()
parser.add_argument("--high", type=int,
                    help="Display a hight of a tree",
                    required=True)
parser.add_argument("--char", type=str,
                    help="Display a symbol of a tree",
                    default="'Brak symbolu!'",
                    required=True,
                    choices=("*", "@", "#", "o", "O", "0", "8"))
parser.add_argument("--savetofile", type=str)

args = parser.parse_args()

def choinka(high):
    n = 3 + (high * 2)
    print args.char.center(n)
    for i in xrange(1, high):
        j = i * 2
        print ((j + 1) * args.char).center(n)
    print ('|').center(n)
    print ('^').center(n)

if 3 <= args.high <= 24:
    choinka(args.high)

elif 0 <= args.high <= 2:
    sys.exit(1)

elif args.high > 24:
    sys.exit(1)

else:
    print "Blad"

