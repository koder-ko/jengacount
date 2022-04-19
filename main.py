# 층 형태에 따른 질량중심의 위치와 걸리는 질량, 5번째 인덱스는 총 경우수, 6번째 인덱스는 층수
stairlist = [
             [1.5, 1.5, 3],
             [1.5, 1.5, 2],
             [1.5, 1.5, 1],
             [1, 1.5, 2],
             [1.5, 1, 2],
             [0.5, 1.5, 1],
             [2.5, 1.5, 1],
             [0], [0]
            ]

# 맨 위층이 어느 방향을 보고 있는지. (북/남 쪽 = True 동/서 쪽 = False)
start_way = True


def centor_of_mass(rx, ry, rm, px, py, pm):
    # 질량 중심 계산

    nx = (rx * rm + px * pm) / (pm + rm)
    ny = (ry * rm + py * pm) / (pm + rm)
    nm = pm + rm

    return nx, ny, nm


def bool_change(var: bool):
    if var:
        return False
    else:
        return True


def recursive(rx, ry, rm, way: bool, stairs):
    if stairs > (stairlist[8][0] - 1):
        # 새로운 경우 발견
        stairlist[7][0] += 1
        return

    px = 0
    py = 0
    pm = 0

    for i in range(0, 7):
        if way:
            px = stairlist[i][0]
            py = stairlist[i][1]
            pm = stairlist[i][2]
        else:
            py = stairlist[i][0]
            px = stairlist[i][1]
            pm = stairlist[i][2]

        nx, ny, nm = centor_of_mass(rx, ry, rm, px, py, pm)

        if i == 2:
            if (nx > 2 or nx < 1) and way:
                continue
            elif (ny > 2 or ny < 1) and not way:
                continue

        if i == 3:
            if (nx > 2) and way:
                continue
            elif (ny > 2) and not way:
                continue

        if i == 4:
            if (nx < 1) and way:
                continue
            elif (ny < 1) and not way:
                continue

        if i == 5:
            if (nx > 1) and way:
                continue
            elif (ny > 1) and not way:
                continue

        if i == 6:
            if (nx < 2) and way:
                continue
            elif (ny < 2) and not way:
                continue

        way = bool_change(way)
        recursive(nx, ny, nm, way, stairs + 1)
        way = bool_change(way)
        px = 0
        py = 0
        pm = 0


stairlist[8][0] = int(input("젠가 탑 층 수를 입력하세요:"))
recursive(0, 0, 0, True, 0)
print(stairlist[7][0])
