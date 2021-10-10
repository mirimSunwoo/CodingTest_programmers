def solution(scores, cutline):
	answer = 0
	for x in scores:
    # x변수에다가 scores 배열에 있는 값들을 하나씩 넣어줘야합니다
		if x >= cutline:
		# x변수에 있는 값이 60점 넘는다면
			answer +=1
			#cultline을 넘은 점수가 몇개인지 셉니다
	return answer
	#그리고 반환해줍니다

scores = [80, 90, 55, 60, 59]
cutline = 60
ret = solution(scores, cutline)

print("solution 함수의 반환 값은", ret, "입니다.")