## 1644번 소수의 연속합

---

하나 이상의 연속된 소수의 합으로 나타낼 수 있는 자연수들이 있다. 몇 가지 자연수의 예를 들어 보면 다음과 같다.

- 3 : 3 (한 가지)
- 41 : 2+3+5+7+11+13 = 11+13+17 = 41 (세 가지)
- 53 : 5+7+11+13+17 = 53 (두 가지)

하지만 연속된 소수의 합으로 나타낼 수 없는 자연수들도 있는데, 20이 그 예이다. 
7+13을 계산하면 20이 되기는 하나 7과 13이 연속이 아니기에 적합한 표현이 아니다. 또한 한 소수는 반드시 한 번만 덧셈에 사용될 수 있기 때문에, 3+5+5+7과 같은 표현도 적합하지 않다.

자연수가 주어졌을 때, 이 자연수를 연속된 소수의 합으로 나타낼 수 있는 경우의 수를 구하는 프로그램을 작성하시오.

### 입력 

- 첫째 줄에 자연수 N이 주어진다. (1 ≤ N ≤ 4,000,000)

### 출력

- 첫째 줄에 자연수 N을 연속된 소수의 합으로 나타낼 수 있는 경우의 수를 출력한다.

---
### Problem Solved Check
- [x] 1회 24/07/05
- [ ] 2회
- [ ] 3회

특정 범위의 소수를 빠르게 구하는 방법은 에라토스테네스의 체를 사용하는 것이다.
~~~
n = int(input())


def find_prefix_sum(number):
    prefix_sum = [0]
    prime_list = return_prime_list(number)
    for prime_number in prime_list:
        prefix_sum.append(prefix_sum[-1]+prime_number)
    return prefix_sum


def return_prime_list(number):
    sieve = [True]*(number+1)
    m = int((number+1)**0.5)
    for i in range(2, m+1):
        if sieve[i] is True:
            for j in range(i+i, number+1, i):
                sieve[j] = False
    return [i for i in range(2, number+1) if sieve[i] is True]


def find_continuous_sum(target, prefix):
    answer = 0
    start, end = 0, 1
    while end < len(prefix):
        if prefix[end]-prefix[start] == target:
            answer += 1
            start += 1
        elif prefix[end]-prefix[start] > target:
            start += 1
        else:
            end += 1
    return answer


prime_prefix = find_prefix_sum(n)
result = find_continuous_sum(n, prime_prefix)
print(result)

~~~
