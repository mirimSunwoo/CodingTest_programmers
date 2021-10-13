def solution(temperature, A, B):
	answer = 0
	for i in range(A+1,B):
		#처음에 실행해 보고 오류가 안나서 당황했다
		#문제를 다시 읽어보니 이 부분이 틀렸다는 걸 알수 있었다
		#"A번쨰 일과 B번째 일 사이에서" 이부분 때문에 이렇게 바꿔주어야한다
		#원래 문장은 range(0, len(temperature) 이거였는데, 꽤 그럴싸 했다
		#하지만 나중에 자료가 더 많아지게 되면 모든 수 사이에서 A,B보다 큰수를 구하게 되니 결과값이 달라질 수 있다
		if temperature[i] > temperature[A] and temperature[i] > temperature[B]:
			answer += 1
	return answer

temperature = [3, 2, 1, 5, 4, 3, 3, 2]
A = 1
B = 6
ret = solution(temperature, A, B)

print("solution 함수의 반환 값은", ret, "입니다.")