def solution(genres, plays):
    answer = []
    dict = {}
    play_count = {}

    idx = 0
    for genre, time in zip(genres, plays):
        if genre not in dict:
            dict[genre] = []
            play_count[genre] = 0
        dict[genre].append((idx, time))
        play_count[genre] += time
        idx += 1

    while dict:
        top_genre = max(play_count, key=play_count.get)

        dict[top_genre].sort(key=lambda x: -x[1])

        cnt = 0
        while cnt != 2:
            if not dict[top_genre]:
                break
            answer.append(dict[top_genre].pop(0)[0])
            cnt += 1

        dict.pop(top_genre)
        play_count.pop(top_genre)

    return answer


print(
    solution(["classic", "classic", "classic", "pop", "pop"], [600, 600, 150, 600, 700])
)
