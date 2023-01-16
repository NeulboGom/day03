#Chapter 5: Text string

#5.5 복제하기
start="Na "*4+"\n"
middle="Hey "*3+"\n"
end="Goodbye."
print(start+start+middle+end)

#5.7 슬라이스로 부분 문자열 추출
univ="Inha University"
print(univ[5:])
print(univ[5:15])
print(univ[-10:])
print(univ[:14])
print(univ[0:14:3])
print(univ[::3])
print(univ[5:-6])
print(univ[-10:-6])

#5.8 문자열의 길이: len()
print(len(univ))

#5.9 문자열 나누기: split()
tasks="get gloves, get mask, give cat vitamins, call ambuland"
delimiter=","
print(tasks.split(delimiter))
delimiter_2="i"
print(univ.split(delimiter_2))


#5.10 문자열 결합하기: join()
poke_mons=["피카츄", "꼬북이", "파이리", "이상해씨"]
dele_poke=", "
poke_mons_string=dele_poke.join(poke_mons)
print(poke_mons_string)


#5.11 문자열 대체하기: replaced()
setup="a duck goses into a bar..."
setup.replace("duck", "marmoset")
print(id(setup))
print(id(setup.replace("duck", "marmoset")))
print(setup)
inha="a duck goes into a sea"
print(inha.replace('a','a nice'))
print(inha.replace('a ', 'a nice '))