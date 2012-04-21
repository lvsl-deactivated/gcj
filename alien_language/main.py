#!/usr/bin/env python
# coding: utf-8


def build_trie(words):
    ''' Build trie from a list of words '''
    G = {}
    for word in words:
        g = G
        for c in word:
            if c not in g:
                g[c] = {}
            g = g[c]
    return G


def parse_pattern(s):
    ''' Parse string pattern '''
    p = []
    in_braces = s[0] == '('
    i = 0
    for c in s:
        if c == '(':
            in_braces = True
        elif c == ')':
            in_braces = False
            i += 1
        elif in_braces:
            if i == len(p):
                p.append(c)
            else:
                p[i] += c
        else:
            p.append(c)
            i += 1
    return p


def count_words(trie, pattern):
    ''' Count words using Deep First Search '''
    def _dfs_rec_count(t, p):
        count = 0
        c = p.pop(0)
        for k, v in t.items():
            if k not in c:
                continue
            if not v: # this is leaf
                count += 1
            else:
                count += _dfs_rec_count(v, p[:])
        return count

    return _dfs_rec_count(trie, pattern[:])


def main():
    _, D, N = [int(x) for x in raw_input().split()]
    trie = build_trie([raw_input() for i in range(D)])
    for i in range(N):
        pattern = parse_pattern(raw_input())
        print "Case #%s: %s" % (i+1, count_words(trie, pattern))


if __name__ == "__main__":
    main()
