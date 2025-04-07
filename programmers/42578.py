def solution(clothes):

    dict = {}
    for cloth in clothes:
        if cloth[1] not in dict:
            dict[cloth[1]] = 0
        dict[cloth[1]] += 1

    mix = 1
    for k, v in dict.items():
        mix = mix * (v + 1)

    return mix - 1


print(
    solution(
        [["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]]
    )
)
