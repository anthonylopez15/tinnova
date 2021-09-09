
def order_elements(vector):
    elements = len(vector) - 1
    is_ordered = False
    while not is_ordered:
        is_ordered = True
        for i in range(elements):
            if vector[i] > vector[i + 1]:
                vector[i], vector[i + 1] = vector[i + 1], vector[i]
                is_ordered = False
    return vector

if __name__ == '__main__':
    my_elements = [5, 3, 2, 4, 7, 1, 0 ,6]
    print(order_elements(my_elements))