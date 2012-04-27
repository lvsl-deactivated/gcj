#!/usr/bin/env python
# coding: utf-8

def guess():
    ''' Guess alphabet from given example '''
    d = {
        'y': 'a',
        'e': 'o',
        'q': 'z',
        'z': 'q',
    }
    googlerese = "ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv"
    english = "our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up"

    for ggl, eng in zip(googlerese.split(), english.split()):
        for g, e in zip(ggl, eng):
            d[g] = e
    return d


def translate(d, words):
    twords = []
    for w in words:
        tword = []
        for c in w:
            tword.append(d[c])
        twords.append("".join(tword))
    return " ".join(twords)


def main():
    t = int(raw_input())
    d = guess()
    for i in range(t):
        words = raw_input().split()
        print "Case #%s: %s" % (i+1, translate(d, words))

if __name__ == "__main__":
    main()
