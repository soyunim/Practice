#n개의 수 / m번째 자리까지 / 한 숫자당 k번 더하기
n, m, k = map(int, input().split())
#n개의 수 입력받기
data = list(map(int, input().split()))

data.sort(reverse=True)
first=data[0]
second=data[1]

result = 0

while True:
    #k번 반복
    for i in range(k):
        if m == 0:
            break
        result += first
        m-=1
    if m == 0:
        break
    result+=second
    m-=1

print(result)
