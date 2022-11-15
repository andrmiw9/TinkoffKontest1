# (Code parser)
data = {}

with open('input.txt', 'r') as f:
    for line in f.readlines():
        line = line.rstrip()
        print(line)

        if line == '{':
            pass
        elif line == '}':
            pass
        else:
            line = line.split('=')
            try:  # число
                line[1] = int(line[1])

                data[line[0]] = line[1]
            except Exception:  # переменная
                
                pass

    pass

print(data)
