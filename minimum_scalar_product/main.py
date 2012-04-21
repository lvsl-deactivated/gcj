#!/usr/bin/env python
# coding: utf-8


def find_min_product(v, w):
    v = sorted(v)
    w = sorted(w, reverse=True)

    return sum(x*y for x, y in zip(v, w))


def main():
    n = int(raw_input())
    for i in range(n):
        raw_input() # ignore length
        v1 = [int(x) for x in raw_input().split()]
        v2 = [int(x) for x in raw_input().split()]
        print "Case #%s: %s" % (i+1, find_min_product(v1, v2))


if __name__ == "__main__":
    main()
