print("Pham Viet Quan mssv:235752021610022")
import math
print('giải phương trình ax^2+bx+c=0')
a=float(input('nhập giá trị của a là:'))
b=float(input('nhập giá trị của b là:'))
c=float(input('nhập giá trị của c là:'))
denta=b**2-4*a*c
if denta>0:
    x1=(-b+math.sqrt(denta))/(2*a)
    x2=(-b-math.sqrt(denta))/(2*a)
    print("phương trình có 2 nghiệm lần lượt là",x1,x2)
else:
    if denta<0: 
        print('phương trình không có nghiệm')
    else:
        print('phương trình có 1 nghiệm kép là',-b/(2*a))
