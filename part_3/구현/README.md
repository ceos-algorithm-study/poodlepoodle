## 📋 알고리즘 소개

### 🧐 "머릿속에 떠오른 대로 코드로 표현하는 능력"

**구현 알고리즘** ([백준 카테고리 - Implementation](https://www.acmicpc.net/problemset?sort=ac_desc&algo=102)) 은 문제 풀이에 사용되는
알고리즘의 한 종류지만 특이하게 어떠한 형태가 정해져 있지 않다.

그 이유는 말 그대로 문제에서 제시된 상황을 해결하기 위한 방법,
머릿속 설계도를 그대로 코드로 표현하는 개념에 가깝기 때문이다.  
_(이코테 책에서는 이걸 **피지컬**이라고 표현한다.)_  
백준을 통해 문제 풀이를 하다 보면 다른 알고리즘 분류에도
_Implementation_ 태그가 달려 있는 이유는 이 때문이다.

### 🔖 구현의 두 가지 대표 유형 - **완전 탐색**, **시뮬레이션**

구현 문제의 풀이는 정해져 있지 않으나, 코딩 테스트에서 출제되는
대표적인 유형은 두 가지가 존재한다.

> 완전 탐색 (Bruteforcing)

**완전 탐색**은 **가능한 가짓수를 무식하게 모두 시도해 보는 방법**이다.

보통 알고리즘 문제 풀이에서 이중, 삼중 포문을 사용해 가며
중첩 구조를 만들어 모든 경우를 시도해 보는 것은 금기처럼 느껴지나,
문제에서 함께 제시된 **입력의 크기가 작은 편에 속해
충분히 코드의 실행 시간이 시간 제한을 밑돈다고 판단** 했을 때
시도해 볼 수 있는 하나의 알고리즘이다.

> 시뮬레이션

**시뮬레이션**은 문제에서 제시된 **어떠한 상황이나 실행 규칙에 대해서
코딩을 통해 조건을 설정해 준 후, 작성한 규칙대로 흘러가도록 하는 방법** 으로
주로 시간이나 어느 단계가 지난 후의 결과를 물어보는 유형으로 출제된다.

---

이 두 유형의 또 다른 특징 하나는 **문제에서 제시된 입력 최대값** 혹은
**시간 제한**에 상관없이 작동되는 코드를 제출하도록 출제된다는 것이다.  
_(물론 그렇지 않은 케이스 또한 존재한다.)_

완전 탐색의 경우 기본적으로는 모든 방법의 가짓수를 빠짐없이 전부 탐색하는
형식으로 돌아가나, 간혹 탐색 과정에서 해당 방법이 이미 최선의 방법이
아니라는 걸 알 수 있는 경우가 있다.  
그 때는 해당 가짓수를 끊어내고 다음 가짓수로 넘어가는 방법을 사용할 수 있는데,
이를 **백트래킹(Backtracking)** 기법이라고 한다.

---

> 추가 : 완전 탐색 vs DFS

완전 탐색의 경우는 모든 노드를 탐색한다는 점에서 재귀 함수로 구현할 경우
특히 **DFS**와 헷갈릴 수 있으나,
DFS를 **"완전 탐색을 기본 베이스로 한 그래프 순회 알고리즘"** 으로 이해하면 된다.

또한 현재 시도 중인 방법이 비효율적이라고 판단됐을 경우 완전 탐색은
백트래킹을 통해 끊어내는 반면 DFS는 `visited` 등의 리스트를 이용해
아예 해당 노드를 방문하지 않는 식으로 처리할 수 있다.

---

시뮬레이션의 경우는 굉장히 개인적으로 선호하는 유형인데,
유형 특성 상 시간 초과를 따지는 경우가 거의 없을 뿐더러
문제에서 시뮬레이션 상황을 설명해 주면서
**Pseudo Code**를 제시해 주는데, 이걸 그대로 갖다가
주석으로 달아 놓고 순서대로 코딩해 채우면 되기 때문이다.

![image](https://user-images.githubusercontent.com/6462456/194544405-64622a2b-8c21-4e04-863d-8c8759c737d7.png)
![image](https://user-images.githubusercontent.com/6462456/194544594-81d60fee-acae-4767-b3ee-9c289d5bd10b.png)
_(문제에서 제시된 Pseudo를 그대로 사용한 예시 - [백준 14503번 : 로봇 청소기](https://www.acmicpc.net/problem/14503))_

## 💻 대표적인 문제 풀이

### 📄 백준 15686번 : 치킨 배달 (구현 - 완전 탐색)

![image](https://user-images.githubusercontent.com/6462456/194547693-3697b8fe-3654-4218-8fe2-e7d06a1a5d7e.png)
![image](https://user-images.githubusercontent.com/6462456/194547721-26028cae-8e63-4e96-8289-fe186830e9e7.png)
_백준 15686번 : 치킨 배달_

링크 : [https://www.acmicpc.net/problem/15686](https://www.acmicpc.net/problem/15686)

> 🤨 초기 접근

문제를 간단히 해석하면, 도시에 있는 치킨집을 M개만 빼고 다 없애고 싶은데
가장 **치킨 거리**가 가깝도록 배치하면서 M개만 남기겠다는 게 요점이다.

이런 문제를 풀 때 가장 먼저 나아가야 하는 다음 단계는
**"무식한 방법으로 풀 수 있는 알고리즘의 시간 복잡도"** 를 대충 계산한 후
문제에서 제시된 입력의 최댓값을 넣어 보는 것이다.

1. 도시의 치킨집 중 M개를 고르는 조합의 수를 반복문으로 돌린다.
2. 해당 조합마다 각 집에 이르기까지의 치킨 거리를 구한다.
3. 모든 조합에 대해 최솟값을 비교한 후, 출력한다.

> 🧐 풀이 전략

![image](https://user-images.githubusercontent.com/6462456/194548117-bf60ae95-c4b6-46a2-8bb7-5bd97c8dc4c3.png)

문제에서 제시된 입력 값을 봤을 때 치킨집의 수 `M`은 최대 13개라고 했으므로
치킨집의 조합을 구하는 경우의 수는 `13C?` 정도가 소요된다.  
이는 조합의 특성 상 6이나 7 정도의 중간값에서 가장 많은 경우의 수를 가지며
13C7 기준으로 **1,716**이라는 값이 나온다.

또한 치킨 집의 조합이 정해졌을 때,
특정 집을 기준으로 치킨 거리를 구하는 시간은
치킨 가게의 수인 `O(M)` 만큼인데
이를 모든 집 `2N` 개에 대해서 구해야 하므로
치킨 집의 조합마다 `O(2N * M)`이 소요된다.

결론적으로 N과 M의 최댓값으로 계산한 최대 소요 시간이 크지 않기 때문에
완전탐색으로 풀이 가능하다고 판단하고 진행할 수 있다.

```python
# sys.stdin.readline() 사용
import sys
# 치킨 집을 고르는 경우의 수를 위해 itertools.combinations 사용
from itertools import combinations

# 도시의 가로 및 세로 크기 N 및 치킨집 조합의 수 M 입력
N, M = map(int, sys.stdin.readline().rstrip().split())
# 도시 정보 입력
city = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(N)]
# 도시의 집 정보와 치킨 정보를 따로 리스트에 저장해 놓기
houses = []
total_chicks = []
for i in range(N):
    for j in range(N):
        if city[i][j] == 1:
            houses.append((i, j))
        elif city[i][j] == 2:
            total_chicks.append((i, j))
```

문제에서 주어진 입력을 받아 저장한다.

나중에 각 집집마다 치킨집에 대해서 치킨 거리를 구하기 용이하도록
가정집과 치킨집의 좌표는 따로 리스트에 담아 둔다.

```python
# 도시의 최소 치킨 거리 비교 변수 충분히 큰 수로 초기화
min_len_chick = 30000
# 모든 치킨집을 고르는 경우의 수마다
for chicks in combinations(total_chicks, M):
    # 도시의 치킨 거리 저장 변수 초기화
    len_chick = 0
    # 중간에 이미 최소 치킨 거리보다 커지는 경우 완전탐색을 끊어내기 위함
    backtracking = False

    # 모든 집마다
    for house in houses:
        # 각 집에서 가장 가까운 치킨 거리 비교를 위한 변수 충분히 큰 수로 초기화
        nearest_chick = 30000
        for chick in chicks:
            nearest_chick = min(nearest_chick, abs(chick[0] - house[0]) + abs(chick[1] - house[1]))
        len_chick += nearest_chick

        # 계산 중인 치킨집 조합의 치킨 거리가 최소 치킨 거리보다 이미 커진 경우
        if len_chick >= min_len_chick:
            # 백트래킹 플래그 설정
            backtracking = True
            break

    # 효율적인 완전탐색을 위한 백트래킹
    if backtracking:
        continue

    # 해당 치킨집의 조합이 최소 치킨 거리를 산출하는지 확인 후 최솟값 갱신
    min_len_chick = min(min_len_chick, len_chick)

# 정답 출력
print(min_len_chick)
```

치킨 집의 조합을 구하는 과정에서 `itertools.combinations`를 이용하면
가능한 조합들이 이터레이터로 반환되므로 효율적으로 계산할 수 있다.

따라서 모든 조합마다 모든 집의 최소 치킨 거리를 합산한 후
전체 마을의 치킨 거리의 최솟값을 기록한 후 마지막에 출력해 주면 된다.

어떤 도시의 치킨 거리를 합산해 가던 중에
이미 구해 놓은 최소 치킨 거리보다 현재 계산 중인 거리 값이 길어져서
더 알아보지 않아도 되는 경우도 존재하는데,
이 때는 백트래킹 방식을 이용해 해당 탐색을 끊어내고
다음 탐색으로 넘어가도 된다.

### 📄 백준 3190번 : 뱀 (구현 - 시뮬레이션)

![image](https://user-images.githubusercontent.com/6462456/194552492-f9cb8e45-ab54-4a0c-963d-556c98dbd1b1.png)
_백준 3190번 : 뱀_

링크 : [https://www.acmicpc.net/problem/3190](https://www.acmicpc.net/problem/3190)

> 🤨 초기 접근

문제를 잘 읽어보면 뱀이 사과를 먹으면 길이가 +1 되고
방향 전환을 하면서 돌아다니다가 벽이나 자기 꼬리에 부딪히면 죽는
오락실 게임 같은 느낌의 시뮬레이션임을 알 수 있다.

![image](https://user-images.githubusercontent.com/6462456/194555839-9d9d3b93-3671-4283-b641-0b55d2c033e8.png)

> 🧐 풀이 전략

매 초를 나타내는 변수 `T`를 선언한 후, 아래 동작을 매 초마다 반복하도록 작성한다.

1. 뱀의 머리가 나아갈 좌표 확인  
   1-1. 나아갈 수 없는 경우 -> **종료 후 T 출력**  
   1-2. 나아갈 수 있는 경우 -> **머리 좌표 지도 및 큐에 추가**
2. 만약 이동한 칸에 사과가 없다면 -> **꼬리 좌표 지도 및 큐에서 삭제**
3. 방향 전환 큐의 맨 앞 요소 확인 후 필요 시 방향 전환

```python
# sys.stdin.readline() 사용
import sys
# 뱀의 움직임 및 방향 전환을 위한 deque 사용
from collections import deque

# 보드의 크기 N 입력
N = int(sys.stdin.readline())
# 보드 초기화
board = [[0 for _ in range(N)] for _ in range(N)]
# 뱀 움직임 초기화
snakes = deque([(0, 0)])
board[0][0] = 2
```

문제에서 주어진 입력을 받아 저장한다.

뱀의 움직임은 앞으로 나아갈 때마다 머리를 추가하고 꼬리를 빼 줘야 되기 때문에
지도에 `2`로 표시하는 동시에 움직임을 큐로도 저장해 주어야 한다.

앞에서 빼는 연산이 많으므로 `collections.deque`를 사용했다.

```python
# 사과 갯수 K 및 사과 정보 입력
K = int(sys.stdin.readline())
for _ in range(K):
    r, c = map(int, sys.stdin.readline().rstrip().split())
    board[r - 1][c - 1] = 1

# 방향 전환 횟수 L 및 방향 전환 정보 입력
L = int(sys.stdin.readline())
q = deque()
for _ in range(L):
    sec, rotation = sys.stdin.readline().rstrip().split()
    q.append((int(sec), rotation))

# 방향 설정 (0부터 시계방향으로 동 남 서 북)
direction = 0
moves = ((0, 1), (1, 0), (0, -1), (-1, 0))
```

사과가 있는 칸은 먹은 후에 일반 칸이 되는 것을 유도하기 위해 지도에 `1`로 기록하고,
방향 전환은 뱀의 움직임과 마찬가지로 시간에 따라 앞에서부터 빼서 적용해야 하므로
`deque`를 사용해서 저장했다.

```python
# 시뮬레이션 수행
T = 1
while True:

    # 뱀의 다음 머리가 갈 곳 좌표 계산
    head_r, head_c = snakes[-1]
    dr, dc = moves[direction]
    next_r, next_c = head_r + dr, head_c + dc

    # 다음 머리 위치로 이동할 수 없다면 종료
    if next_r < 0 or next_r >= N or next_c < 0 or next_c >= N or board[next_r][next_c] == 2:
        break

    # 뱀의 꼬리 제외하기 (사과를 먹지 않은 경우는)
    if board[next_r][next_c] == 0:
        prev_r, prev_c = snakes.popleft()
        board[prev_r][prev_c] = 0

    # 뱀의 머리 새로 포함하기)
    snakes.append((next_r, next_c))
    board[next_r][next_c] = 2

    # 방향 전환을 하는 경우
    if q and q[0][0] == T:
        _, rotation = q.popleft()
        if rotation == 'L':
            direction = (direction + 3) % 4
        elif rotation == 'D':
            direction = (direction + 1) % 4

    # 해당 시간이 문제 없이 진행됐을 경우 시간 증가
    T += 1

print(T)
```

나머지는 위의 동작을 그대로 코드로 표현해 준 내용이다.

뱀의 다음 머리가 갈 좌표가 2거나 화면 밖으로 벗어나는 경우라면
게임을 종료하고 지나는 시간 `T`를 출력해 주면 된다.

만약 다음 머리가 갈 좌표가 1이나 0 둘 중 하나인 경우는 머리를 새로 추가하고
0인 경우 (사과를 먹지 않은 경우) 에만 꼬리 정보를 삭제해 주면 된다.

방향 전환 같은 경우는 큐의 맨 앞 요소의 `sec`가 현재 흐른 시간 `T`와
같은 경우, 방향 전환을 하는 타이밍이므로 꺼내서 뱀이 바라보는 방향
`direction`을 변경해 준다.
주의할 점은 방향 전환을 검사하는 과정에서 `IndexError` 가 나지 않도록
큐가 비어 있는 경우도 고려해 줘야 한다는 점이다.

---

### 📄 추가로 풀어볼 만한 문제 추천

> 완전 탐색

1. [백준 1759번 - 암호 만들기](https://www.acmicpc.net/problem/1759)
2. [백준 3980번 - 선발 명단](https://www.acmicpc.net/problem/3980)
3. [백준 14225번 - 부분수열의 합](https://www.acmicpc.net/problem/14225)

> 시뮬레이션

1. [백준 14499번 - 주사위 굴리기](https://www.acmicpc.net/problem/14499)
2. [백준 14503번 - 로봇 청소기](https://www.acmicpc.net/problem/14503)
3. [백준 14890번 - 경사로](https://www.acmicpc.net/problem/14890)
