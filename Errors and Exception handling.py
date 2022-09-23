# ERRORS AND EXCEPTIONS

"""
try block: This is the block of code to be attempted (may lead to an error)

except block : Block of code will execute in case there is an error in try block.

finally block: A final block of code to be executed, regardless of an error.
"""


def add(n1, n2):
    print(n1 + n2)


number1 = 10
# number2 = input('Please provide a number')
# add(number1,number2) # error
# print('Something happened')

# try:
#     result = 10 + 10  # or 10 + ->'10'<- for error'
# except:
#     print("Hey it looks like you aren't adding correctly!")
# else:
#     print('add went well')
#     print(result)

# try:
#    f = open('testfile','r')
#    f.write('Write a test line to the file')
# except TypeError:
#     print('There was a type error!')
#
# except OSError:
#     print('Hey you have an OSError')
# finally:
#     print('I always run')


# def ask_for_int():
#     while True:
#         try:
#             result = int(input("Please provide number: "))
#         except:
#             print("Whoops that is not a number!")
#             continue
#         else:
#             print('Yes Thank you!')
#             break


# ask_for_int()

# HOMEWORK SECTION FOR EXCEPTION

"""
HANDLE THE EXCEPTION THROWN BY THE CODE BELOW USING TRY EXCEPT!:
for i in ['a', 'b', 'c']:
    print(i ** 2)
"""
# PROBLEM 1:

# try:
#     for i in ['a', 'b', 'c']:
#         print(i ** 2)
# except TypeError:
#     print('Wrong Type Mate!')
# finally:
#     print('There are letters as a string in a list: A B or C')


""" 
HANDLE THE EXCEPTION THROWN BY THE CODE BELOW USING TRY EXCEPT!
x = 5
y = 0
z = x / 5
"""

# PROBLEM 2:

# x = 5
# y = 0
#
#
# try:
#     z = x / y
# except ZeroDivisionError: #z == ZeroDivisionError:
#     if ZeroDivisionError:
#         print('YO UNABLE TO DIVIDE BY ZERO CHECK YO MATHS!')
# finally:
#     print('ALL DONE')

"""
WRITE A FUNCTION THAT ASKS FOR AN INTEGER AND PRINTS THE SQUARE OF IT USE A WHILE LOOP WITH EXCEPT TRY ELSE!
"""


# def ask_int():
#     while True:
#         try:
#             asking = int(input("GIVE ME YO NUMBER!"))
#
#         except:
#             print('YOU HAVE NOT INPUTTED A NUMBER, CORRECT YOUR MISTAKE!')
#             continue
#         else:
#             print(f"your number squared is: {asking ** 2}")
#             print('YOU HAVE DONE WELL CHILD!')
#             break
#
#
# ask_int()
