
def solution(taekwondo, running, shooting):
	answer = 0
	if taekwondo >= 25:
		answer += 250
		# 25경기 이상 승리하면 250점을 추가해준다
	else:
		answer += taekwondo * 8
		#그 외에는 경기당 승리하면 8점의 점수가 주어진다
	answer += 250 + (60 - running) * 5
	# 500m달리기는 60초 완주시 250, 그보다 빠르면 1초당 5점 느리면 -5씩 차감된다
	count = 0
	for s in shooting:
		answer += s
		if s == 10:
			count += 1
	if count >= 7:
		answer += 100
		#사격역시 7번 이상 10점에 맞추면 추가 점수 100점이 주어진다
	return answer

taekwondo = 27
running = 63
shooting = [9, 10, 8, 10, 10, 10, 7, 10, 10, 10]
ret = solution(taekwondo, running, shooting)

print("solution 함수의 반환 값은", ret, "입니다.")