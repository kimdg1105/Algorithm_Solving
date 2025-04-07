def solution(genres, plays):
    answer = []
    dict = {}

    idx = 0
    for genre, time in zip(genres, plays):
        if genre not in dict:
            dict[genre] = []
        dict[genre].append((idx, time))
        idx += 1

    phase = 0
    while phase != 2:
        if not dict:
            break
        top_genre = max(dict)

        dict[top_genre].sort(key=lambda x: -x[1])

        cnt = 0
        while cnt != 2:
            if not dict[top_genre]:
                break
            answer.append(dict[top_genre].pop(0)[0])
            cnt += 1
        phase += 1
        dict.pop(top_genre)

    return answer


print(
    solution(["classic", "classic", "classic", "pop", "pop"], [600, 600, 150, 600, 700])
)  # 	[4, 1, 3, 0]
