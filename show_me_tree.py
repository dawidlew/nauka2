import argparse
import sys


parser = argparse.ArgumentParser()
parser.add_argument("--high", type=int,
                    help="display a high of a tree",
                    required=True)
parser.add_argument("--symbol",type=str,
                    help="display a symbol of a tree",
                    default="'Brak symbolu!'",
                    required=True)
# parser.add_argument("--invert")

args = parser.parse_args()
symbole = ("*", "@", "#", "o", "O", "0", "8")

if 3 <= args.high <= 24 and args.symbol in symbole:
    # print "The high of a tree equals {} and symbol is {}.".format(args.high, args.symbol)

    for i in range(args.high):
        j = (i * 2)
        print (j * args.symbol).center(120)

    print ("|").center(120)
    print ("^").center(120)


elif 0 <= args.high <= 2:
    sys.exit(1)
    # print "echo $?"

elif args.high > 24:
    sys.exit(1)

elif args.symbol not in symbole:
     sys.exit(2)

else:
    print "Blad"


