## N으로 표현

---

[출처] https://school.programmers.co.kr/learn/courses/30/lessons/42895

아래와 같이 5와 사칙연산만으로 12를 표현할 수 있습니다.

12 = 5 + 5 + (5 / 5) + (5 / 5)
12 = 55 / 5 + 5 / 5
12 = (55 + 5) / 5

5를 사용한 횟수는 각각 6,5,4 입니다. 그리고 이중 가장 작은 경우는 4입니다.  
이처럼 숫자 N과 number가 주어질 때, N과 사칙연산만 사용해서 표현 할 수 있는 방법 중 
N 사용횟수의 최솟값을 return 하도록 solution 함수를 작성하세요.

### 제한사항

- N은 1 이상 9 이하입니다.
- number는 1 이상 32,000 이하입니다.
- 수식에는 괄호와 사칙연산만 가능하며 나누기 연산에서 나머지는 무시합니다.
- 최솟값이 8보다 크면 -1을 return 합니다.

---
### Problem Solved Check
- [X] 1회 24/06/25
- [X] 2회 24/08/09
- [ ] 3회
~~~
def solution(n, number):
    dp = [set() for _ in range(9)]
    for i in range(1, 9):
        now = dp[i]
        now.add(int(str(n) * i))
        for j in range(1, i):
            for k in dp[j]:
                for l in dp[i-j]:
                    now.add(k+l)
                    if k-l > 0:
                        now.add(k-l)
                    now.add(k*l)
                    if k != 0 and l != 0:
                        now.add(k//l)
        if number in now:
            return i
    return -1
    
~~~
~~~
def solution(n, target):
    dp = [set()]*9
    answer = -1
    for i in range(1, 9):
        dp[i] = fill_number(n, i, dp)
        if target in dp[i]:
            answer = i
            break
    return answer


def fill_number(number, index, dynamic):
    temp = set()
    temp.add(int(''.join([str(number)]*index)))
    if index == 1:
        return temp
    for i in range(1, index):
        num_group1 = dynamic[i]
        num_group2 = dynamic[index-i]
        for num1 in num_group1:
            for num2 in num_group2:
                temp.add(num1+num2)
                temp.add(num1-num2)
                if num2 != 0:
                    temp.add(num1//num2)
                temp.add(num1*num2)
    return temp
~~~
