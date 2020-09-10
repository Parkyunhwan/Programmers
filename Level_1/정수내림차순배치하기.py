# 십의자릿수마다 계산해서 구한 식
def solution(n): 
    sum = 0
    ten = 1
    a = list(str(n))
    a = [int(i) for i in a]
    a.sort()
    print(a)
    for i in a:
        sum += i*ten
        ten *= 10
    return sum

# sorted , join을 통해 int -> str -> list -> int 를 한번에 처리함
def solution(n):
    return int("".join(sorted(list(str(n)), reverse=True)))
