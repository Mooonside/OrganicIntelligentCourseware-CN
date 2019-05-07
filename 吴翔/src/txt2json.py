import json


with open('result.txt') as f:
    N, k = f.readline().split()
    components = []
    for _ in range(int(k)):
        components.append(f.readline().split())

nodes = []
for i in range(int(k)):
    for co in components[i]:
        nodes.append({'id': co, 'group': i+1})

links = []
with open('edgel.txt') as f:
    for line in f.readlines():
        s, t, v = line.split()
        links.append({'source': s, 'target': t, 'value': int(v)})

data = {'nodes': nodes, 'links': links}
with open('result.json', 'w') as f:
    json.dump(data, f)
