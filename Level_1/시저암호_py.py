## v1

def solution(s, n):
    answer = []
    print(ord('a'),ord('A'),ord('z'),ord('Z'))
    for i in s:
        print(i)
        print( ord(i) )
        if ord('a') <= ord(i) <= ord('z'):
            print("aa"+ chr( (ord(i)+n-ord('a'))%26 + ord('a') ) )
            answer += chr( (ord(i)+n-ord('a'))%26 + ord('a') )        
        elif ord('A') <= ord(i) <= ord('Z'):
            print("bb"+ chr( (ord(i)+n-ord('A'))%26 + ord('A') ) )
            answer +=  chr( (ord(i)+n-ord('A'))%26 + ord('A') )
        else :
            answer += ' '
                
    return ''.join(answer)

## v2

def solution(s, n):
    # string -> 즉 s 에 할당은 불가능하다.
    answer = list(s)
    for i in range(len(s)):
        if answer[i].isupper():
            answer[i] = chr( (ord(answer[i])+n-ord('A'))%26 + ord('A'))
        elif answer[i].islower():
            answer[i] = chr( (ord(answer[i])+n-ord('a'))%26 + ord('a'))
        print(answer)
    return ''.join(answer)