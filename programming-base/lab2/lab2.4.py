# Составной оператор присваивания объединяет в себе простое присваивание и арифметическую бинарную операцию (+=, -= и т.д).

number = 9.0

print("number = " + str(number))

number -= 2

print("number = " + str(number))

# Попрактикуйтесь в использовании разных типов составных операторов для переменной number, выведите результаты в консоль

number += number

number *= 2

number -= (number + number / 2) / 2

print("number = " + str(number))