def stack_working_process(operation: list, stack: list) -> int:

    """Function to determine functionality of stack with max"""

    name_of_operation = operation[0]    # decoding an operation
    if name_of_operation == "push":
        value = int(operation[1])    # getting the value from request

        if len(stack) == 0 or value > stack[-1][1]:     # if stack is empty or we have a bigger value
            max_value = value

        else:
            max_value = stack[-1][1]

        stack.append([value, max_value])

    elif name_of_operation == "pop":
        if stack:   # if stack is not empty
            stack.pop()

    elif name_of_operation == "max":
        if stack:
            return stack[-1][1]
        else:   # if stack is empty return zero
            return 0


number_of_requests = int(input())
stack_of_operation = []

# creating a list of all the operations
for _ in range(number_of_requests):
    request = list(map(str, input().split()))
    answer = stack_working_process(request, stack_of_operation)

    if type(answer) == int:
        print(answer, '\n')



