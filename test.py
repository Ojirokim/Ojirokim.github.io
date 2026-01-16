k = 4
score =[0, 300, 40, 300, 20, 70, 150, 50, 500, 1000]
def solution(k, score):
    answer = []
    thelist=[]
    for inde, x in enumerate(score):
        if inde<k:
            thelist.append(x)
        else:
            if min(thelist)<x:
                thelist.append(x)
                thelist.sort()
                thelist=thelist[1:]
        answer.append(min(thelist))
    return answer
solution(k, score)