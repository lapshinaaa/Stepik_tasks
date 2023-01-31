def check_parenthesis(expression: str):
    dict_of_parenthesis = {")": "(", "]": "[", "}": "{"}
    stack_of_parenthesis, stack_of_indexes = [], []
    index = 1

    list_of_chars = []
    for char in expression:
        list_of_chars.append(char)

    for char in list_of_chars:
        if char in dict_of_parenthesis.values():
            stack_of_parenthesis.append(char)
            stack_of_indexes.append(index)
            index += 1

        elif char in dict_of_parenthesis.keys():
            if len(stack_of_parenthesis) != 0:
                if stack_of_parenthesis.pop() == dict_of_parenthesis[char]:
                    stack_of_indexes.pop()
                    index += 1

                else:
                    return index

            else:
                return index

        else:
            index += 1

    return "Success" if len(stack_of_parenthesis) == 0 else stack_of_indexes[-1]


print(check_parenthesis(str(input())))

