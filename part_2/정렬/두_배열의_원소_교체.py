import sys

def input(): return sys.stdin.readline().rstrip()

N, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()
B.sort(key=lambda x:-x)

for i in range(K):
    if A[i] < B[i]:
        A[i], B[i] = B[i], A[i]
    else: break

print(sum(A))
