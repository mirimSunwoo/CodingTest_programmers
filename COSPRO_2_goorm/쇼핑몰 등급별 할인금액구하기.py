def solution(price, grade):
	answer = 0
	if(grade == 'S'):
		answer = int(price - price * 0.05)
	elif(grade == 'G'):
		answer = int(price - price * 0.1)
	elif(grade == 'V'):
		answer = int(price - price * 0.15)
	return answer


price1 = 2500
grade1 = "V"
ret1 = solution(price1, grade1)

print("solution 함수의 반환 값은", ret1, "입니다.")

price2 = 96900
grade2 = "S"
ret2 = solution(price2, grade2)

print("solution 함수의 반환 값은", ret2, "입니다.")