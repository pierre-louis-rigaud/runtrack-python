number1 = float(input('Enter first number: '))
operator = input('Enter operator (+,-,*,/,%): ')
number2 = float(input('Enter second number: '))


def calculate(num1,num2,operator):
    if operator == '+':
        result = num1+num2
    elif operator == '-':
        result = num1-num2
    elif operator == '*':
        result =  num1*num2
    elif operator == '/':
        result = num1/num2
    elif operator =='%':
        result =  num1%num2
    return result

print(number1,operator,number2)
result=calculate(number1,number2,operator)
print('=',result)

    

    
