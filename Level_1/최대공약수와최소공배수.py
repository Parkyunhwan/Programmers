# version1
# 유클리드 호제법을 이용한 최소공배수 최대공약수 구하기
# 작은 값은 big으로 간다. 서로의 나머지는 small로 간다. small이 0이 될 때까지 계속한다.
def gcd(a, b):
    while b != 0:
        tmp = a % b
        a = b
        b = tmp
    return a

def solution(n, m):
    answer = []
    if (n < m):
        tmp = n  # 3
        n = m  # 12
        m = tmp  # 3
    temp = gcd(n, m)
    answer.append(temp)
    answer.append((n * m) / temp)
    return answer

# version2
# 파이썬의 특성을 이용해서 한번에 계산해본 버전
def gcdlcd(n, m):
    n , m = max(n, m), min(n, m)
    a , b = n , m
    while m != 0:
        tmp , n = n%m , m
        m = tmp
    return [n,(a*b)/n]