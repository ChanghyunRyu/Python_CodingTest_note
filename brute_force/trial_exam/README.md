## 모의고사

---

[출처] https://school.programmers.co.kr/learn/courses/30/lessons/42840

수포자는 수학을 포기한 사람의 준말입니다. 수포자 삼인방은 모의고사에 수학 문제를 전부 찍으려 합니다. 
수포자는 1번 문제부터 마지막 문제까지 다음과 같이 찍습니다.

1번 수포자가 찍는 방식: 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, ...  
2번 수포자가 찍는 방식: 2, 1, 2, 3, 2, 4, 2, 5, 2, 1, 2, 3, 2, 4, 2, 5, ...  
3번 수포자가 찍는 방식: 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, ...  

1번 문제부터 마지막 문제까지의 정답이 순서대로 들은 배열 answers가 주어졌을 때, 
가장 많은 문제를 맞힌 사람이 누구인지 배열에 담아 return 하도록 solution 함수를 작성해주세요.

### 제한사항

- 시험은 최대 10,000 문제로 구성되어있습니다.
- 문제의 정답은 1, 2, 3, 4, 5중 하나입니다.
- 가장 높은 점수를 받은 사람이 여럿일 경우, return하는 값을 오름차순 정렬해주세요.

---
### Problem Solved Check
- [x] 1회 24/06/12 
- [x] 2회 24/07/31
- [ ] 3회

~~~
def solution(answers):
    answer = []
    test_taker = [[1, 2, 3, 4, 5],
                  [2, 1, 2, 3, 2, 4, 2, 5],
                  [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]
    collect = [0]*3
    for i in range(len(answers)):
        for j in range(3):
            if answers[i] == test_taker[j][i%len(test_taker[j])]:
                collect[j] += 1
    result = max(collect)
    for i in range(3):
        if collect[i] == result:
            answer.append(i+1)
    return answer
    
~~~
~~~
def solution(answers):
    m1 = [1, 2, 3, 4, 5]
    m2 = [2, 1, 2, 3, 2, 4, 2, 5]
    m3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    answer = []
    r1 = scoring(answers, m1)
    r2 = scoring(answers, m2)
    r3 = scoring(answers, m3)

    result = max(r1, r2, r3)
    if r1 == result:
        answer.append(1)
    if r2 == result:
        answer.append(2)
    if r3 == result:
        answer.append(3)
    return answer


def scoring(answers, method):
    result = 0
    for i in range(len(answers)):
        index = i % len(method)
        if answers[i] == method[index]:
            result += 1
    return result
    
~~~