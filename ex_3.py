def factorial(entry: int):
    first_element = entry
    result = 0
    is_one = False

    if not entry or entry == 0 or entry == 1:
        return 1

    while not is_one:
        if first_element == entry:
            result = entry * (entry - 1)
        else:
            result = result * (entry - 1)
        entry -= 1
        is_one = True if entry == 1 else False
    return result

if __name__ == '__main__':
    for i in [6, 5, 4, 3, 2, 1, 0]:
        print(f"{i}! = {factorial(i)}")


