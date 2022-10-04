import sys

N, K = map(int, sys.stdin.readline().rstrip().split())

cnt = 0
while N > 1:
    print(N)
    if N % K == 0:
        N //= K
    else:
        N -= 1
    cnt += 1
    
print(cnt)