#code for normal distribution
import math
miu, sigma=list(map(float, input().split(" ")))
l=float(input())
b1, b2=list(map(float, input().split(" ")))
cdf = lambda x: 0.5 * (1 + math.erf((x - miu) / (sigma * (2 ** 0.5))))
print('{:.3f}'.format(cdf(l)))
print('{:.3f}'.format(cdf(b2) - cdf(b1)))