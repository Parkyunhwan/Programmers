# velog
# 나의 풀이
def solution(priorities, location):
    sorting = sorted(priorities)
    i = 0
    num = 0
    while len(sorting)!=0:
        if(i==location and sorting[-1] == priorities[location]):
            num +=1
            break
        elif(sorting[-1] == priorities[i]):
            sorting.pop()
            num +=1
        i = (i+1) % len(priorities)
    return num

# 다른 사람 풀이
# enumerate의 사용
# any의 사용
def solution2(priorities, location):
    queue =  [(i,p) for i,p in enumerate(priorities)]
    answer = 0
    while True:
        cur = queue.pop(0)
        if any(cur[1] < q[1] for q in queue):
            queue.append(cur)
        else:
            answer += 1
            if cur[0] == location:
                return answer