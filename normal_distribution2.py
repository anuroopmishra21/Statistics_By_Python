#code for normal distribution 2
import math
miu, sigma=list(map(float, input().split(" ")))
h=float(input())
p=float(input())
cdf = lambda x: 0.5 * (1 + math.erf((x - miu) / (sigma * (2 ** 0.5))))
print(round((1-cdf(80))*100,2))
print(round((1-cdf(60))*100,2))
print(round((cdf(60))*100,2))