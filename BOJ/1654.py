K, N = map(int,input().split())

lan_list = []
for _ in range(K):
    lan_list.append(int(input()))


def bin_search(arr,target):

    start = 1
    end = max(arr)

    while start <= end:
        mid = (start + end) // 2
        ret = 0
        for lan in lan_list:
            ret += lan // mid

        # print("now st, end,mid:",start,end,mid)
        # print("now exist",ret)

        if ret >= target:
            start = mid+1
        if ret < target:
            end = mid-1


    return end

print(bin_search(lan_list,N))

