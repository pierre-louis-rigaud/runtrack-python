def calculate(num1,operator, num2):
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

result=calculate(6, "*", 8)
print(result)



    

    
