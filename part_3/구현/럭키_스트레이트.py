import sys

N = list(map(int, list(sys.stdin.readline().rstrip())))
print("LUCKY" if sum(N[0:len(N) // 2]) == sum(N[len(N) // 2:]) else "READY")