def solution(arr):
    answer = int(arr == list(map(list, zip(*arr))))
    return answer 
