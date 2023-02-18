size_of_array = int(input())
list_of_nodes = list(map(int, input().split()))
array_of_operations = []    # to keep track of all the operations


def sift_down(i, list_with_nodes: list, size: int):
    """ Recursive function for sifting down the tree"""

    max_index = i
    left_node = left_child(i)

    if left_node < size and list_with_nodes[left_node] < list_with_nodes[max_index]:
        max_index = left_node

    right_node = right_child(i)

    if right_node < size and list_with_nodes[right_node] < list_with_nodes[max_index]:
        max_index = right_node

    if i != max_index:
        array_of_operations.append((i, max_index))
        list_with_nodes[i], list_with_nodes[max_index] = list_with_nodes[max_index], list_with_nodes[i]
        sift_down(max_index, list_with_nodes, size)


def left_child(i):
    return 2 * i + 1


def right_child(i):
    return 2 * i + 2


def build_heap(list_with_nodes: list, size: int):
    n = size
    for i in range((n - 1) // 2, -1, -1):
        sift_down(i, list_with_nodes, size)


build_heap(list_of_nodes, size_of_array)

print(len(array_of_operations))
for operation in array_of_operations:
    print(*operation)
