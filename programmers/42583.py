def solution(bridge_length, weight, truck_weights):
    answer = 0
    q = []
    goal = []
    truck_on_brige = 0
    goal_len = len(truck_weights)

    while len(goal) != goal_len:
        for t in q:
            if t[0] == bridge_length:
                goal.append(q.pop(0))
                truck_on_brige -= 1

        total_weight = 0
        for _, w in q:
            total_weight += w

        if truck_weights:
            cur_truck = truck_weights[0]
            if cur_truck + total_weight <= weight:
                q.append([0, truck_weights.pop(0)])
                truck_on_brige += 1

        answer += 1
        for v in q:
            v[0] += 1

    return answer


print(solution(2, 10, [7, 4, 5, 6]))
print(solution(100, 100, [10]))
print(solution(100, 100, [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]))
