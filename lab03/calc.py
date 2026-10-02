print('Калькулятор')

a = float(input('Введите первое число: '))
b = float(input('Введите второе число: '))

operation = str(input('(Доступные операции +, -, *, /): ')).strip()

result = ''
if operation == '+':
    result = f'{a + b}'
elif operation == '-':
    result = f'{a - b}'
elif operation == '*':
    result = f'{a * b}'
elif operation == '/':
    if b == 0: raise ValueError('Division by zero!')
    result = f'{a / b}'

print(result)
