## 피보나치 수

---

피보나치 수는 F(0) = 0, F(1) = 1일 때, 1 이상의 n에 대하여 F(n) = F(n-1) + F(n-2) 가 적용되는 수 입니다.

예를들어

- F(2) = F(0) + F(1) = 0 + 1 = 1
- F(3) = F(1) + F(2) = 1 + 1 = 2
- F(4) = F(2) + F(3) = 1 + 2 = 3
- F(5) = F(3) + F(4) = 2 + 3 = 5

와 같이 이어집니다.

2 이상의 n이 입력되었을 때, 
n번째 피보나치 수를 1234567으로 나눈 나머지를 리턴하는 함수, solution을 완성해 주세요.

---
### Problem Solved Check
- [x] 1회 24/06/24
- [x] 2회 24/08/08
- [ ] 3회
~~~
def solution(n):
    f_num = [0]*(n+1)
    f_num[1] = 1
    for i in range(2, n+1):
        f_num[i] = (f_num[i-1]+f_num[i-2])%1234567
    answer = f_num[-1]
    return answer
    
~~~
~~~
def solution(n):
    fib = [0]*(n+1)
    fib[1] = 1
    for i in range(2, n+1):
        fib[i] = fib[i-1]+fib[i-2]
    return fib[n] % 1234567

~~~