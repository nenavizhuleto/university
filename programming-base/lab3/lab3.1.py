# Объединение двух строк с использованием символа `+` называется конкатенацией (concatenation).

# Python поддерживает умножение строк на числа.


hello = "Hello "

world = 'World'

# Получите строку "Hello World" с помощью конкатенации предыдущих переменных
result = hello + world

# Получите строку "HelloHelloHelloHelloHelloHelloHelloHelloHelloHello" с помощью операций со строками
result = hello * 10

# Получите строку "Hello, World! World World Hello Hello!"  с помощью операций со строками
########
result = (hello + world) * 3



# Вы можете получить доступ к символу строки, если знаете его позицию. Например, str[index] даст символ в позиции index в строке str.

# Запомните! Строки всегда индексируются с 0.

python = "Python"

p_letter = python[0] # Используйте переменную python для получения строки "pthn".
t_letter = python[2] # Используйте переменную python для получения строки "pthn".
h_letter = python[3] # Используйте переменную python для получения строки "pthn".
n_letter = python[-1] # Используйте переменную python для получения строки "pthn".
########

result = p_letter + t_letter + h_letter + n_letter


# В Python индексы также могут быть отрицательными числами. Это позволяет начать отсчет с конца строки. 
# Обратите внимание, что, поскольку -0 совпадает с 0, отрицательные индексы начинаются с -1.
# Таким образом, вы можете использовать отрицательные числа в операторе индексирования для подсчета символов с конца строки.

long_string = "This is a very long string!"

# Используйте отрицательный индекс для получения символа '!' из строки

result = long_string[-1]
