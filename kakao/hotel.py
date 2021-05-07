
## 첫 풀이 시, 정확성 100/100 효율성 통과 못함. 

def solution(k, room_number):
    answer = []
    hotel = {}

    for i in range(len(room_number)):
        node = room_number[i]
        visited = [node]
        while node in hotel:
            node = hotel[node]
            visited.append(node)
            # print("now visited:",visited)
        answer.append(node)
        for j in visited:
            hotel[j] = node + 1
        # print(hotel)

    return answer