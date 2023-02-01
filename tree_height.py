n = int(input())
nodes = list(map(int, input().split()))

list_with_relations = [[] for i in range(n + 1)]

for j in range(n):
    list_with_relations[nodes[j]] += [j]

root = list_with_relations[-1]    # always the last element
level = 0  # measuring the height of the current tree

while root:                # while root is not an empty list, iterate:
    q, root = root, []     # swapping values: q, root = [1], [] during the first iteration, where q will allows us to find children
    for j in q:
        root += list_with_relations[j]

    level += 1

print(level)

