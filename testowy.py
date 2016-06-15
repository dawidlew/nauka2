





def show_item(word_or_char, count, is_word):
    if word:
        formant = '{:<15}: {:}'
    else:
        formant = '{}: {:<15}'
    print formant.format(chr(word_or_char), count)








    def print_sorted_list(data, rows=0, columns=0, print_solution=False):
        if rows:
            lines = {}
            for count, item in enumerate(data):
                lines.setdefault(count % rows, []).append(item)
            for key, value in lines.items():
                for item in value:
                    if print_solution:
                        print '{:<15}: {:}'.format((item[0]), item[1]),
                    else:
                        print '{}: {:<15}'.format(chr(item[0]), item[1]),
                print

    elif columns:
    for count, item in enumerate(data, 1):
        print item,
        if count % columns == 0:
            print

else:
print data
