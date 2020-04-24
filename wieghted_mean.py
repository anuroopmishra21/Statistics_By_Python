# code for wieghted mean in python
n=int(input())
x=list(map(int, input().split(" ")))
y=list(map(int, input().split(" ")))
W = sum(a*b for a,b in zip(x,y))/sum(y)
print(round(W,1))
