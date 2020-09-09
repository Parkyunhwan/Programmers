# 자릿수를 재귀함수를 통해 모두 더하는 방법
def sum_digit(number):
    if number < 10:
        return number
    return (number % 10) + sum_digit(number // 10) 



# 무식하게 각각의 자릿수를 str으로 변환 후 다시 int형으로 변환해 더하는 방법
def solution(n):
    N = str(n)
    summ = 0
    for i in N :
        summ += int(i)
    return(summ)