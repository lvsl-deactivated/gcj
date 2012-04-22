#!/usr/bin/env python
# coding: utf-8

def count_mkdirs(old, new):
    G = {}

    for path in old:
        g = G
        for d in path[1:].split('/'):
            if d not in g:
                g[d] = {}
            g = g[d]

    count = 0
    for path in new:
        g = G
        for d in path[1:].split('/'):
            if d not in g:
                g[d] = {}
                count += 1
            g = g[d]

    return count

def main():
    T = int(raw_input())
    for i in range(T):
        N, M = map(int, raw_input().split())
        old_dirs = []
        for _ in xrange(N):
            old_dirs.append(raw_input())
        new_dirs = []
        for _ in xrange(M):
            new_dirs.append(raw_input())
        print "Case #%s: %s" % (i+1, count_mkdirs(old_dirs, new_dirs))


if __name__ == "__main__":
    main()
