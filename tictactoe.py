"""
1, 2, 3
4, 5, 6
7, 8, 9
"""
WIN_MASK = [
    0b000000111, # row 1,2,3
    0b000111000, # row 4,5,6
    0b111000000, # row 7,8,9
    0b100100100, # col 3,6,9
    0b010010010, # col 2,5,8
    0b001001001, # col 1,4,7
    0b100010001, # dlg 1,5,9
    0b001010100, # dlg 3,5,7
]

x = 0
o = 0

win = False
who = 'x'
while True:
    print(str(bin(x)))
    print(str(bin(o)))
    ch = int(input(f"pos {who}: "))
    if ch < 1 or ch > 9:
        print("invalid")
        continue

    ch = 1 << ch - 1
    if (x & ch) == ch or (o & ch) == ch:
        print('invalid')
        continue

    if who == 'x':
        x |= ch
    else:
        o |= ch

    for mask in WIN_MASK:
        if (x & mask) == mask:
            print("x wins")
            win = True
            break
        elif (o & mask) == mask:
            print("o wins")
            win = True
            break
    if win:
        break

    who = 'o' if who == 'x' else 'x'
