#code for poisson distribution 1 without using importing math library
l=float(input())
k=int(input())
def fact(n):
    return 1 if n==1 else n*fact(n-1)
p=(l**k)*(2.71828**(-l))/fact(k)
print("%.3f" %p)