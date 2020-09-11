# 어떤 풀이나 핵심은 바로 answer에 넣기 전에 서브 리스트를 어떻게 구성할 것이냐가 문제였다.
# zip() 내장함수를 써도 좋고 미리 서브 리스트를 구성해서 append()해도 된다.

def solution(arr1, arr2):
    print(len(arr1))
    answer = []
    for i in range(len(arr1)):
        content = []
        answer.append(content)
        for j in range(len(arr1[i])):
            answer[i].append(arr1[i][j]+arr2[i][j])
    return answer