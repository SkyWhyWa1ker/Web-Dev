def func(a, b, c, d):
    return min(a, b, c, d)


a, b, c, d = map(int, input().split())

print(func(a, b, c, d))
