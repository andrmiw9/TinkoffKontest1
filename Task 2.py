entrys_count = int(input())
teams = {}

for entry in range(0, entrys_count):
    team = frozenset(input().split(' '))
    if team not in teams:
        teams[team] = 1
    else:
        teams[team] += 1

# print(teams)
# print(teams.keys())
# print(teams.values())
print(max(teams.values()))
