# velog
from queue import Queue  # queue
from collections import deque  # deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    curr_weight = 0
    truck_weights.reverse()
    q = deque()
    # print(truck_weights[-1])
    for i in range(bridge_length):
        q.appendleft(0)

    while len(q) != 0:
        answer += 1
        curr_weight -= q.pop()
        if len(truck_weights) != 0:
            if curr_weight + truck_weights[-1] <= weight:
                curr_weight += truck_weights[-1]

                q.appendleft(truck_weights.pop())
            else:
                q.appendleft(0)
        # print(curr_weight)
    return answer