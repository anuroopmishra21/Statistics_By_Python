#code for geometric distribution 1
n,d=list(map(int, input().split(" ")))
t=int(input())
p=n/d
g=((1-p)**(t-1))*p
print(round(g,3))