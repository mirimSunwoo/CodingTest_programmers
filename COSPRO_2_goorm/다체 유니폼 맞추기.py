def solution(people):
	answer = [0 for _ in range(4)]
	for size in people:
		if size<95:
			answer[0] += 1
			#이상은 자기 자신을 포함, 이하는 내 아래의 숫자를 의미
		elif size>=95 and size<100:
			answer[1] += 1
		elif size>=100 and size<105:
			answer[2] += 1
		elif size>=105:
			answer[3] += 1
	return answer

people = [97, 102, 93, 100, 107]
ret = solution(people)

print("solution 함수의 반환 값은", ret, "입니다.")