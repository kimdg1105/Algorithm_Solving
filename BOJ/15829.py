l = int(input())
string = input()


word_dict = {chr(ord("a") + i): i + 1 for i in range(26)}


def hash(word: str):
    r = 31
    M = 1234567891
    H = 0
    for i in range(l):
        H += (word_dict[word[i]] * pow(r, i, M)) % M

    return H


print(hash(string))
