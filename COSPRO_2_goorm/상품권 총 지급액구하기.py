def solution(purchase):
	total = 0
	for p in purchase:
		if p >= 1000000:
			total += 50000
		elif p >= 600000:
			total += 30000
		elif p >= 400000:
			total += 20000
		elif p >= 200000:
		#else : 라고 되어있으면 안된다.
		#왜냐하면 20만원 이상을 안사도, 만원이 지급되면 치명적인 오류가 발생한다
			total += 10000
	return total

purchase = [150000, 210000, 399990, 990000, 1000000]
ret = solution(purchase)

print("solution 함수의 반환 값은", ret, "입니다.")