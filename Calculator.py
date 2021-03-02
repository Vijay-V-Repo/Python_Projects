a=0
def calculate():
    operation = input(''' Please type in the math operation:
+ for addition
- for subtraction
* for multiplication
/ for division  : ''')

    number_1 = int(input('Please enter the first number: '))
    number_2 = int(input('Please enter the second number: '))

    if operation == '+':
        print('{} + {} = '.format(number_1, number_2),number_1 + number_2)
        a=number_1 + number_2

    elif operation == '-':
        print('{} - {} = '.format(number_1, number_2),number_1 - number_2)
        a=number_1 - number_2
        
    elif operation == '*':
        print('{} * {} = '.format(number_1, number_2),number_1 * number_2)
        a=number_1 * number_2

    elif operation == '/':
        print('{} / {} = '.format(number_1, number_2),number_1 / number_2)
        a=number_1 / number_2

    else:
        print("You have not typed a valid operator, please run the program again.")
    lastagain(a)       
    
def lastcalculate(a):
    operation = input(''' Please type in the math operation:
+ for addition
- for subtraction
* for multiplication
/ for division  : ''')
    
    number_1 = a
    number_2 = int(input('Please enter the second number: '))

    if operation == '+':
        print('{} + {} = '.format(number_1, number_2),number_1 + number_2)
        a=number_1 + number_2

    elif operation == '-':
        print('{} - {} = '.format(number_1, number_2),number_1 - number_2)
        a=number_1 - number_2
        
    elif operation == '*':
        print('{} * {} = '.format(number_1, number_2),number_1 * number_2)
        a=number_1 * number_2

    elif operation == '/':
        print('{} / {} = '.format(number_1, number_2),number_1 / number_2)
        a=number_1 / number_2

    else:
        print("You have not typed a valid operator, please run the program again.") 
    lastagain(a)        
    
def lastagain(a):
    calc_again = input('''Do you want to calculate again with Last Value?
    Please type Y for YES or N for NO. ''')
    if calc_again.upper() == 'Y':
        lastcalculate(a)
    elif calc_again.upper() == 'N':
        again()
    else:
        lastagain(a)

def again():
    calc_again = input('''Do you want to calculate again with New Value ?
    Please type Y for YES or N for NO. ''')
    if calc_again.upper() == 'Y':
        calculate()
    elif calc_again.upper() == 'N':
        print('See you later.')
    else:
        again()

calculate()