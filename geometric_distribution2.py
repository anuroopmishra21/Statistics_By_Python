# code for geometric distribution 2
n,d=list(map(int, input().split(" ")))
t=int(input())
p=n/d
print(round(sum([(1 - p)**(t - x) * (p) for x in range(1, 6)]), 3))