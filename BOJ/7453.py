import sys
input = sys.stdin.readline

def binary_search(target):
    s,e = 0 , len(ab)-1

    while s <= e:
        mid = (s+e)//2

        if ab[mid] == target:
            return target
        elif ab[mid] > target:
            e = mid - 1
        else:
            s = mid + 1

    return -1



n = int(input())
field = []
for _ in range(n):
    field.append(list(map(int,input().split())))

ab, cd = [],[]
cnt = 0
for i in range(n):
    for j in range(n):
        ab.append(field[i][0] + field[j][1])
        cd.append(field[i][2] + field[j][3])



# for i in range(len(ab)):
#     for j in range(len(cd)):
#         if ab[i] == -1*cd[j]:
#             cnt += 1
#             #print("with",ab[i],cd[j])




ab.sort()
cd.sort()

l,r = 0,len(cd) - 1
while l <= len(ab)-1 and r >= 0:
    if ab[l] + cd[r] == 0:
        nl = l+1
        nr = r-1
        l_move, r_move =1,1
        while nl <= len(ab)-1 and ab[l] == ab[nl]:
            l_move += 1
            nl += 1
        while nr >= 0 and cd[r] == cd[nr]:
            r_move += 1
            nr -= 1
        cnt += l_move * r_move
        l, r = nl, nr

    elif -1 * ab[l] < cd[r]:
        r -= 1
    else:
        l += 1

#print(field)
# print(ab)
# print(cd)
print(cnt)
