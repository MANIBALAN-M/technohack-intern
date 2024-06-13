print('what did you want to convert')
print("if you want to convert celsius to fahrenheit enter 'f'")
print("if you want to convert fahrenheit to celsius enter 'c'")
action = input('enter your action: ')
def print_fah (value):            
    fah = (int(value) * (9/5)) + 32
    return fah

def print_cel (value):
    cel = (5/9) * (int(value) - 32)
    return cel
value = input('enter the value: ') 
if action == 'f':
    print(f'the fahrenheit of celsius {value} is ',print_fah(value))
    
elif action == 'c':
    print(f'the celsius of fahrenheit {value} is ',print_cel(value))
    
else:
    print('please enter valid action')