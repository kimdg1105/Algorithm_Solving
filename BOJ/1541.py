y = str(input())
ly = list(y)
# print(ly)
flag = False
ret = []
num_f = True
for i in range(len(ly)):
    if ly[i] != '-' and ly[i] and ly[i] != '(' and ly[i] != ')':
        ret.append(ly[i])
    if ly[i] == '-' and not flag:
        ret.append(ly[i])
        ret.append('(')
        flag = True
        continue
    if ly[i] == '-' and flag:
        ret.append(')')
        ret.append(ly[i])
        ret.append('(')
        continue
    if i == len(ly) - 1 and flag:
        ret.append(')')

for i in range(len(ret)):
    if ret[i] == '0' and (ret[i - 1] == '(' or ret[i -1] == '+' or ret[i -1] == '-'):
        del ret[i + 1]
print(ret)
merge = ''.join(ret)
print(merge)
print(eval(merge))
