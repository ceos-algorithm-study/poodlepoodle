import sys

def input(): return sys.stdin.readline().rstrip()

N = int(input())
numbers = [int(input()) for _ in range(N)]

numbers.sort(key=lambda x:-x)
print(*numbers)