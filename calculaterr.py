
num1=input("Enter a first number: ")
num2=input("Enter a first number: ")

print("1.ADD")
print("2.SUB")
print("3.MUL")
print("4.DIV")

operation=input("Choose number of opration: ")

if operation in '1':
    result=int(num1)+int(num2)
    print(result)
elif operation in '2':
    result=int(num1)-int(num2)
    print(result)
elif operation in '3':
    result=int(num1)*int(num2)
    print(result)
elif operation in '4':
    result=int(num1)/int(num2)
    print(result)
 

