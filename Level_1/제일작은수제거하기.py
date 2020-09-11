# coding=utf-8
def solution(arr):
    answer = []
    m = min(arr)
    if len(arr) is 1 :
        return [-1]
    else :
        for i in range(len(arr)):
            if m is arr[i] :
                continue
            answer.append(arr[i])
    return answer

# min을 미리 구해두는 것이 속도에서 많은 도움이 된다.
# 리스트를 바로 반환하는 것에 익숙해지면 짧은 코드 작성이 가능하다.
# 그리고 for문 뒤에 if문을 적용시킬수 있음을 기억하
def solution1(arr):
    m = min(arr)
    if len(arr) is 1:
        return [-1]
    return [i for i in arr if i > m]