n, m = map(int,input().split())
lan = [int(input()) for _ in range(n)]

so, dae = 1, max(lan)
while so <= dae:
    mid = (so + dae)//2
    cnt = 0
    for i in lan:
        cnt += i//mid 
    if cnt >= m: so = mid + 1
    else: dae = mid -1
print(dae)

