#!/usr/bin/env python
# coding: utf-8


def count_intersections(wires):
    swires = sorted(wires, key=lambda w: max(w[0], w[1]), reverse=True)
    count = 0
    while swires:
        max_x, max_y = swires.pop(0)
        for x, y in swires:
            if max_x > max_y:
                if y > max_y:
                    count += 1
            else:
                if x > max_x:
                    count += 1
    return count

def main():
    T = int(raw_input())
    for i in range(T):
        N = int(raw_input())
        wires = []
        for j in range(N):
            w = tuple(map(int, raw_input().split()))
            wires.append(w)
        print "Case #%s: %s" % (i+1, count_intersections(wires))


if __name__ == "__main__":
    main()
