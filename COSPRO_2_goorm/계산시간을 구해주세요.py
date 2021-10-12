def solution(stuffs):
	answer = 0
	small_counter, general_counter = 0, 0
	for s in stuffs:
		if s > 3:
			general_counter += s
		else:
			small_counter += s
	if small_counter > general_counter:
    #일반계산대와 소량 계산대의 시간중 큰 시간을 넣어햐하기 때문에
    #samll_counter가 general_counter보다 크다면 small_counter를 반환해주는것이 맞습니다
		answer = small_counter
	else:
		answer = general_counter
	return answer

stuffs = [5, 3, 4, 2, 3, 2]
ret = solution(stuffs)

print("solution 함수의 반환 값은", ret, "입니다.")