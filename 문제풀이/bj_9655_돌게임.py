n = int(input())

# 첫 시작을 상근이가 한다면
# n개의 돌에서 남은 가짓수가 4개 또는 2개이면 싱근의 승
# 1, 3개라면 창영이의 승리

# 띠리사 2의 배수에 따라 승리가 달라진다.

if(n%2 == 1):
    print("SK")
else:
    print("CY")