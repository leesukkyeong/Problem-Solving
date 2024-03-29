def solution(n, lost, reserve):
    answer = [1]*(n+2)
    cnt = 0 

    for i in range(1, n+1):
        if i in lost and i in reserve:
            lost.remove(i)
            reserve.remove(i)

    for i in range(1, n+1):
        if i in lost:
            if answer[i] == 0:
                continue
            answer[i] -= 1 
        if i in reserve:
            if answer[i] == 2:
                continue
            answer[i] += 1 
    
    
    for i in range(1, n+1):
        if answer[i] == 2:
            if answer[i-1] == 0:
                answer[i-1] += 1 
                answer[i] -= 1 
            elif answer[i+1] == 0:
                answer[i+1] += 1
                answer[i] -= 1 
    

    for i in range(1, n+1):
        if answer[i] >= 1:
            cnt += 1 
    return cnt

