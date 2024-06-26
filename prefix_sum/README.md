# 누적합(Prefix Sum, Cumulative Sum)

누적합(prefix sum)이란, 단어 그대로 **나열된 숫자의 누적된 합**이다.  
수열 An이 있다고 한다면, 누적합 Pn은 P3 = A1 + A2 + A3이 된다.   
즉 Pn = A1 + A2 + ... + An이 되게 된다.


### **왜 사용하는가?**  

수열의 특정 구간의 합을 구한다고 가정해보자.  
구하는 구간의 길이가 M 이라고 하면, 총 M번의 더하기 연산을 수행해야되기 때문에 시간복잡도는 **O(M)** 이 되게 된다.  
총 N개의 구간의 합을 구하게 되면 총 **O(NM)** 의 시간복잡도가 소모된다.

#### 누적합을 이용한 구간 합 구하기

위에서는 길이가 M인 구간합을 구할 때, a(i)+a(i+1)+a(i+2)+...+a(j) 식으로 하나씩 더해주었다.
그러나 누적합을 통해 구하게 되는 경우,  
P(j)   = a(1)+a(2)+...+a(i-1)+a(i+1)+...+a(j)  
p(i-1) = a(1)+a(2)+...+a(i-1)  
즉 i~j 구간의 구간합을 구하는 경우 **누적합 P(j)-P(j-1)으로 하나의 연산을 통해 구할 수 있다.**  
하나의 연산을 하는데 걸리는 시간복잡도는 O(1)이므로,  
N개의 구간합을 구하는 경우, 처음 누적합을 계산하는 데에 걸리는 O(r)이 합쳐져(r은 수열의 크기)
**O(r+N)** 이 걸리게 된다.




