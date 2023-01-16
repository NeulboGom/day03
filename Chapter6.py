#Chapter6 예제

#prime number

'''number=int(input("Type a number:"))
counts=0

k=1
while k<=number:
    if number%k==0:
        counts+=1
    k+=1
if counts==2:
    print(f"{number} is a prime number.")
else:
    print(f"{number} is not a prime number")
    '''

# prime number determination by using 'for' statement
number=int(input("Type a number:"))
counts=0
for i in range(1,number+1):
    if number%i==0:
        counts+=1
    break

if counts==2:
    print(f"{number} is a prime number.")
else:
    print(f"{number} is not a prime number")