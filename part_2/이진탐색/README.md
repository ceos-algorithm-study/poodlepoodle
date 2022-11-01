# 이분 탐색 알고리즘 - 이코테 요약

## 핵심

**정렬된 배열 내에서 O(logN) 안에 특정 요소를 찾아내는 알고리즘**

## 순차 탐색

배열의 첫 번째 요소부터 마지막 요소까지 순차적으로 특정 요소를 검색

- 배열이 정렬되어 있을 필요 없음
- 최선의 경우 1번만에, 최악의 경우 배열의 길이 N번만에 탐색 -> **O(N)**

## 이분 탐색

`start`, `end`, `middle` 3가지 변수를 통해
한 번의 탐색마다 탐색 범위를 절반으로 줄이는 탐색

- 배열이 정렬되어 있어야 함
- 최선의 경우 1번만에 (정확히 배열의 중간), 최악의 경우 log N번만에 탐색  
  -> **O(logN)**

## 이분 탐색의 구현

> 재귀 함수를 이용

```python
array = [1, 2, 3, 5, 7, 8, 15]

def bin_search(start, end, target):
    if start > end:
        return -1

    middle = (start + end) // 2

    if target == array[middle]:
        return middle
    elif target < array[middle]:
        return bin_search(start, middle - 1, target)
    else:
        return bin_search(middle + 1, end, target)
```

> 반복문을 이용 (문제 풀이에 권장)

```python
array = [1, 2, 3, 5, 7, 8, 15]

start = 0
end = len(array) - 1
found = False
answer = -1

while start <= end:
    middle = (start + end) // 2

    if target == array[middle]:
        answer = middle
        found = True
        break
    elif target < array[middle]:
        end = middle - 1
    else:
        start = middle + 1
```

## 이진 탐색 트리

- 모든 부모 노드는 최대 2개의 자식 노드를 가질 수 있음
- 왼쪽 자식 노드는 부모보다 무조건 작은 값을 가짐
- 오른쪽 자식 노드는 부모보다 무조건 큰 값을 가짐
- 나머지는 생략

## Parametric Search?

주어진 범위 내에서 원하는 값 또는 원하는 조건에
가장 일치하는 값을 찾아내는 알고리즘

- **최적화 문제**를 **결정 문제**로 바꾸어 풀이가 가능해짐
- `left`, `right`, `middle`을 이용한다는 점에서 이분 탐색과 매우 유사
