N,C = map(int,input().split())
house = []
for _ in range(N):
    house.append(int(input()))


house.sort()

start = 1
end = house[-1] - house[0]
ret = 0
while start <= end:
    mid = (start + end )//2
    old = house[0]
    cnt = 1

    # print("now mid,", mid)
    for i in range(1,len(house)):
        # print("house idx, val",i,house[i])
        if house[i] >= old + mid:
            cnt += 1
            old = house[i]
            # print("cnt up,",cnt)

    if cnt >= C:
        start = mid+1
        ret = mid
    else:
        end = mid-1


print(ret)