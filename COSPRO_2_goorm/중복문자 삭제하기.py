def solution(characters):
	result = ""
	# result += characters[0]
	# 이줄을 빼는게 정답이었는데 이 줄을 넣으면 첫글자를 또 넣게 되어서 틀린답이 나오기 때문이다.
	for i in range(len(characters)):
		if characters[i - 1] != characters[i]:
			result += characters[i]
	return result

characters = "senteeeencccccceeee"
ret = solution(characters)

print("solution 함수의 반환 값은", ret, "입니다.")