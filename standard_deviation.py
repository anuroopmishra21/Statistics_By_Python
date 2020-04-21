#without using numpy
n=int(input())
x=list(map(int, input().split(" ")))
x.sort()
mean=sum(x)/n
Sum=0
for i in range(n):
    Sum+=(mean-x[i])*(mean-x[i])
std_deviation=(Sum/n)**0.5
print(round(std_deviation,1))