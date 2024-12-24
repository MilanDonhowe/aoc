from collections import Counter
L1 = [];L2=[];
with open("input", "r") as input:
    lines = input.read().strip().split('\n')
    for line in lines:
        a,b = line.split()
        L1.append(int(a))
        L2.append(int(b))
    differences = [abs(a-b) for a, b in zip(sorted(L1),sorted(L2))]
    instances = Counter(L2)
    similarity_score = sum([a * instances[a] for a in L1])

print("Part 1:", sum(differences))
print("Part 2:", similarity_score)