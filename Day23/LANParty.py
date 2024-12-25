from collections import defaultdict

with open('LANParty_Data.txt') as file:
    data = [[pairs for pairs in line.strip().split('-')] for line in file]
connections = defaultdict(set)
for i, j in data:
    connections[i].add(j)
    connections[j].add(i)

triples = set()
for computer1 in connections:
    for computer2 in connections[computer1]:
        for computer3 in connections[computer2]:
            if computer1 in connections[computer3]:
                if any(computer[0]=='t' for computer in (computer1, computer2, computer3)):
                    triples.add(tuple(sorted((computer1, computer2, computer3))))
print(len(triples))
