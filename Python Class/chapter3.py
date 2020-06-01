'''
Lesson 3 Function
1. What's function?
Function is to define some code snips which needs to re-use in future.
'''

# Demostrate of code without function
# Noted: line 10 to 14 are duplicated and can be grouped as a function
'''
x = int(input('please choose first number and write on computer.'))
r = 0
for i in range(1, x + 1):
    r = r+i

print(r)

x = int(input('please choose second number and write on computer.'))
r = 0
for i in range(1, x + 1):
    r = r+i

print(r)
'''

"""
How to define a function
def functionName(arg,...):
    ...
    return

"""

# Demo of a function
'''
def calculator(msg):
    x=int(input(msg))
    r = 0
    for i in range(1, x + 1):
        r = r+i

    print(r)

calculator('please choose first number and write on computer.')
calculator('please choose second number and write on computer.')
'''

# Another demo of function can return value
'''

def mySum(n):
    try:
        r = 0
        for i in range(1, n + 1):
            r = r+i

        return r
    except:
        print(n+' is not a number, please use number only.')
        return 0


x = mySum('10')
x = x + mySum(10)

print(x)
'''

# Demo of arg key words
'''
l = [1, 2, 3, 4, 5, 6]
i = 10
s = 'Hello'
f = 10.1
d = {
    'Name': 'Aubrey',
    'Age': 9,
    'School': 'SD'
    }
# sep arg
print('Hello', end=' ')
print('World')

# print int
print(i)

# print float
print(f)

# print string
print(s)

# print list
print(l)

# print dictionary
print(d)
'''

# Variable domain
def f1():
    global x
    x=x+1
    print(x)


x = 1
f1()
print(x)


def myDivid(number, dividedBy):
    try:
        return number / dividedBy
    except ZeroDivisionError:
        print('Error: Zero cannt be divided')
    execpt TypeError:
        print('Error: Only number accepted.')


x1 = 10
x2 = '10'

r = myDivid(x1, x2)

print(r)
