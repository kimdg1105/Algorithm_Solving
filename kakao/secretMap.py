def solution(n, arr1, arr2):
    answer = []
    merge =[]
    bi = []

    for i in range(n):
        merge.append(arr1[i] | arr2[i])

    for i in range(n):
        line = str(format(merge[i],'b'))
        while len(line) != n:
            line = '0' + line
        bi.append(line)

    for i in range(n):
        line = bi[i].replace('1','#')
        line = line.replace('0',' ')
        answer.append(line)

    for i in range(n):
        # print(bi[i])
    return answer

N = int(input())
arr1 = list(map(int,input().split()))
arr2 = list(map(int,input().split()))
solution(N,arr1,arr2)
