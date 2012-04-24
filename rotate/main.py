#!/usr/bin/env python
# coding: utf-8


def apply_gravity(board):
    ''' apply gravity '''
    new_board = []
    for row in board:
        if 'R' in row or 'B' in row:
            new_row = ""
            for c in row[::-1]:
                if c != '.':
                    new_row = c + new_row
            if len(new_row) < len(row):
                new_row = ('.' * (len(row) - len(new_row))) + new_row
        else:
            new_row = row
        new_board.append(new_row)
    return new_board


def rotate_board(board):
    ''' rotate by 90deg clockwise '''
    new_board = []
    for i in range(len(board)):
        new_board.append("".join(reversed([s[i] for s in board])))
    return new_board


def check_horizontal(board, c, k):
    seq = c * k
    for row in board:
        if seq in row:
            return True
    return False


def check_main_diagonal(board, c, k):
    seq = c * k
    l = len(board)
    for _slice in range(2*l - 1):
        z = 0 if _slice < l else _slice - l + 1
        diag = ""
        for i in range(_slice-z, z-1, -1):
            diag += board[i][_slice - i]
        if seq in diag:
            return True
    return False


def check_board(k, board):
    rotated_board = rotate_board(board)
    red_win = check_horizontal(board, 'R', k) or check_main_diagonal(board, 'R', k)
    if not red_win:
        red_win = check_horizontal(rotated_board, 'R', k) or check_main_diagonal(rotated_board, 'R', k)

    blue_win = check_horizontal(board, 'B', k) or check_main_diagonal(board, 'B', k)
    if not blue_win:
        blue_win = check_horizontal(rotated_board, 'B', k) or check_main_diagonal(rotated_board, 'B', k)

    if red_win and blue_win:
        return 'Both'
    elif red_win:
        return 'Red'
    elif blue_win:
        return 'Blue'
    else:
        return 'Neither'


def main():
    T = int(raw_input())
    for i in range(T):
        N, K = map(int, raw_input().split())
        board = []
        for _ in range(N):
            board.append(raw_input())
        board = apply_gravity(board)
        print "Case #%s: %s" % (i+1, check_board(K, board))


if __name__ == "__main__":
    main()
