def calc(num1,num2,operation):
    if operation ==  '+':
        return num1 + num2
    if operation ==  '-':
        return num1 - num2
    if operation ==  '*':
        return num1 * num2
    if operation ==  '/':
        return num1 / num2
    if operation == '//':
        return num1 // num2
    if operation ==  '%':
        return num1 % num2
    if operation ==  '**':
        return num1 ** num2
    else:
        return "Enter valid numbers and operations(+,-,*,/,//,%,**)"

print(calc(32,6,'*'))
print(calc(32,6,''))