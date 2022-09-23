# Decorators!

# Decorators, allow us to decorate a function. they also allow us to tack
# on extra functionality to an already existing function.

# They use the @ operator and are then placed on top of the original function.

# def hello(name='Igal'):
#     print('The hello() function has been executed')
#
#     def greet():
#         return '\t This is the greet function inside hello'
#
#     def welcome():
#         return '\t This is welcome inside hello'
#
#     print('I am going to return a function!!')
#
#     if name == 'Igal':
#         return greet()
#     else:
#         return welcome()
#
#
# my_new_func = hello('Igal')  # you don't Have to type the default name!!
#
# print(my_new_func)


# def hello():
#     return 'Hi Jose'
#
#
# def other(some_def_func):
#     print('Other code runs here')
#     print(some_def_func())
#
#
# other(hello)

def new_decorator(original_func):
    def wrap_func():
        print('Some extra code, before the original function')

        original_func()

        print('Some extra code, After the original function.')

    return wrap_func()


def func_needs_decorator():
    print('I want to be decorated!')


new_decorator(func_needs_decorator)


@new_decorator
def func_needs_decorator():
    print('I want to be decorated!')


func_needs_decorator()
