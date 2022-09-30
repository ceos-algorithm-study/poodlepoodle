import sys

convert = {
    'a' : 0,
    'b' : 1,
    'c' : 2,
    'd' : 3,
    'e' : 4,
    'f' : 5,
    'g' : 6,
    'h' : 7,
}

c, r = list(sys.stdin.readline().rstrip())
c = convert[c]
r = int(r) - 1

drc = [[1, -2], [-1, -2], [-2, -1], [-2, 1], [-1, 2], [1, 2], [2, -1], [2, 1]]

moves = [(r + d[0], c + d[1]) for d in drc]
available_moves = [(r, c) for r, c in moves if r >= 0 and r < 8 and c >= 0 and c < 8]
print(len(available_moves))