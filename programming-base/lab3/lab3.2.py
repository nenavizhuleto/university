# Ввод данных с клавиатуры осуществляется с помощью функции input(). 


a = input()  		# В переменную a записывается введенное с клавиатура значение 


print(a) 



name = input("What is your name?")  # Текст в скобках выводится перед считыванием данных 

print(...)    		

# Дополните программу так, чтобы она выводила на экран “Hello, <ваше имя>” 

 



"""
Функция input() возвращает только строковые значения.
Если вам нужны данные другого типа, введенное значение нужно явно преобразовать в необходимый тип
"""



a = int(input()) 	# Преобразование введенной строки к целочисленному типу данных 

b = float(input()) 		# Считайте с клавиатуры вещественное число. Используйте функцию float()
print(a + b) 		# Выведите на экран сумму a и b 
