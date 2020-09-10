# 간단한 식이다. 스택처럼 생각해보자
# 가장큰 숫자는 먼저 들어가서 맨 뒤로 가고 가장 작은 수는 맨 앞에 위치하게 될 것 이다.
# //은 C++의 int형 나누기 처럼 소숫점을 남기지 않는다. 그러나 / 연산은 소숫점까지 계산하게 된다.
def solution(n):
    answer = []
    while n is not 0 :
        answer.append(n%10)
        n = n//10
    print(answer)
    return answer

# 내가 풀고 싶언던 코드
# 내가 놓친 것 -> 정수를 이터러블하게 str으로 바꾸고 reverse함수를 사용하기 위해 list로 변환하는 것은 맞지만 그렇게 되면 '문자'가 리스트에 들어가므로
#               '문자'가 아닌 'int'형으로 변환을 각 인덱스마다 시켜줘야만 한다. (18번 코드)
def digit_reverse(n):
    a = list(str(n))
    a.reverse()
    return [int(i) for i in a]
