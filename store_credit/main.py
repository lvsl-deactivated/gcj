#!/usr/bin/env python
# coding: utf-8


def find_optimal_prices(credit, prices):
    prices = list(enumerate(prices))
    prices.sort(key=lambda item: item[1], reverse=True)


    i = 0
    j = len(prices)-1

    while True:
        max_item = prices[i]
        min_item = prices[j]

        if max_item[1] + min_item[1] > credit:
            i = i + 1
            j = len(prices)-1
            continue
        elif max_item[1] + min_item[1] == credit:
            return sorted([min_item[0]+1, max_item[0]+1])
        else:
            j = j - 1


def main():
    n = int(raw_input())
    for i in range(n):
        credit = int(raw_input())
        raw_input() # dont' need list size
        prices = [int(item) for item in raw_input().split()]
        a, b = find_optimal_prices(credit, prices)
        print "Case #%s: %s %s" % (i+1, a, b)

if __name__ == "__main__":
    main()
