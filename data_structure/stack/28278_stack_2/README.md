## 28278번 스택 2

---

시간 제한: 2초, 메모리 제한: 1024MB

정수를 저장하는 스택을 구현한 다음, 입력으로 주어지는 명령을 처리하는 프로그램을 작성하시오.

명령은 총 다섯 가지이다.

1. 1 X: 정수 X를 스택에 넣는다. (1 ≤ X ≤ 100,000)  
2. 2: 스택에 정수가 있다면 맨 위의 정수를 빼고 출력한다. 없다면 -1을 대신 출력한다.  
3. 3: 스택에 들어있는 정수의 개수를 출력한다.  
4. 4: 스택이 비어있으면 1, 아니면 0을 출력한다.  
5. 5: 스택에 정수가 있다면 맨 위의 정수를 출력한다. 없다면 -1을 대신 출력한다.  

### 입력

- 첫째 줄에 명령의 수 N이 주어진다. (1 ≤ N ≤ 1,000,000)
- 둘째 줄부터 N개 줄에 명령이 하나씩 주어진다. 
- 출력을 요구하는 명령은 하나 이상 주어진다.

### 출력

- 출력을 요구하는 명령이 주어질 때마다 명령의 결과를 한 줄에 하나씩 출력한다.

---
### Problem Solved Check

- [x] 1회 24/05/10
- [ ] 2회
- [ ] 3회
~~~
import sys
from collections import deque

n = int(input())
s = deque()
for _ in range(n):
    command = list(map(int, sys.stdin.readline().split()))
    if command[0] == 1:
        s.append(command[1])
    elif command[0] == 2:
        if s:
            print(s.pop())
        else:
            print(-1)
    elif command[0] == 3:
        print(len(s))
    elif command[0] == 4:
        if s:
            print(0)
        else:
            print(1)
    elif command[0] == 5:
        if s:
            num = s.pop()
            print(num)
            s.append(num)
        else:
            print(-1)
~~~