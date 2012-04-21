#!/usr/bin/env python
# coding: utf-8

def main():
    n = int(raw_input())
    for i in range(n):
        words = raw_input().split()
        print "Case #%s: %s" % (i+1, " ".join(words[::-1]))

if __name__ == "__main__":
    main()
