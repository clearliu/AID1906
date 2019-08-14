number01 = float(input("请录入第一个数字:"))
operator = input("请录入一个运算符:")
number02 = float (input("请录入第二个数字:"))
if operator == "+":
    print(number01 + number02)
elif operator == "-":
    print(number01 - number02)
elif operator == "*":
    print(number01 * number02)
elif operator == "/":
    print(number01 / number02)
else:
    print("运算符输入有误")