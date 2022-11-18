# (Code parser)

data = {}  # данные по уровням


def is_in_data_up(subj, cur_level):
    for lvl in data:  # maybe add list slicing, if using of list type of data is chosen
        if lvl > cur_level:  # skip if lvl is deeper, and yes im too lazy to rewrite 'in data + if' to simply 'i in
            # range() + indexes'
            continue
        for entry in data[lvl]:
            if subj == entry:
                return lvl
    return None


def return_old_values(level_to_delete):
    for
    pass


# find_in_data(5)

with open('input.txt', 'r') as f:
    cur_lvl: int = 0
    data[0] = {}

    for line in f.readlines():
        line = line.rstrip()
        print('\n' + line)

        if line == '{':
            cur_lvl += 1
            if cur_lvl not in data:
                data[cur_lvl] = {}
        elif line == '}':
            del data[cur_lvl]  # delete local scope level
            cur_lvl -= 1
            if cur_lvl not in data:
                data[cur_lvl] = {}
            # (for list real-n)check if lvl is < 0, and if is, move data lvls, and delete last context based on cur_lvl
        else:
            line = line.split('=')
            try:  # число
                line[1] = int(line[1])
                print('Number')

                lvl = is_in_data_up(line[0], cur_lvl)
                if lvl is not None:  # var in data
                    data[lvl][line[0]] = line[1]
                    # print(t)
                    # t = line[1]
                else:  # var not in data
                    data[cur_lvl][line[0]] = line[1]
                    # print(line[1])
                # print(line[1])

            except Exception:  # переменная
                print('Exception')

                lvl1 = is_in_data_up(line[0], cur_lvl)
                lvl2 = is_in_data_up(line[1], cur_lvl)

                if lvl1 is not None and lvl2 is not None:  # both vars are in data
                    print('both is')
                    data[lvl1][line[0]] = data[lvl2][line[1]]
                    print(data[lvl1][line[0]])


                elif lvl1 is not None and lvl2 is None:  # first var is in data, its level = lvl1, second is not
                    print('lvl1 only')
                    data[lvl1][line[0]] = 0
                    print(0)

                elif lvl1 is None and lvl2 is not None:  # second in data, first not
                    print('lvl2 only')
                    t = data[lvl2][line[1]]
                    data[cur_lvl][line[0]] = t
                    print(t)

                else:  # both vars are not in data
                    print('both not')
                    data[cur_lvl][line[0]] = 0
                    print(0)

    print(data)
