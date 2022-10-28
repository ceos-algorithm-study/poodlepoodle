import sys

def input(): return sys.stdin.readline().rstrip()

N = int(input())
datas = list(map(int, input().split()))

M = int(input())
requests = list(map(int, input().split()))

# N은 최대 10^6, M은 최대 10^5
# 각 부품에 대해서 순차 탐색을 수행하면 O(10^11)이 소요되므로 시간 초과
# 적어도 모든 부품에 대해서는 체크를 해야 하므로 해당 부품의 존재 여부를 찾는 과정을 O(N)에서 O(logN)으로 줄일 필요가 있다.

datas.sort()

answers = []

for number in requests:
    start = 0
    end = N - 1

    found = False
    
    while start <= end:
        middle = (start + end) // 2

        if datas[middle] == number:
            found = True
            break
        elif datas[middle] < number:
            start = middle + 1
        else:
            end = middle - 1

    if found:
        answers.append('yes')
    else:
        answers.append('no')

print(*answers)
