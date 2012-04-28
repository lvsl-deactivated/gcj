#!/usr/bin/env python
# coding: utf-8


def check_points(p, total):
    # search for not soltion
    for k in range(p, 11):
        if total > (k + 20):
            continue
        seq = [k, k-1, k+1]
        for i in seq:
            for j in seq:
                if total == (k + i + j):
                    #print "choice for %s with %s is %s" % (total, p, [k,i,j])
                    return True, False

    # search for surprising soltion
    for k in range(p, 11):
        if total > (k + 20):
            continue
        if k == 1:
            seq = [k, k-1, k+1]
        else:
            seq = [k, k-1, k+1, k-2, k+2]
        for i in seq:
            for j in seq:
                if total == (k + i + j):
                    #print "surprise! choice for %s with %s is %s" % (total, p, [k,i,j])
                    return True, True

    return False, None


def find_winners(n, s, p, points):
    if p == 0:
        return n

    surp_count = 0
    win_count = 0

    for total in points:
        is_winner, is_surp = check_points(p, total)
        if is_winner and not is_surp:
            win_count += 1
        elif is_winner:
            surp_count += 1

    if surp_count > s:
        surp_count = s

    return win_count + surp_count


def main():
    T = int(raw_input())
    for i in range(T):
        numbers = [int(x) for x in raw_input().split()]
        n = numbers.pop(0)
        s = numbers.pop(0)
        p = numbers.pop(0)
        points = numbers
        print "Case #%s: %s" % (i+1, find_winners(n, s, p, points))


if __name__ == "__main__":
    main()
