def basic_op(operator, value1, value2):
    if operator == '+':
        return value1 + value2
    elif operator == '-':
        return value1 - value2
    elif operator == '*':
        return value1 * value2
    elif operator == '/':
        if value2 == '0':
            return 'Error, division por cero'
        else: 
            return value1 / value2
    else: 
        return 'Valor invalido'
print(basic_op('+', 10, 5))
print(basic_op('-', 10, 7))
print(basic_op('*', 10, 7))
print(basic_op('/', 100, 5))