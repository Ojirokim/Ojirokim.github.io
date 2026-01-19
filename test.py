def solution(number, limit, power):
    answer = 0
    for i in range(1, number+1):
        amount = 0
        for j in range(1, i+1):
            if i%j==0:
                amount += 1
        if amount > limit:
            answer += power
        else:
            answer += amount
return answer


solution(10, 3, 2)
