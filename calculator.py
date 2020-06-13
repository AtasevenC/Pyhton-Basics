# Basic Calculator
print("Please enter the first number:")
Num1=int(input())
print("Please choose the operator: +,-,*,:")
op= str(input())
print("Please enter the second number:")
Num2=int(input())



if op=="+":
  print("Result: "+ str(Num1+Num2))
elif op=="-":
  print("Result: "+ str(Num1-Num2))
elif op=="*":
  print("Result: "+ str(Num1*Num2))
elif op== ":":
  print("Result: "+ str(Num1/Num2))





