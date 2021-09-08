def get_multiple(value: list):
    result = 0
    for item in range(1, 10):
        for multiple in value:
            if item % multiple == 0:
                result += item
    return result


print(get_multiple([5, 3]))
