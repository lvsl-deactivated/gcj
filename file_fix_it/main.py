#!/usr/bin/env python
# coding: utf-8


def _build_tree(paths, G=None):
    if G is None:
        G = {}
    count = 0
    for path in paths:
        g = G
        for d in path[1:].split('/'):
            if d not in g:
                g[d] = {}
                count += 1
            g = g[d]

    return G, count


def count_mkdirs(old, new):
    return _build_tree(new, G=_build_tree(old)[0])[1]


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
