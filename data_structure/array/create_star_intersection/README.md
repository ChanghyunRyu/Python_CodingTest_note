## 교점에 별 만들기

---

[출처]https://school.programmers.co.kr/learn/courses/30/lessons/87377

Ax + By + C = 0으로 표현할 수 있는 n개의 직선이 주어질 때, 이 직선의 교점 중 정수 좌표에 별을 그리려 합니다.

### 제한 사항

- line의 세로(행) 길이는 2 이상 1,000 이하인 자연수입니다.
  - line의 가로(열) 길이는 3입니다.
  - line의 각 원소는 [A, B, C] 형태입니다.
  - A, B, C는 -100,000 이상 100,000 이하인 정수입니다.
  - 무수히 많은 교점이 생기는 직선 쌍은 주어지지 않습니다.
  - A = 0이면서 B = 0인 경우는 주어지지 않습니다.
- 정답은 1,000 * 1,000 크기 이내에서 표현됩니다.
- 별이 한 개 이상 그려지는 입력만 주어집니다.

---
### Problem Solved Check
- [x] 1회 24/07/15
- [ ] 2회
- [ ] 3회

배열 뒤집기 = arr[::-1]
~~~
from itertools import combinations


def find_intersection(line1, line2):
    a, b, e = line1[0], line1[1], line1[2]
    c, d, f = line2[0], line2[1], line2[2]
    if a*d-b*c != 0:
        x = (b*f-e*d)/(a*d-b*c)
        y = (e*c-a*f)/(a*d-b*c)
    else:
        x = y = False
    return x, y


def solution(lines):
    intersections = []
    x_min = y_min = int(1e15)
    x_max = y_max = -int(1e15)
    for combination in combinations(lines, 2):
        i_x, i_y = find_intersection(combination[0], combination[1])
        if i_x is not False and i_x.is_integer() and i_y.is_integer():
            i_x, i_y = int(i_x), int(i_y)
            if i_x < x_min:
                x_min = i_x
            if i_x > x_max:
                x_max = i_x
            if i_y < y_min:
                y_min = i_y
            if i_y > y_max:
                y_max = i_y
            intersections.append((i_x, i_y))
    answer = [['.']*(x_max-x_min+1) for _ in range(y_max-y_min+1)]
    for x, y in intersections:
        d_x = x-x_min
        d_y = abs(y_min-y)
        answer[d_y][d_x] = '*'
    result = []
    for line in answer:
        result.append(''.join(line))
    return result[::-1]

~~~