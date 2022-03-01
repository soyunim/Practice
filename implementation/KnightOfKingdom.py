input_data=input()
row=int(input_data[1])
col=int(ord(input_data[0])-ord('a'))+1

directions=[(2,1),(2,-1),(-2,1),(-2,-1),(1,2),(-1,2),(1,-2),(-1,-2)]

result=0

for direction in directions:
    n_row=row+direction[1]
    n_col=col+direction[0]
    if n_row>=1 and n_row<=8 and n_col>=1 and n_col<=8:
        result+=1

print(result)