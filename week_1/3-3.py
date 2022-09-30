import sys

M, N = map(int, sys.stdin.readline().rstrip().split())
numbers = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(M)]

mins = [min(line) for line in numbers]
print(max(mins))