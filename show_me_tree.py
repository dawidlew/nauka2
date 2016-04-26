import argparse
import sys

try:
    parser = argparse.ArgumentParser()
    parser.add_argument("--high", type=int,
                        help="Display a hight of a tree",
                        required=True)
    parser.add_argument("--char",type=str,
                        help="Display a symbol of a tree",
                        default="'Brak symbolu!'",
                        required=True,
                        choices=("*", "@", "#", "o", "O", "0", "8"))

    args = parser.parse_args()


    if 3 <= args.high <= 24:

        print args.char.center(120)

        for i in range(args.high):
            j = (i * 3)
            print (j * args.char).center(120)

        print ("|").center(120)
        print ("^").center(120)


    elif 0 <= args.high <= 2:
        sys.exit(1)

    elif args.high > 24:
        sys.exit(1)

    else:
        print "Blad"

except: print "Wprowadz poprawna wartosc!"

