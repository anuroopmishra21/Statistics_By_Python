#finding quartiles wihtout using numpy
n=int(input())
x=list(map(int, input().split(" ")))
x.sort()
def median(array,m):
    if m%2==0:
        median=(array[m//2-1]+array[(m//2)])/2
    else:
        median=array[m//2]
    print(round(median))

median(x,n//2)
median(x,n)
if n%2==0:
    median(x[n//2:],n//2)
else:
    median(x[n//2+1:],n//2)