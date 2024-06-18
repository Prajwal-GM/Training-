arr = list(map(int,input().split()))
n=int(input())
for i in  arr:
    if i==0:
        continue
    if (i<=3):
        c=c+1
    else:
        if(i%3==0):
            c=c+i//3
        else:
            c=c+i//3+1
print(c)
