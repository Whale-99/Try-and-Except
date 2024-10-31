def add_everything_up(a, b):
    try:
        # Попробуем сложить a и b
        return a + b
    except TypeError:
        # Если возникает TypeError, значит, a и b разных типов
        # Возвращаем строковое представление этих данных вместе, в том же порядке
        return str(a) + str(b)

# Примеры вызовов
print(add_everything_up(123.456, 'строка'))  # Ожидается: '123.456строка'
print(add_everything_up('яблоко', 4215))     # Ожидается: 'яблоко4215'
print(add_everything_up(123.456, 7))         # Ожидается: 130.456
