def solution(tickets):
    answer = []
    visited = [False] * len(tickets)

    def dfs(airport, path):
        if len(path) == len(tickets) + 1:
            answer.append(path)
            return

        for idx, ticket in enumerate(tickets):
            if ticket[0] == airport and not visited[idx]:
                visited[idx] = True
                dfs(ticket[1], path + [ticket[1]])
                visited[idx] = False

    dfs("ICN", ["ICN"])
    answer.sort()

    return answer[0]


print(solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]))
print(
    solution(
        [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL", "SFO"]]
    )
)
print(
    solution(
        [
            ["ICN", "AAA"],
            ["ICN", "CCC"],
            ["CCC", "DDD"],
            ["AAA", "BBB"],
            ["AAA", "BBB"],
            ["DDD", "ICN"],
            ["BBB", "AAA"],
        ]
    )
)
