# 문제풀이 전략
#   1. 피연산자의 갯수 = N, 연산자의 갯수 = N - 1 ->
#       출발점을 첫 피연산자로 하는 완전 탐색 수행
#   2. 1로 이어서 생각하면 각 식을 구성했을 때의 결과는 모든 노드를 순회했을 때의 결과를 가지고 판단
#   3. 완전 탐색 이유 : 중간에 값이 작아졌다가도 최대/최소를 마지막에 갱신할 수 있는 가능성이 있기 때문
#   4. DFS, BFS 어떤 방식으로든 가능하나 이번에는 BFS로 함

# sys.stdin.readline() 사용
import sys
# collections.deque 사용
from collections import deque

# 수열의 길이 N 입력
N = int(sys.stdin.readline())
# 수열 정보 입력
numbers = list(map(int, sys.stdin.readline().rstrip().split()))
# 각 연산자에 대한 사용 가능 횟수 입력
plus, minus, mul, div = map(int, sys.stdin.readline().rstrip().split())

# 큐 초기화
q = deque()
visited = [plus, minus, mul, div]
q.append((0, visited, numbers[0]))

# 최대, 최소 결과값을 저장하기 위한 변수 초기화
max_number = -1000000000
min_number = 1000000000

# 큐가 비어있지 않을 동안 bfs 수행
while q:
    # 현재 깊이, 방문 기록 (연산자 사용 기록), 현재까지의 결과값 기록
    idx, visited, result = q.popleft()
    p, m, mu, di = visited

    # 마지막 피연산자까지 계산을 완료한 경우
    if idx == N - 1:
        # 결과값을 가지고 최대, 최소 비교 후 갱신
        max_number = max(max_number, result)
        min_number = min(min_number, result)
        continue

    # 덧셈
    if p > 0:
        q.append((idx + 1, [p - 1, m, mu, di], result + numbers[idx + 1]))
    # 뺄셈
    if m > 0:
        q.append((idx + 1, [p, m - 1, mu, di], result - numbers[idx + 1]))
    # 곱하기
    if mu > 0:
        q.append((idx + 1, [p, m, mu - 1, di], result * numbers[idx + 1]))
    # 나누기
    if di > 0:
        if result > 0:
            q.append((idx + 1, [p, m, mu, di - 1], result // numbers[idx + 1]))
        # 나누기의 경우는 C++14의 기준을 사용하기 때문에 부호를 바꾸고 몫을 취한 후 다시 원래 부호를 붙여줌
        else:
            q.append((idx + 1, [p, m, mu, di - 1], -(-result // numbers[idx + 1])))

# 최대, 최소 정답 출력
print(max_number)
print(min_number)
