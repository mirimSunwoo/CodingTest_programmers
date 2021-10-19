def solution(money, price, n):
	answer = 0
	empty_bottle = answer = money // price
	#남은병과 답 변수에는 남은 돌은 돈으로 마실 수 있는 병의 수를 넣었습니다(//연산자를 이용해 나머지가 없음)
	while n <= empty_bottle:
		#교환할 수 있을땐(음료수로 교환할 수 있는 수보다 남은 병이 더 많을때)
		empty_bottle = empty_bottle - n
		#남아있는 병에서 n을 빼줍니다
		answer += 1
		#그리고 마실 수 있으므로 1더해줍니다
		empty_bottle += 1
		#그리고 먹었으니빈병에 1을 더해줍니다
	return answer

money1 = 8
price1 = 2
n1 = 4
ret1 = solution(money1, price1, n1)

print("solution 함수의 반환 값은", ret1, "입니다.")

money2 = 6
price2 = 2
n2 = 2
ret2 = solution(money2, price2, n2)

print("solution 함수의 반환 값은", ret2, "입니다.")