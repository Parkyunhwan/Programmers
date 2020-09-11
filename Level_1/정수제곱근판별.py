# python의 range는 0부터 n+1을 포함하지 않으며 n까지이다.

def solution(n):
    answer = -1
    for i in range(n+1):
        if i*i == n:
            answer = (i+1) * (i+1)
            break
        if i*i > n:
            break
    return answer

# import sqrt from math를 통해 sqrt() 함수를 사용해도 된다.
# 그러나 (1/2)를 **(제곱)함으로 제곱근을 구할 수 있다.
# 또한 sqrt()%1을 하면 제곱근이 정수가 아닌 것을 거를 수 있으므로 엄청난 시간 절약이 가능하다!!

def solution2(n):
    sqrt = n ** (1/2)
    print(sqrt%1)
    if sqrt % 1 == 0:
        return (sqrt + 1) ** 2
    return -1