# # def hello():
# #     print('hello')


# # def decor(func):
# #     def wrapper():
# #         print('Логирование...')
# #         func()
# #     return wrapper

# # func = decor(hello)
# # func()


# # 1.
from functools import wraps

# def upper_text(func):
#     @wraps(func)
#     def wrapper():
#         result = func()
#         return result.upper()
    
#     return wrapper



# @upper_text
# def say_hi():
#     return 'всем привет'

# print(say_hi())


# my_number = ‘+996700123456’
# Далее создайте переменную my_number_hidden 
# и зашифруйте переменную my_number так, 
# чтобы остались только последние 2 числа, 
# а остальные все были заменены на символ # например
# ‘###########56’
# все реализовать через декоратор



# решение без декоратора
# my_number = '+996700123456'

# def change_number_to_sharp(number):
#     result = ''

#     for i in number[:-2]:
#         result += '#'

#     result += number [-2:]

#     return result

# print (change_number_to_sharp(my_number))

# решение с декортаторром

def change_number_to_sharp(func):

    @wraps(func)
    def wrapper():
        number = func()
        result = ''

        for _ in number[:-2]:
            result += '#'
        
        result += number [-2:]
        return result

    return wrapper

my_number = '+996700123456'

@change_number_to_sharp
def get_number(number):
    return number

print (get_number(my_number))
