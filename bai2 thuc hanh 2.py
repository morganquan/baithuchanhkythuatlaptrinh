print("Pham Viet Quan Mssv 23575202161002")
import math;
x1=int(input("Enter x1--->"))
y1=int(input("Enter y1--->"))

x2=int(input("Enter x2--->"))
y2=int(input("Enter y2--->"))

d1 = (x2 - x1) * (x2 -x1);
d2 = (y2 -y1) * (y2 -y1);
res = math.sqrt(d1+d2)
print ("Distance between two points:",res);
