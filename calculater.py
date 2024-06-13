'''
simple calculator using functions
'''

import sys
from datetime import datetime

def add(val1,val2):
    sum = val1 + val2
    return sum
    
def sub(val1,val2):
    sum = val1 - val2
    return sum

def mul(val1,val2):
    sum = val1 * val2
    return sum

def div(val1,val2):
    sum = val1 / val2
    return sum            

def mod(val1,val2):
    sum = val1 % val2
    return sum

end = 0
v = 2
val1 = int(input('enter value1: '))

while end==0:
    val2 = int(input(f'enter value{v}: '))
    op = input('enter operation: ')
    if op == '+':
        value = add(val1,val2)
    if op == '-':
        value = sub(val1,val2)
    if op == '*':
        value = mul(val1,val2)
    if op == '/':
        value = div(val1,val2)
    if op == '%':
        value = mod(val1,val2)
    if (op!='+') and (op!='-') and (op!='*') and (op!='/') and (op!='%'):
        print('enter valid operation')
        pass

    ender = input('if you want to end the problem (yes/no): ')
    if ender=='yes':
        end = end + 1
    else:
        val1=value
        v = v + 1

print(f'the answer of your problem is ',value)