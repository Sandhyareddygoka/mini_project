def undscr(str):
    op = ""
    for i in range(len(str)):
        if str[i] == "_":
            continue
        op += str[i]
    print(op)

undscr("FUll_ST_AC_K")

