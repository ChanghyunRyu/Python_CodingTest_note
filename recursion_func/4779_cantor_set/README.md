## 4779번 칸토어 집합

---

시간 제한: 1초, 메모리 제한: 128MB

칸토어 집합은 0과 1사이의 실수로 이루어진 집합으로, 구간 [0, 1]에서 시작해서 각 구간을 3등분하여 가운데 구간을 반복적으로 제외하는 방식으로 만든다.  
전체 집합이 유한이라고 가정하고, 다음과 같은 과정을 통해서 칸토어 집합의 근사를 만들어보자.

1. -가 3N개 있는 문자열에서 시작한다.
2. 문자열을 3등분 한 뒤, 가운데 문자열을 공백으로 바꾼다. 이렇게 하면, 선(문자열) 2개가 남는다.
3. 이제 각 선(문자열)을 3등분 하고, 가운데 문자열을 공백으로 바꾼다. 
이 과정은 모든 선의 길이가 1일때 까지 계속 한다.

### 입력

- 입력을 여러 줄로 이루어져 있다. 각 줄에 N이 주어진다. 
- 파일의 끝에서 입력을 멈춘다. N은 0보다 크거나 같고, 12보다 작거나 같은 정수이다.

### 출력

- 입력으로 주어진 N에 대해서, 해당하는 칸토어 집합의 근사를 출력한다.
---
### Problem Solved Check
- [x] 1회 24/06/12
- [ ] 2회
- [ ] 3회

~~~
def cantor(num, is_blank):
    if is_blank:
        return ' '*(3**num)
    if num == 0:
        return '-'
    return ''.join([cantor(num-1, False), cantor(num-1, True), cantor(num-1, False)])


while True:
    try:
        n = int(input())
        print(cantor(n, False))
    except:
        break
        
~~~