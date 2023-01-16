#Chapter 5: Text string

#5.12 문자열 스트립: strip() // 양 사이드에 달려있는 것만 특정해서 지우기
subjects="  python, data structure, database    "
print(subjects)
print(subjects.strip())
subjects2=" $ python, data structure, database    $$$$$"
print(subjects2.strip("$")) #공란이 앞에 있기 때문에 $ 표시가 안 지워짐
#나중에 뭔가를 다운받았을 때, 쓰잘떼기 없는 것들을 지울 때 쓰임

blurt="What the ...!!?"
print(blurt.strip(".?!"))

#5.13 검색과 선택
print(subjects.find("data"), subjects.index("data"))
# 못 찾았을 때
#print(subjects.find("inha"))
#print(subjects.index("inha"))
print(subjects[10:15])
print(subjects.count("data"))

#5.14 대소문자
print(subjects.title())

#5.15 정렬
print(subjects.center(60))
print(subjects.ljust(50))
print(subjects.rjust(80))


#5.16 formating
# "%": Old style
