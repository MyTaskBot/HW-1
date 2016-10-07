def table_print(table, cols):
    BORDER = (9484, 9516, 9488, 9500, 9532, 9508, 9492, 9524, 9496, 9472, 9474)
    FIRST_ROWS = 0
    ROWS = 1
    END_ROWS = 2

    # Печать строки таблицы
    def print_rows(cols, style_rows=ROWS):
        cnt = 0
        print('%c' % (BORDER[style_rows * 3]), end='')
        for k in cols:
            cnt += 1
            print('%s' % (chr(BORDER[9]) * k[1]), end='')
            if (cnt == len(cols)):
                print('%c\n' % (BORDER[style_rows * 3 + 2]), end='')
            else:
                print('%c' % (BORDER[style_rows * 3 + 1]), end='')

    print_rows(cols, FIRST_ROWS)
    # Печатать заголовок
    cnt_elem = 0
    print('%c' % (BORDER[10]), end='')
    for val in cols:
        cnt_elem += 1
        str = "{0:^%d}" % (val[1])
        print(str.format(val[2][:val[1]]), end='')
        if (cnt_elem == len(cols)):
            # last
            print('%c\n' % (BORDER[10]), end='')
        else:
            # not a last
            print('%c' % (BORDER[10]), end='')
    print_rows(cols)
    # Печатать строки
    cnt_rows = 0
    for elem in table:
        cnt_elem = 0
        print('%c' % (BORDER[10]), end='')
        for val in cols:
            cnt_elem += 1
            fstr = "{0:^%d}" % (val[1])
            print(fstr.format(elem[val[0]]), end='')
            if (cnt_elem == len(cols)):
                # last
                print('%c\n' % (BORDER[10]), end='')
            else:
                # not a last
                print('%c' % (BORDER[10]), end='')
        cnt_rows += 1
        if (cnt_rows == len(table)):
            print_rows(cols, END_ROWS)
        else:
            print_rows(cols)
