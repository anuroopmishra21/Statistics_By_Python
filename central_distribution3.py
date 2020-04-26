#code for central distribution 3 using math library
import math

s = int(input())
mean = int(input())
std = int(input())
interval = float(input())
z = float(input())
print(round(mean - (std / math.sqrt(s)) * z, 2))
print(round(mean + (std / math.sqrt(s)) * z, 2))