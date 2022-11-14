# Найти самый длинный цикл в графе (лифты)
entries = int(input())
graph = {}
# entries = 7
# graph = {2: [6, 5, 2, 2], 5: [6], 6: [8], 0: [2]}

for i in range(entries):
    fromm, too = map(int, input().split(' '))
    if fromm in graph:
        graph[fromm].append(too)
    else:
        graph[fromm] = [too]

# print(graph)
mx_floor = max(graph)
# print('max floor: ', mx_floor)

floors = list(graph)
floors.sort()

costs = {key: -1 for key in graph.keys()}  # для каждого этажа иниц-ем -1


def find_max_count(floor):
    count = 0  # счёт каждого этажа

    if costs[floor] != -1:  # оптимизация для уже посчитанных путей для этажей
        return costs[floor]

    if floor == mx_floor:  # базовый случай (предпоследний этаж с последним лифтм)
        flag = False
        for entr in graph[floor]:
            if entr == floor:  # лифты на этот же этаж
                count += 1
            elif not flag:  # считаем последний лифт (с этого этажа на последний этаж)
                count += 1
                flag = True
        costs[floor] = count  # в базу +1 не заносим, тк этаж может оказаться единственным
        return count  # базовый случай.

    maxim = 0  # максимум лифтов
    for val in graph[floor]:
        if val == floor:  # лифты на этот же этаж
            count += 1
            continue
        res = find_max_count(val) + 1  # + 1 чтобы учесть и лифт к val тоже
        if res > maxim:
            maxim = res
    count += maxim
    costs[floor] = count  # заносим в базу уже полностью пройденный этаж для оптимизации
    return count


maxes = []

for fl in floors:
    # print('floor:', fl)
    # print(find_max_count(fl))
    maxes.append(find_max_count(fl))

print(max(maxes))
