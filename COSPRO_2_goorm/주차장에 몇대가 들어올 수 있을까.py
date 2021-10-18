def solution(day, numbers):
	count = 0
	for number in numbers:
		if number%2 == day%2:
		#if 자동차판의 수가 2로 나누고 나머지수와 일수가 2로 나눠지고 그 나머지 수가 같다면 count가 1증가시킵니다
		#원래 number%2 != day%2이렇게 되어있었는데 이렇게 되면 값이 4가 나오게 됩니다
		#왜냐하면 두개의 나머지 값이 다르다면 원래 구하려고 했던 조건과 다르기 때문입니다
		#홀수날이면 나머지수가 1로 같고, 짝수 날이면 나머지 수가 2로 같은 자동차가 들어올 수 있게됩니다
			count += 1
	return count

day = 17
numbers = [3285, 1724, 4438, 2988, 3131, 2998]
ret = solution(day, numbers)

print("solution 함수의 반환 값은", ret, "입니다.")