gl_plan = input()
otr_count = int(input())

if (not gl_plan or otr_count < 1):
    exit(-1)

# maxotr = [1, len(plan)]
cached = {}
# cached[' '.join(str(x) for x in maxotr)] = 9
print(cached)


def find_next_ch(char):
    pass


def fun(otrezok):
    plan = gl_plan[otrezok[0] - 1:otrezok[1]]
    # print('local plan:', plan)
    moves: int = 0
    last_p: int = 0

    while True:
        minim = min(plan)
        # print('plan min:', minim)
        if minim == '{':  # выходим, тк букв не осталось (базовый случай)
            break

        pointer = plan.index(minim)  # ищем индекс мин символа
        if pointer < last_p:  # если индекс меньше текущего, то значит мы прошли до конца строки + индекс с начала
            moves += len(plan) - last_p + 1

        moves += pointer - last_p
        plan = plan.replace(minim, '{', 1)  # заменяем символ на пробел для корректной работы min()
        last_p = pointer

        # print('plan:', plan)
        # print('p:', pointer)
        # print('moves:', moves)
    return moves


for i in range(otr_count):
    podotr_str = input()
    if podotr_str in cached:  # оптимизации (кэш)
        print(cached[podotr_str])
        continue

    podotr = [int(v) for v in podotr_str.split()]
    # print(podotr)

    if podotr[0] == podotr[1]:  # оптимизации (совпадающие границы подотрезка)
        print(1)
        cached[podotr_str] = 1
        continue

    res = fun(podotr)
    if res > 0:
        cached[podotr_str] = res
        print(res)

    pass
