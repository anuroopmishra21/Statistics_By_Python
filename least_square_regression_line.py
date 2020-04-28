#code for the least square regression line
s1=list(map(int, input().split(" ")))
s2=list(map(int, input().split(" ")))
s3=list(map(int, input().split(" ")))
s4=list(map(int, input().split(" ")))
s5=list(map(int, input().split(" ")))
sum_x=s1[0]+s2[0]+s3[0]+s4[0]+s5[0]
sum_y=s1[1]+s2[1]+s3[1]+s4[1]+s5[1]
sum_xy=s1[0]*s1[1]+s2[0]*s2[1]+s3[0]*s3[1]+s4[0]*s4[1]+s5[0]*s5[1]
sum_x2=(s1[0]**2)+(s2[0]**2)+(s3[0]**2)+(s4[0]**2)+(s5[0]**2)
sum_x_square=sum_x**2
b=((5*sum_xy)-(sum_x*sum_y))/((5*sum_x2)-sum_x_square)
a=(sum_y/5)-(b*(sum_x/5))
y=a+(b*80)
print(round(y,3))
