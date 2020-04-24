def fact(n):
    return 1 if n == 0 else n*fact(n-1)

def comb(n, x):
    return fact(n) / (fact(x) * fact(n-x))

def b(x, n, p):
    return comb(n, x) * p**x * (1-p)**(n-x)

d, n = list(map(int, input().split(" ")))
print(round(sum([b(i, n, d/100 ) for i in range(0, 3)]), 3))
print(round(sum([b(i, n, d/100 ) for i in range(2, n+1)]), 3))