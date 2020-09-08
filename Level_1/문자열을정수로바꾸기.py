# int(?) 는 다른 타입의 변수형을 int형으로 바꾸는 것이다.
# 이때 주의할 점은 int 안에 숫자이외의 특수문자가 존재해서는 안된다는 점이다.
def solution(s):
    if s[len(s)-1]=='-':
        num = int(s[1:])*-1
    elif s[len(s)-1]=='+':
        num = int(s[1:])
    else:
        num = int(s)
    return num

#### bool 표현을 이용한다면 먼저 나온 부호를 나중에 적용시킬 수 있다. 왜나면 첨에는 answer가 0 이기 때문에 부호를 적용시킬수 없다.
def solution(s):
    answer = 0 
    plus = 1
    for i in range(len(s)):
        if s[i] == '-':
            #answer *= -1
            plus = -1
        elif s[i] == '+':
            #answer *= +1
            plus = 1
        else:
            answer = answer*10 + int(s[i])
    answer = answer*plus
    return answer