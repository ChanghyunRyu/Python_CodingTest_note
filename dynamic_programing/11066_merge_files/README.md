## 11066번 파일 합치기

---

시간 제한: 2초, 메모리 제한: 256MB

소설가인 김대전은 소설을 여러 장(chapter)으로 나누어 쓰는데, 각 장은 각각 다른 파일에 저장하곤 한다. 소설의 모든 장을 쓰고 나서는 각 장이 쓰여진 파일을 합쳐서 최종적으로 소설의 완성본이 들어있는 한 개의 파일을 만든다. 이 과정에서 두 개의 파일을 합쳐서 하나의 임시파일을 만들고, 이 임시파일이나 원래의 파일을 계속 두 개씩 합쳐서 소설의 여러 장들이 연속이 되도록 파일을 합쳐나가고, 최종적으로는 하나의 파일로 합친다. 두 개의 파일을 합칠 때 필요한 비용(시간 등)이 두 파일 크기의 합이라고 가정할 때, 최종적인 한 개의 파일을 완성하는데 필요한 비용의 총 합을 계산하시오.

예를 들어, C1, C2, C3, C4가 연속적인 네 개의 장을 수록하고 있는 파일이고, 파일 크기가 각각 40, 30, 30, 50 이라고 하자. 이 파일들을 합치는 과정에서, 먼저 C2와 C3를 합쳐서 임시파일 X1을 만든다. 이때 비용 60이 필요하다. 그 다음으로 C1과 X1을 합쳐 임시파일 X2를 만들면 비용 100이 필요하다. 최종적으로 X2와 C4를 합쳐 최종파일을 만들면 비용 150이 필요하다. 따라서, 최종의 한 파일을 만드는데 필요한 비용의 합은 60+100+150=310 이다. 다른 방법으로 파일을 합치면 비용을 줄일 수 있다. 먼저 C1과 C2를 합쳐 임시파일 Y1을 만들고, C3와 C4를 합쳐 임시파일 Y2를 만들고, 최종적으로 Y1과 Y2를 합쳐 최종파일을 만들 수 있다. 이때 필요한 총 비용은 70+80+150=300 이다.

소설의 각 장들이 수록되어 있는 파일의 크기가 주어졌을 때, 이 파일들을 하나의 파일로 합칠 때 필요한 최소비용을 계산하는 프로그램을 작성하시오.

### 입력

- 프로그램은 표준 입력에서 입력 데이터를 받는다.
- 프로그램의 입력은 T개의 테스트 데이터로 이루어져 있는데, T는 입력의 맨 첫 줄에 주어진다.
- 각 테스트 데이터는 두 개의 행으로 주어지는데, 첫 행에는 소설을 구성하는 장의 수를 나타내는 양의 정수 K (3 ≤ K ≤ 500)가 주어진다. 
- 두 번째 행에는 1장부터 K장까지 수록한 파일의 크기를 나타내는 양의 정수 K개가 주어진다. 파일의 크기는 10,000을 초과하지 않는다.

### 출력

- 프로그램은 표준 출력에 출력한다. 
- 각 테스트 데이터마다 정확히 한 행에 출력하는데, 모든 장을 합치는데 필요한 최소비용을 출력한다.

---

### Problem Solved Check

- [x] 1회
- [ ] 2회
- [ ] 3회

곤혹을 많이 치룬 문제다. 동적계획법 문제를 간만에 푼 것도 있겠지만 갈피를 잡지 못해 결국 풀이를 참고했다.  

최단 경로 알고리즘의 플로이드-워셜 알고리즘과 유사한 부분이 있다.  
플로이드-워셜 알고리즘은 한 노드 K를 선택하고 다른 나머지 노드 A, B를 선택하여,  
Path(A, B) = min(Path(A, B), Path(A, K)+Path(K, B)) 형태로 문제를 해결한다.

해당 문제도 비슷한 형식으로 문제를 해결한다.  
dp[i][j] = i번째부터 j번째까지 파일을 합치는 최솟값.  

이때 i와 j 사이의 숫자 k가 있다고 하자. (i ≤ k ≤ j)  
i부터 k까지 파일을 합치는 최솟값 = dp[i][k], k+1부터 j까지 파일을 합치는 최솟값 = dp[k+1][j] 이게 된다.  
다시 이 두 파일(i~k까지 합친 파일, k+1~j까지 합친 파일)을 합치는 데에 드는 비용 = i~k까지 파일을 합이다.  
따라서 모든 k에 대하여,  

dp[i][j] = min(dp[i][j], dp[i][k]+dp[k+1][j]+sum(i,j))  
을 통해 문제의 해답을 구할 수 있다.

~~~
import sys
INF = int(1e9)

t = int(input())
for _ in range(t):
    k = int(sys.stdin.readline().rstrip())
    files = list(map(int, sys.stdin.readline().split()))

    pfs = [0]*(k+1)
    pfs[0] = 0
    dp = [[INF]*k for _ in range(k)]
    for i in range(k):
        pfs[i+1] = pfs[i]+files[i]
        dp[i][i] = 0

    for d in range(1, k):
        for start in range(k-d):
            end = start+d
            for mid in range(start, end):
                dp[start][end] = min(dp[start][end], dp[start][mid]+dp[mid+1][end]+pfs[end+1]-pfs[start])

    print(dp[0][k-1])
~~~

단, 해당 해답을 제출해보면 알겠지만 **PyPy3로 제출해야지만 시간초과가 나지 않는다.**  
이를 해결하기 위해서는 동적계획법 최적화하여야 한다.  

다음은 동적계획법 최적화 방법 중 하나인 Knuth's Optimization을 사용하는 방법이다.  
원래는 i~j 사이의 모든 숫자 k를 검사하였고 이 때문에 거의 O(n^3)의 시간복잡도를 지녔지만 이를 사용하면 O(n^2)의 시간복잡도를 가지게 된다.  

Knuth's Optimization에 대해서는 동적계획법에 설명해놓을 생각이다.

~~~
import sys
INF = int(1e9)

t = int(input())
for _ in range(t):
    k = int(sys.stdin.readline().rstrip())
    files = list(map(int, sys.stdin.readline().split()))

    pfs = [0]*(k+1)
    num = [[0]*k for _ in range(k)]
    dp = [[0]*k for _ in range(k)]
    for i in range(k):
        num[i][i] = i
        pfs[i+1] = pfs[i]+files[i]

    for d in range(1, k):
        for start in range(k-d):
            end = start+d
            dp[start][end] = INF
            for mid in range(num[start][end-1], min(num[start+1][end]+1, end)):
                cost = dp[start][mid]+dp[mid+1][end]+pfs[end+1]-pfs[start]
                if dp[start][end] > cost:
                    dp[start][end] = cost
                    num[start][end] = mid

    print(dp[0][k-1])

~~~
