import sys

def input(): return sys.stdin.readline().rstrip()

N = int(input())
students = []
for _ in range(N):
    name, score = input().split()
    students.append((name, int(score)))

students.sort(key=lambda x:x[1])
print(*[name for name, _ in students])
