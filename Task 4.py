d = {}

for i in range(10):
    d[i] = d.get(i, 0) + 1

print(d)