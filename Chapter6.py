#Chapter6 반복문

#for statement 구구단

dan=int(input("Dan is: "))

while True:
    if dan==0:
        break
    elif 1<dan<10:
        for i in range(1,10):
            answer=dan*i
            print(f"{dan}*{i}={answer}")
        break
    else:
        print("2에서 9 사이의 숫자를 입력하세요.")
