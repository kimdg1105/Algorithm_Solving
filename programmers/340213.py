def solution(video_len, pos, op_start, op_end, commands):
    video_minute, video_second = parseVideoLen(video_len)
    video_total_second = video_minute * 60 + video_second

    pos_minute, pos_second = parseVideoLen(pos)
    pos_total_second = pos_minute * 60 + pos_second

    op_start_minute, op_start_second = parseVideoLen(op_start)
    op_start_total_second = op_start_minute * 60 + op_start_second

    op_end_minute, op_end_second = parseVideoLen(op_end)
    op_end_total_second = op_end_minute * 60 + op_end_second

    if op_start_total_second <= pos_total_second <= op_end_total_second:
        pos_total_second = op_end_total_second

    for command in commands:
        if command == "prev":
            if pos_total_second < 10:
                pos_total_second = 0
            else:
                pos_total_second -= 10
        if command == "next":
            if video_total_second - pos_total_second < 10:
                pos_total_second = video_total_second
            else:
                pos_total_second += 10
        if op_start_total_second <= pos_total_second <= op_end_total_second:
            pos_total_second = op_end_total_second

    return parseSecToStr(pos_total_second)


def parseVideoLen(video_len: str):
    split = video_len.split(":")
    return int(split[0]), int(split[1])


def parseSecToStr(sec: int) -> str:
    result = ""

    minute = sec // 60
    second = sec % 60

    if minute < 10:
        result += "0"
    result += str(minute) + ":"

    if second < 10:
        result += "0"
    result += str(second)

    return result


print(solution("34:33", "13:00", "00:55", "02:55", ["prev", "next"]))
print(solution("10:55", "00:05", "00:15", "06:55", ["prev", "next", "next"]))
print(solution("07:22", "04:05", "00:15", "04:07", ["next"]))
