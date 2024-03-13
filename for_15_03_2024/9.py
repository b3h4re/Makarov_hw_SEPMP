from time import time


MAX_TURN = 6  # 6 вроде как верное значение, но в принцепе можно использовать более очевидное чило (например 30)
# и даже так будет работать хорошо (максимальное время не превышало у меня 0.5 с при 30)


def format_coord(pos, reverse=False):
    if reverse:
        return chr(pos[0] + 97) + str(pos[1] + 1)
    return ord(pos[0]) - 97, int(pos[1]) - 1


def get_moves_from_position(pos):
    x, y = format_coord(pos)
    modifiers = [
        (1, 2), (1, -2),
        (2, 1), (2, -1),
        (-1, 2), (-1, -2),
        (-2, 1), (-2, -1)
    ]
    next_positions = set()
    for d_x, d_y in modifiers:
        if 0 <= x + d_x <= 7 and 0 <= y + d_y <= 7:
            next_positions.add(format_coord((x+d_x, y+d_y), reverse=True))
    return next_positions


def dist(pos1, pos2):
    x1, y1 = format_coord(pos1)
    x2, y2 = format_coord(pos2)
    return abs(x1 - x2) + abs(y1 - y2)


def search(s1, s2, turn=0, max_turn=MAX_TURN):
    if turn > max_turn:
        return max_turn
    if s1 == s2:
        return turn
    ans = max_turn
    moves1 = get_moves_from_position(s1)
    moves2 = get_moves_from_position(s2)
    if len(moves1.intersection(moves2)) > 0:  # Если это условие не выполнено, то значение dist(s1, s2) >= 4
        return turn+1
    for new_s1 in moves1:
        for new_s2 in moves2:
            if dist(new_s1, new_s2) <= dist(s1, s2):
                ans = min(ans, search(new_s1, new_s2, turn+1, max_turn))
                max_turn = ans
    return ans


pos1, pos2 = input().split()
x1, y1 = format_coord(pos1)
x2, y2 = format_coord(pos2)
color = (lambda x, y: 0 if x % 2 == y % 2 else 1)
if color(x1, y1) != color(x2, y2):
    print(-1)
else:
    print(search(pos1, pos2))

# Проверка максимального времени работы
# all_positions = []
# for i in "abcdefgh":
#     for j in "12345678":
#         all_positions.append(i + j)
# mx = -1
# for pos1 in all_positions:
#     for pos2 in all_positions:
#         t1 = time()
#         x1, y1 = format_coord(pos1)
#         x2, y2 = format_coord(pos2)
#         color = (lambda x, y: 0 if x % 2 == y % 2 else 1)
#         if color(x1, y1) != color(x2, y2):
#             tmp = -1
#         else:
#             tmp = search(pos1, pos2)
#         t2 = time()
#         # print(pos1, pos2, tmp, t2 - t1)
#         if t2 - t1 > mx:
#             print(pos1, pos2, tmp, t2 - t1)
#         mx = max(mx, t2 - t1)
# print(mx)