def solution(korean, english):
	answer = 0
	math = 210 - (korean + english)
    #이 문제에서 틀린점은 ()가 빠졌다는 것이다
    #다른문제에서도 종종 보이는 것이라 기억해두는것이 좋을 것 같다
    #math를 구하는 이유가 평균 70점이 나오기 위해 70*3 = 210에서 영어와 국어를 더한점수를 빼는것인데
    #()가 없다면 210에서 70을 뺀 140에다가 60을 더하게 되어 200이 되는 이상현상이 발생한다
    #그렇기 때문에 ()를 꼭 써야한다
	if math > 100: #math가 100점이 넘는다면 -1을 반환
		answer = -1
	else:
		answer = math
	return answer

korean = 70
english = 60
ret = solution(korean, english)

print("solution 함수의 반환 값은", ret, "입니다.")