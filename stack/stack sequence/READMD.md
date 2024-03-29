
## 스택 수열

------

스택 (stack)은 기본적인 자료구조 중 하나로, 컴퓨터 프로그램을 작성할 때 자주 이용되는 개념이다. 스택은 자료를 넣는 (push) 입구와 자료를 뽑는 (pop) 입구가 같아 제일 나중에 들어간 자료가 제일 먼저 나오는 (LIFO, Last in First out) 특성을 가지고 있다.

1부터 n까지의 수를 스택에 넣었다가 뽑아 늘어놓음으로써, 하나의 수열을 만들 수 있다. 이때, 스택에 push하는 순서는 반드시 오름차순을 지키도록 한다고 하자. 임의의 수열이 주어졌을 때 스택을 이용해 그 수열을 만들 수 있는지 없는지, 있다면 어떤 순서로 push와 pop 연산을 수행해야 하는지를 알아낼 수 있다. 이를 계산하는 프로그램을 작성하라.

### 입력

- 첫 줄에 n (1 ≤ n ≤ 100,000)이 주어진다. 
- 둘째 줄부터 n개의 줄에는 수열을 이루는 1이상 n이하의 정수가 하나씩 순서대로 주어진다. 물론 같은 정수가 두 번 나오는 일은 없다.

### 출력

- 입력된 수열을 만들기 위해 필요한 연산을 한 줄에 한 개씩 출력한다. 
- push연산은 +로, pop 연산은 -로 표현하도록 한다. 불가능한 경우 NO를 출력한다.

------

### 풀이

해당 문제는 복잡하게 생각하기보다 직접 스택을 만든 후, 이를 통해 해당 수열을 만들면 된다.  

제시된 수열에서 첫 숫자가 4라고 가정해 보자. 숫자 4를 내보내기 위해 4번의 push 후(각각 스택에 1,2,3,4가 push된다), pop을 하면 된다.  
그 다음 숫자가 6이라면 2번의 push 후(각각 5, 6이 push 된다), pop을 하면 된다.  
여기서 우리가 알 수 있는 것은 수열에서 전에 나온 가장 큰 숫자(4)보다 이후 숫자(6)가 큰 경우, 기존 스택에 들어간 가장 큰 수부터 새로 나온 숫자만큼 push한 후 pop하면 된다는 것이다. 만약 기존 스택에 들어간 가장 큰 수보다 새로 나온 숫자가 작다면 이미 스택에 들어가 있으므로 pop을 하면 된다.  
그럼 여기서 생각해볼 수 있는 것은 언제 수열을 만들 수 없는가이다.  
아까처럼 첫 숫자가 4라고 하자. 그 다음 나온 숫자가 2라고 한다면 이 수열은 만들 수 없을 것이다. 첫 숫자 4를 만들기 위해 우리는 4번의 push 이후 1번의 pop을 실행했다. 이 연산을 통해 stack 가장 위에는 3이 위치해 있다. 그러나 이후 숫자는 2가 나왔고 3을 빼내기 전에는 2를 꺼낼 수 없으므로 수열을 만드는 것이 불가능한 것이다.  
즉 수열의 가장 위에 있는 숫자가 다음 수열에 나오는 숫자보다 클 경우 수열을 만들 수 없다. 수열을 만들면서 해당 조건을 참조하여 수열의 가능여부를 따지면 된다.

~~~
import sys
n = int(input())

seq = []
for _ in range(n):
    seq.append(int(sys.stdin.readline()))
result = []

start = 0
stack = [0]
for num in seq:
    if num - start > 0:
        for i in range(start, num):
            stack.append(i+1)
            result.append('+')
    elif stack[len(stack)-1] > num:
        result = ['NO']
        break
    result.append('-')
    start = max(stack.pop(), start)

for r in result:
    print(r)
~~~
