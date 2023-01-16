#Chapter6 반복문

'''dan=int(input("Dan:"))
i=1
while i<10:
    print("{0}*{1}={2}".format(dan,i,dan*i))
    i+=1
'''

while True:
    dan=int(input("Dan:"))
    if 1<dan<10:
        i=1
        while i<10:
            print("{0}*{1}={2}".format(dan,i,dan*i))
            i+=1
        break
    else:
        print("2에서 9사이의 숫자를 입력하세요")
