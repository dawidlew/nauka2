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
parser.add_argument("--savetofile", type=str,
                    help="Path to the file",
                    required=False)

args = parser.parse_args()

def writer(args, directory):
    file_name = str(args.high) + ".txt"
    try:
        os.chdir(directory)
        file_h = open(file_name, "w")
        tree = choinka(args)
        file_h.write(tree)
        file_h.close()
        print tree
    except (IOError, OSError):
        print 'Unable to write to file ' + directory + file_name
        sys.exit(4)

def exit(wys):
    print '[ERROR] Unexpected height: ' + str(wys)
    sys.exit(3)


def choinka(args):
    n = 3 + (args.high * 2)
    var = args.char.center(n) + "\n"
    for i in xrange(1, args.high):
        j = i * 2
        var= var + ((j + 1) * args.char).center(n) + "\n"
    var = var + ('|').center(n) + "\n"
    var = var + ('^').center(n) + "\n"
    return var


def wysokosc(katalog, args):
    if 3 <= args.high <= 24:
        writer(args, katalog)
    elif 0 <= args.high <= 2:
        exit(args.high)
        sys.exit(1)
    elif args.high > 24:
        exit(args.high)
        sys.exit(1)

if not args.savetofile:
    directory = raw_input('Please input directory for output file > ')
    wysokosc(directory, args)
else:
    wysokosc(args.savetofile, args)
