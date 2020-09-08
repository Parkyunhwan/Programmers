## 하나 하나 비교해서 갯수를 세는 코드이다.
def solution(s):
    li = list(s)
    answer = True
    p = 0
    y = 0
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    print(answer)
    for i in li:
        print(i)
        if i=='p' or i=='P':
            p += 1
        elif i=='y' or i=='Y':
            y += 1
    if(p!=y):
        answer = False
    return answer


#### Count() 함수를 기억하도록하자
#### 일일히 세지 않고 count를 이용하면 굉장히 쉽게 풀 수 있는 방법이다. 
def solution(s):
    return s.lower().count('p') == s.lower().count('y')