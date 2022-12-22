import sys
from collections import deque

sys.stdin = open("C:/Users/R/Desktop/python_input/bj_12852.txt")

n = int(sys.stdin.readline().rstrip())
q = deque() # 우선순위큐
q.append([n]) #큐 안에 n만 담긴 배열을 추가
ans = []

while q:
    # 가장 우선순위가 앞선 q를 pop
    i = q.popleft()
    # 뽑아낸 q의 배열에서 1번째 값을 x로 선언
    x = i[0]
    # 만약 x가 1이라면, 즉 큐에서 뽑아낸 값의 배열에서 
    # 첫 번째 값이 1이라면 ans에 i를 담고 반복문 멈춤
    if x == 1:
        ans = i
        break

    if x % 3 == 0:
        q.append([x//3] + i)

    if x % 2 == 0:
        q.append([x//2] + i)

    q.append([x-1] + i)

print(len(ans)- 1)
print(*ans[::-1])


# deque([[12]])
# ----
# deque([[4, 12], [6, 12], [11, 12]])
# ----
# deque([[6, 12], [11, 12], [2, 4, 12], [3, 4, 12]])
# ----
# deque([[11, 12], [2, 4, 12], [3, 4, 12], [2, 6, 12], [3, 6, 12], [5, 6, 12]])  
# ----
# deque([[2, 4, 12], [3, 4, 12], [2, 6, 12], [3, 6, 12], [5, 6, 12], [10, 11, 12]])
# ----
# deque([[3, 4, 12], [2, 6, 12], [3, 6, 12], [5, 6, 12], [10, 11, 12], [1, 2, 4, 12], [1, 2, 4, 12]])
# ----
# deque([[2, 6, 12], [3, 6, 12], [5, 6, 12], [10, 11, 12], [1, 2, 4, 12], [1, 2, 4, 12], [1, 3, 4, 12], [2, 3, 4, 12]])
# ----
# deque([[3, 6, 12], [5, 6, 12], [10, 11, 12], [1, 2, 4, 12], [1, 2, 4, 12], [1, 3, 4, 12], [2, 3, 4, 12], [1, 2, 6, 12], [1,], [1, 2, 6, 12]])
# ----
# deque([[5, 6, 12], [10, 11, 12], [1, 2, 4, 12], [1, 2, 4, 12], [1, 3, 4, 12], [2, 3, 4, 12], [1, 2, 6, 12], [1, 2, 6, 12],  12], [1, 3, 6, 12], [2, 3, 6, 12]])
# ----
# deque([[10, 11, 12], [1, 2, 4, 12], [1, 2, 4, 12], [1, 3, 4, 12], [2, 3, 4, 12], [1, 2, 6, 12], [1, 2, 6, 12], [1, 3, 6, 12 6, 12], [2, 3, 6, 12], [4, 5, 6, 12]])
# ----
# deque([[1, 2, 4, 12], [1, 2, 4, 12], [1, 3, 4, 12], [2, 3, 4, 12], [1, 2, 6, 12], [1, 2, 6, 12], [1, 3, 6, 12], [2, 3, 6, 1, 6, 12], [4, 5, 6, 12], [5, 10, 11, 12], [9, 10, 11, 12]])