def solution(scores):
	count = 0
	for s in scores:
		if 650 <= s < 800:
	    # if 650 <= s or s <800:
		# 한줄을 바꾸는 테스트였는데 위에처럼 쓰면 안되는 이유는
		# 650 이상 모든것, 800이하 모든것을 해서 모든것을 취하게 된다
		# 그렇기 때문에 or를 빼줘야한다
			count += 1
	return count

scores = [650, 722, 914, 558, 714, 803, 650, 679, 669, 800]
ret = solution(scores)

print("solution 함수의 반환 값은", ret, "입니다.")
