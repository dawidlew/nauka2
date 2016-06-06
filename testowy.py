def print_sorted_list(data, rows=0, columns=0):
    """
    Prints sorted item of the list data structure formated using
    the rows and columns parameters
    """
    print the_list
    if not data:
        return

    if rows:
        # column-wise sorting
        # we must know the number of rows to print on each column
        # before we print the next column. But since we cannot
        # move the cursor backwards (unless using ncurses library)
        # we have to know what each row with look like upfront
        # so we are basically printing the rows line by line instead
        # of printing column by column
        lines = {}
        for count, item in enumerate(sorted(data)):
            lines.setdefault(count % rows, []).append(item)
        for key, value in sorted(lines.items()):
            for item in value:
                print '{:<10}'.format(item),
            print
    elif columns:
        # row-wise sorting
        # we just need to know how many columns should a row have
        # before we print the next row on the next line.
        for count, item in enumerate(sorted(data), 1):
            # print item,
            print '{:<10}'.format(str(chr(key)) + ': ' + str(value)),
            if count % columns == 0:
                print
    else:
        print sorted(data)  # the default print behaviour


if __name__ == '__main__':
    # the_list = ['apricot','banana','apple','car','coconut','baloon','bubble']
    the_list = [(46, 1), (48, 6), (49, 14), (50, 2), (51, 6), (52, 5), (53, 5), (54, 2), (55, 3), (56, 5), (57, 5), (65, 6), (68, 6), (69, 1), (70, 1), (91, 1), (93, 1), (97, 4), (98, 2), (99, 1), (100, 9), (101, 9), (102, 5), (103, 4), (104, 7), (105, 2), (106, 1), (107, 3), (109, 1), (110, 3), (111, 2), (112, 5), (113, 3), (114, 5), (115, 2), (116, 5), (117, 3), (118, 1), (119, 5), (120, 1), (121, 4)]

    print_sorted_list(the_list, columns=3, rows=13)