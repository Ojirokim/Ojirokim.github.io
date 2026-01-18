def solution(k, m, score):
    score.sort(reverse=True)
    price = 0
    if len(score) % m == 0:
        z = len(score) // m
        for x in range(1, (z + 1)):
            price1 = score[x * m - 1] * m
            price += price1
    return price


solution(3, 4, [1, 2, 3, 1, 2, 3, 1])
