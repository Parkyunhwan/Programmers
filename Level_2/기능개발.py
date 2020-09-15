# velog
# zip에 대한 공부
# math 올림 반올림에 대한 공부
def solution(progresses, speeds):
    date = []
    answer = []
    for i, v in enumerate(progresses):
        temp = speeds[i]
        val = 100 - v
        if val % temp != 0:
            date.append(int(val // temp + 1))
        else:
            date.append(int(val / temp))
    print(date)
    i = 0
    while i < len(date):
        print(i)
        start = date[i]
        num = 1
        while i < len(date) - 1:
            if start >= date[i + 1]:
                i += 1
                num += 1
            else:
                break
        i += 1
        answer.append(num)

    return answer

## 다른 사람 풀이

def solution(progresses, speeds):
    print(progresses)
    print(speeds)
    answer = []
    time = 0
    count = 0
    while len(progresses)> 0:
        if (progresses[0] + time*speeds[0]) >= 100:
            progresses.pop(0)
            speeds.pop(0)
            count += 1
        else:
            if count > 0:
                answer.append(count)
                count = 0
            time += 1
    answer.append(count)
    return answer