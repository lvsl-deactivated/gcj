#!/usr/bin/env python
# coding: utf-8

def next_n(current):
    if current.isdigit():
        current = int(current)
        if current == 0:
            current = 2
        elif current == 9:
            return "a"
        else:
            current += 1
        return str(current)
    else:
        current = ord(current)
        current += 1
        return chr(current)

def convert_number(n):
    d = {n[0]: '1'}
    s = "1"
    cur_num = '0'
    for c in n[1:]:
        if c not in d:
            d[c] = cur_num
            cur_num = next_n(cur_num)
        s += d[c]

    base = len(d)
    if base == 1:
        base = 2
    return int(s, base)


def main():
    n = int(raw_input())
    for i in range(n):
        number = raw_input()
        print "Case #%s: %s" % (i+1, convert_number(number))


if __name__ == "__main__":
    main()
