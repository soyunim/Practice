n=int(input())
x,y=1,1
plans=list(map(str,input().split()))

for plan in plans:
    if plan=='L' or plan=='l':
        if y==1:
            continue
        y-=1
    elif plan=='R' or plan=='r':
        if y==n:
            continue
        y+=1
    elif plan=='U' or plan=='u':
        if x==1:
            continue
        x-=1
    elif plan=='D' or plan=='d':
        if x==n:
            continue
        x+=1

print(x,y)