# for문은 수동 sum을 위해서 존재
def solution(arr):
    answer = 0
    for i in arr:
        answer += i
    answer /= len(arr)
    
    return answer

# 제일 중요한 것은 zero division 예외처리 문제 이며 sum()함수를 사용함 mean()함수는 기본 라이브러리에는 존재하지 않는 듯 하다.
def solution(arr):
    if len(arr) == 0:
        return 0
    return sum(arr) / len(arr)