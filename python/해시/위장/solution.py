def solution(clothes):
    c = {}
    for cl in clothes:
        c[cl[1]] = c.get(cl[1], 0) + 1
    result = 1
    for val in c.values():
        result *= val + 1
    return result - 1