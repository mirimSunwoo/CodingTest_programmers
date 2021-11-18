def solution(number):
	count = 0
	while number > 0:
		# 정답은 while number>=0 에서 >=를 >로 바꿔줘야했습니다
		# 흠 왜인지 생각해봤는데요
		# while문이 0일때도 반복하면 무한 루프에 걸리기 때문이 아닐까 생각했습니다
		# 마지막 수는 10으로 나머지 없이 나눠서 0이 될수밖에 없기 때문에 무한루프에 빠질 수있습니다.
		# 그렇기 때문에 0을 포함하지 않을때 while문을 돌려줘야합니다

		n = number % 10
		if n == 2 or n == 3 or n == 5 or n == 7:
			count += 1
		number //= 10
	return count

number = 29022531
ret = solution(number)

print("solution 함수의 반환 값은", ret, "입니다.")