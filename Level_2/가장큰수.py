# 블로그를 참고한 풀이
def solution(numbers):
    li = []
    for nu in numbers:
        s = str(nu)
        nu = list(s)
        i = 0
        while len(nu) <= 4:
            nu.append(nu[i])
            i = (i+1) % len(s)
        nu = int("".join(nu))
        li.append([nu,s])
    li=sorted(li,reverse=True)
    print(int("".join([ i[1] for i in li ])))
    return str(int("".join([ i[1] for i in li ])))

# 다른 사람 풀이
def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: x*3, reverse=True)
    return str(int(''.join(numbers)))