# coding=utf-8
# dfs 풀이

def dfs(routes, N, path, curr):
    path.append(curr)

    if len(path) == N + 1:  # 모든 티켓을 다 쓴거라고 볼 수 있음
        return True

    if curr not in routes:
        path.pop()
        return False

    for i in range(len(routes[curr])):
        end = routes[curr].pop()

        if dfs(routes, N, path, end):
            return True

        routes[curr].insert(0, end)  # 이 길은 불가능하므로 스택의 앞에 넣어서 순서를 바꿔줌

    path.pop()
    return False


def solution(tickets):
    answer = []

    # 그래프 생성
    routes = dict()
    for (start, end) in tickets:
        if not routes.get(start):
            routes[start] = [end]
        else:
            routes[start] += [end]

    # 역순으로 정렬 => 알파벳 빠른것부터 꺼낼 수 있게
    for r in routes.keys():
        routes[r].sort(reverse=True)  # key로참조해서 값 정렬

    N = len(tickets)  # 티켓의 갯수 세기
    path = []

    if dfs(routes, N, path, "ICN"):
        answer = path

    return answer

    answer = path[::-1]
    return answer
#######################################################
# coding=utf-8 => 스택 풀이
##################################
def solution2(tickets):
    answer = []

    # 그래프 생성
    routes = dict()
    for (start, end) in tickets:
        if not routes.get(start):
            routes[start] = [end]
        else:
            routes[start] += [end]

    # 역순으로 정렬 => 알파벳 빠른것부터 꺼낼 수 있게
    for r in routes.keys():
        routes[r].sort(reverse=True)  # key로참조해서 값 정렬

    st = ["ICN"]
    path = []

    while st:
        top = st[-1]
        #  출발지(top)이 routes에 존재하나요?
        #  존재한다면 목적지까지 티켓이 남아있나요?
        if top not in routes or len(routes[top]) == 0:
            path.append(st.pop())  # 더 이상 갈곳이 없으므로 경로에 넣기
        else:  # 목적지가 존재하며 티켓도 남아있을 때
            st.append(routes[top].pop())  # 출발지에서 가장 빠른 도착지

    answer = path[::-1]
    return answer