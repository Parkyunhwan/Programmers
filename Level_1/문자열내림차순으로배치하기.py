## 반대로 sorting하는 함수가 있다는 것은 알았지만 기억이나지않아 버블소팅으로 풀었다.
## 버블소팅은 소팅할 수록 범위가 주는 것이 특징이다.

def solution(s):
    s = list(s)
    for i in range(len(s)):
        for j in range(len(s)-i-1):
            if s[j] < s[j+1]:
                temp = s[j+1]
                s[j+1] = s[j]
                s[j] = temp
    print(s)
    return ''.join(s)


## sorted()는 list로 반환하고 sort() 함수는 list의 메소드 중 하나이다.
## 따라서 sorted()는 반복할 수 있는 모든 객체에 적용이 가능하나 저장되진 않습니다. sort()는 list만 가능하며 list에 저장됩니다.

def solution(s):
    return ''.join(sorted(s,reverse=True))
    # return s.sort(reverse=True)