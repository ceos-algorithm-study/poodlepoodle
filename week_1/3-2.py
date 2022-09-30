import sys

N, M, K = map(int, sys.stdin.readline().rstrip().split())
numbers = list(map(int, sys.stdin.readline().rstrip().split()))

first = max(numbers)
numbers.remove(first)
second = max(numbers)

idx = range(K, M, K + 1)
result = [second if i in idx else first for i in range(M)]

print(sum(result))