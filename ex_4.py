def get_multiple(value):
    result = 0
    for item in range(1, 10):
        if item % 3 == 0 or item % 5 == 0:
            result += item
    return result == value


if __name__ == '__main__':
    print(get_multiple(23))


# Obs: Não ficou claro qual era a finalidade da questão.
# "A implementação deve ser capaz de receber por parametro um numero X se ja
# retornado a soma de todos os numeros multiplos de 3 ou 5" ???