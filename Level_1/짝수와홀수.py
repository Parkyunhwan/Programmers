# == 은 값은 값일 때 참 is는 같은 객체 일 때 참이다.
def solution(num):
    answer = 'Odd'
    if (num%2) == 0 :
        answer = 'Even'
    return answer