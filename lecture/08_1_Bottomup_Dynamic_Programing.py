d = [0] * 100 # dp테이블 생성

d[1] = 1
d[2] = 1
n = 6

for i in range(3, n+1):
    d[i] = d[i-1] + d[i-2]

print(d[6])