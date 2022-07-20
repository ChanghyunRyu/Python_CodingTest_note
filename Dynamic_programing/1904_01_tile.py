# 파이썬 메모리 초과에 대하여
# 파이썬의 int 형은 고정된 크기가 아니다. 그 변수가 실제로 담고 있는 크기에 따라 유동적으로 크기가 변동된다.
# 결국 int 값이 너무 커지게되는 경우, 메모리초과가 일어나게 된다.
# 결국 해당 문제의 15746로 나눈 나머지를 출력하라는 것에 해답이 존재한다.
# 마지막에 15746으로 나누는 것이 아닌 계산 당시 15746으로 나눈 나머지를 저장하여 저장하는 int 값의 크기를 일정하게 유지하여야 한다.
n = int(input())
tiles = [0]*n
tiles[0] = 1
if n > 1:
    tiles[1] = 2
for i in range(2, n):
    tiles[i] = (tiles[i-1] + tiles[i-2]) % 15746
print(tiles[n-1])
