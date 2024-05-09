## 신입 사원

------

[백준 1946번] 언제나 최고만을 지향하는 굴지의 대기업 진영 주식회사가 신규 사원 채용을 실시한다. 인재 선발 시험은 1차 서류심사와 2차 면접시험으로 이루어진다. 최고만을 지향한다는 기업의 이면에 따라 그들은 최고의 인재들만을 사원으로 선발하고 싶어 한다.  

그래서 진영 주식회사는, 다른 모든 지원자와 비교했을 때 서류심사 성적과 면접시험 성적 중 적어도 하나가 다른 지원자보다 떨어지지 않는 자만 선발한다는 원칙을 세웠다. 즉, 어떤 지원자 A의 성적이 다른 어떤 지원자 B의 성적에 비해 서류 심사 결과와 면접 성적이 모두 떨어진다면 A는 결코 선발되지 않는다.  

이러한 조건을 만족시키면서, 진영 주식회사가 이번 신규 사원 채용에서 선발할 수 있는 신입 사원의 최대 인원수를 구하는 프로그램을 작성하시오.

### 입력

- 첫째 줄에는 테스트 케이스의 개수 T(1 ≤ T ≤ 20)가 주어진다.
- 각 테스트 케이스의 첫째 줄에 지원자의 숫자 N(1 ≤ N ≤ 100,000)이 주어진다.
- 둘째 줄부터 N개 줄에는 각각의 지원자의 서류심사 성적, 면접 성적의 순위가 공백을 사이에 두고 한 줄에 주어진다.
- 두 성적 순위는 모두 1위부터 N위까지 동석차 없이 결정된다고 가정한다.

### 출력

- 각 테스트 케이스에 대해서 진영 주식회사가 선발할 수 있는 신입사원의 최대 인원수를 한 줄에 하나씩 출력한다.

------

### 풀이

합격자는 다른 모든 지원자와 비교했을 때, 두 성적 중 하나라도 떨어지면 안 된다.  
반대로 생각하면 두 시험 중 하나라도 1등을 하게 될 경우, 해당 지원자는 탈락하지 않는다.  

그럼 서류 시험(면접을 기준으로 삼아도 상관 X)을 기준으로 삼아 정렬하여 1등을 합격시킨 후, 다른 시험이 해당 합격자보다 성적이 좋은 사람들을 합격시키면 된다.  

뒤의 지원자들은 앞서 체크한 지원자보다 무조건 서류시험의 성적이 낮으므로, 면접 성적이 더 좋아야만 합격할 수 있기 때문이다.
여기서 새로운 합격자가 나올 때마다 해당 합격자의 면접 시험 등수로 기준을 바꿔주워야 한다.

~~~
import sys

t = int(input())
result = []
for _ in range(t):
    n = int(input())
    applicant = []
    for _ in range(n):
        doc, interview = map(int, sys.stdin.readline().split())
        applicant.append((doc, interview))

    applicant.sort()
    check = applicant[0][1]
    people = 0
    for a in applicant:
        if a[1] <= check:
            people += 1
            check = a[1]
    result.append(people)
for r in result:
    print(r)
~~~