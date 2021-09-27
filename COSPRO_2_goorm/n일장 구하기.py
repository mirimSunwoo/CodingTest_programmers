def solution(a, b):
	answer = 0
	for i in range(1, b + 1):
		if (a * i) % b == 0:
			answer = a * i
			break
	return answer

a = 4
b = 6
ret = solution(a, b)

print("solution 함수의 반환 값은", ret, "입니다.")