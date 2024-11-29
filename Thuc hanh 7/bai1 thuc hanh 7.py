print("Pham Viet Quan mssv 235752021610022")
input_file=open('D:/baith7.txt','r')
for line in input_file:
    l=len(line)
    s=' '
    while(l>=1):
        s=s+line[l-1]
        l=l-1
    print(s)
input_file.close()