# a O(n) solution using a Deque data structure

import collections

size_of_list = int(input())
list_of_numbers = list(map(int, input().split()))
window = int(input())
output_array = []
left_pointer, right_pointer = 0, 0
deque = collections.deque()  # collecting indexes

while right_pointer < len(list_of_numbers):     # while we're withing a list (within the bounds)
    while deque and list_of_numbers[deque[-1]] < list_of_numbers[right_pointer]:   # checking the rightmost value in the queue
        deque.pop()

    deque.append(right_pointer)

    # if the leftmost value is out of the window bounds, pop it:
    if left_pointer > deque[0]:
        deque.popleft()

    if right_pointer + 1 >= window:
        output_array.append(list_of_numbers[deque[0]])
        left_pointer += 1

    # incrementing pointers:
    right_pointer += 1

print(*output_array)
