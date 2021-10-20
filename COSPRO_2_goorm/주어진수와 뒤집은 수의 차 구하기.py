# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
#구한 자릿수를 이용하여 주어진 수를 거꾸로 뒤집는 함수
def func_a(number1, number2):
	ret = 0
	if number1 > number2: #둘중 누가 큰지 구해서 큰값에서 작은 값을 뺀 값을 return 합니다
		ret = number1 - number2
	else:
		ret = number2 - number1
	return ret

#주어진 수의 자릿수를 구하는 함수
def func_b(number):
	ret = 0
	while number != 0:
		number = number // 10
		ret += 1
	return ret

#주어진 수의 자릿수를 구하는 함수
def func_c(number, digit):
	ret = 0
	for i in range(digit):
		#digit는 func_b에서 만든 자릿수입니다
		temp = number % 10 #자릿수(10으로 나눈 나머지)를 temp에 담고
		number = number // 10 #number은 10으로 나눠서
		ret = ret * 10 + temp #그것을 ret에 반대로 차례대로 담아줬습니다
	return ret


def solution(number):
	answer = 0
	digit = func_b(number)
	convert_number = func_c(number, digit)
	answer = func_a(number, convert_number)
	return answer

number1 = 120
ret1 = solution(number1)

print("solution 함수의 반환 값은", ret1, "입니다.")

number2 = 23
ret2 = solution(number2)
