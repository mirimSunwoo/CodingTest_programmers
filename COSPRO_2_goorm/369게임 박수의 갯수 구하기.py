def solution(number):
	count = 0
	for i in range(1, number + 1):
		current = i
		while current != 0:
			if current %10 == 3 or current %10 == 6 or current %10 == 9:
            #정말 한참을 고민한 문제...왜 이게 생각이 안났을꼬...
            #만약 current(number를 1부터 40까지 돌린수)가 10으로 나눴을때 3또는 6또는 9가 되는 수를 찾는 것입니다
            #그렇담 3을 10으로 나눌때 나머지 3, 13을 10으로 나눌때 10의자리 나머지1 일의자리 나머지3, 36을 나눌때는 10의 나머지 3, 일의자리 나머지 6이다

				count += 1
			current = current // 10
            #current를 10으로 나눴을때 몫
	return count

number = 40
ret = solution(number)

print("solution 함수의 반환 값은", ret, "입니다.")