def solution(n):
    answer = []
    for i in range(1, n+1, 2):
        answer.append(i)
    answer.sort()
    return answer