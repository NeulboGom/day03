#Chapter6 예제 두 수 사이의 소수를 전부 나열하는 코드

num1=int(input("number1:"))
num2=int(input("number2:"))

if num1>num2:
    num1,num2=num2,num1

for i in range(num1,num2+1):
    if i<=1:
        continue
    elif i>1:
        for k in range(2,i):
            if i%k==0:
                break
        else:
            print(i,end=' ')