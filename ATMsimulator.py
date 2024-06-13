'''
ATM simulator using dictionary
'''

ac_name = {
'raja':6890 ,
'senthil':10000,
'mani':8700,
'akshat':6780,
'raghav':7500
}
pin_name = {
'raja':1234 ,
'senthil':5678 ,
'mani':9012 ,
'akshat':3456 ,
'raghav':7890
}
name = input('please enter your name: ')
if len(name) < 2 or name.isalpha()==0:
    print('please enter valid information')
for key in ac_name :
    cash = ac_name[key]
    if name == key:
        pin_no = int(input('please enter your pin number: '))
        for k in pin_name :
            value = pin_name[k]
            if (pin_no==value) and k==name:
                print("for withdraw press '1' ")
                print("for balance press '2' ")
                print("for deposite press '3' ")
                action = int(input('enter action: '))
                if action == 1:
                    withdraw = int(input('enter the amount: '))
                    if withdraw > cash or withdraw <= 0:
                        print('please enter valid amount of cash')
                    else:
                        print('please collect your cash')
                    cash = cash - withdraw
                if action == 3:
                    deposite = int(input('enter the amount: '))
                    if  deposite <= 0:
                        print('please enter valid amount of cash')
                    else:
                        print('please put your cash into the machine')
                    cash = cash + deposite
                if action == 2:
                    print(f'your balance amount is {cash}')
                if action!=1 and action!=2 and action!=3:
                    print('please enter valid action')
                print(f'your balance amount is {cash}')
                print('thank you for coming')
                break
print('please enter valid information and valid pin number')            