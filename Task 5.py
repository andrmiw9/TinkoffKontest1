db_count, req_count = map(int, input().split())
db = []

for i in range(db_count):
    surname = input()
    db.append(surname)

# print('db after entering:', db)
db_s = db.copy()
db_s.sort()
# print('db_s after sorting:', db_s)


def find_in_db_s(num, query):
    for j in db_s:
        if j.startswith(query):
            num -= 1
            if num == 0:
                return db.index(j)
    return None


for i in range(req_count):
    num, query = input().split()
    num = int(num)
    res = find_in_db_s(num, query)
    if res:
        print(res + 1)
    else:
        print(-1)

    pass
