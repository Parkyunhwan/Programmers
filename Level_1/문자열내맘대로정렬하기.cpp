# version 1
## 먼저 전체 요소 소팅 후 특정 인덱스로 소팅
def solution(strings, n):
    def sortkey(x):
        return x[n]
    strings.sort()
    strings.sort(key=sortkey)
    return strings

# version 2
## sort의 key를 사용하지 않았을 경우

def solution(strings, n):
    for i in range(len(strings)):
        strings[i] = string[i][n] + strings[i]
    strings.sort() # 이를 통해 두 번의 소팅을 한번에 해결할 수 있다.    
    
    # 앞의 문자를 빼줘야함
    for i in range(len(strings)):
        strings[i] = strings[i][1:]
    return strings

# version 3
## lamda 를 사용한 해결법

def solution(strings, n):
    return sorted( sorted(strings), key=lambda x : x[n])
