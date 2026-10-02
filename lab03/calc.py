print('Калькулятор')

a = float(input('Введите первое число: '))
b = float(input('Введите второе число: '))

operation = str(input('(Доступные операции +, -, *): ')).strip()

result = ''
if operation == '+':
    result = f'{a + b}'
elif operation == '-':
    result = f'{a - b}'
elif operation == '/':
    raise ValueError('Данный функционал еще не доступен')

print(result)
