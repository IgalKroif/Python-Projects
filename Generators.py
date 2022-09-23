# # Generators: Allow us to write a function that can send back a value and later
# # resume to pick up where it left off.
#
# # This type of function is a generator in Python,
# # allowing us to generate a sequence of values over time.
# # The main difference in syntax will be the use of a 'yield' statement!.
#
# # When a generator function is compiled,
# # they become an object that supports an iteration protocol.
# # That means, when they are called in your code they don't
# # actually return any value and then exit.
#
# # Generator functions will automatically suspend and resume their execution
# # and state around the last point of value generation.
#
# # The advantage is that instead of having to compute an
# # entire series of values up front,
# # the generator computes one value waits until the next value is called for.
#
#
# # def create_cubes(n):
# #     result = []
# #     for x in range(n):
# #         result.append(x ** 3)
# #     return result
# #
# #
# # print(create_cubes(10))
#
#
# # yielding!
#
# # def create_cubes(n):
# #
# #     for x in range(n):
# #         yield x ** 3
# #
# #
# # for x in create_cubes(10):
# #     print(x)
#
#
# # print(create_cubes(10))
#
# # fibionnaci sequence
#
# # def gen_fibon(n):
# #     a = 1
# #     b = 1
# #     for i in range(n):
# #         yield a
# #         a, b = b, a + b
# #
# # for number in gen_fibon(10):
# #     print(number)
#
#
# # NEXT and ITER functions!!
#
# # def simple_gen():
# #     for x in range(3):
# #         yield x
#
#
# #
# # for number in simple_gen():
# #     print(number)
#
# # g = simple_gen()
# # print(next(g))
# # print(next(g))
# #
# # print()
#
# # s = 'hello'
# #
# # for letter in s:
# #     print(letter)
# #
# # s_iter = iter(s)
# #
# # print('\n' + next(s_iter))
#
#
# # Homework!
#
# # def gensquares(N):
# #     for i in range(N):
# #         yield i ** 2
# #
# #
# #
# # for i in gensquares(10):
# #     print(i)
#
# from random import randint
#
#
# def rand_num(low, high, n):
#     for number in range(n):
#         yield randint(low, high)
#
#
# for num in rand_num(1, 10, 12):
#     print(num)
#
#
# s = 'hello'
#
# new_iter = iter(s)
#
# print(next(new_iter))
