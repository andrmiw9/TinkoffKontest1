import re

n, m = map(int, input().split())

domens = {}  # для небольшого ускорения поиска
r = "^{0}.*?{1}$"

for i in range(n):
    inp = input()
    if inp[0] in domens:
        domens[inp[0]].append(inp)
    else:
        a = []
        a.append(inp)
        domens[inp[0]] = a
    pass

print('domens:', domens)

for i in range(m):
    cstmr = input().split()
    pattern = r.format(cstmr[0], cstmr[1])
    pattern = re.compile(pattern)
    counter = 0
    if cstmr[0][0] not in domens:
        print(0)
        continue

    for entry in domens[cstmr[0][0]]:
        res = re.match(pattern, entry)
        if res:
            counter += 1
    print(counter)

# pattern = copy(r)
# pattern.format(cstmr[0], cstmr[1])
