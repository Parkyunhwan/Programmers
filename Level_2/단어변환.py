from collections import deque

global words


def possible_word(curr, dist):
    possible = []
    for word in words:
        count = 0
        for i in range(len(curr)):
            if word[i] != curr[i]:
                count += 1
        if count == 1:
            if not dist.get(word):
                dist[word] = dist[curr] + 1
                possible.append(word)
    return possible


def bfs(curr_word, target):
    q = deque()
    dist = {curr_word: 0}
    q.append(curr_word)
    while q:
        curr = q.popleft()
        if curr == target:
            return dist[target]
        in_word = possible_word(curr, dist)
        for word in in_word:
            q.append(word)


def solution(begin, target, word):
    global words
    words = word
    if target not in words:
        return 0
    answer = 0
    return bfs(begin, target)