def solution(classes, m):
	answer = 0
	for students in classes:
		answer += students / m
		# 학생의수를 조교가 맡을 수 있는 최대의 주30으로 나눠줍니다
		if students >= m != 0:
			# 만약 학생들이 30명보다 더 넘을때
			answer += 1
			#조교의 수를 한명 더 늘려줍니다
	return int(answer)

classes = [80, 45, 33, 20]
m = 30
ret = solution(classes, m)

print("solution 함수의 반환 값은", ret, "입니다.")