from collections import deque


def package_processing(size_of_buffer: int, packages: list):
    buffer_queue = deque([], maxlen=size_of_buffer)   # deque as a representation of buffer
    starting_time = []

    for i in range(size_of_buffer):
        buffer_queue.append(0)

    for package in packages:
        if buffer_queue[0] <= package[0]:
            starting_time.append(max(package[0], buffer_queue[-1]))
            buffer_queue.append(max(package[0], buffer_queue[-1]) + package[1])  # + time to process current package

        else:
            starting_time.append(-1)

    return starting_time


size, number_of_packages = map(int, input().split())
arrival_duration = []

for _ in range(number_of_packages):
    arrival_duration.append(list(map(int, input().split())))

print("\n".join(map(str, package_processing(size, arrival_duration))))
