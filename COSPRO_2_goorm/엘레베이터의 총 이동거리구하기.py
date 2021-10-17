def solution(floors):
	dist = 0
	length = len(floors)
	for i in range(1,length):
		# 여기서 계속 헤맸는데 생각해보면 엘레베이터가 0층부터 시작하지 않기 때문에
		# 1층부터 시작해야한다
		if floors[i]>floors[i-1]:
		# 배열의i보다 i-1이 더 작으면
			dist += floors[i] - floors[i-1]
			# i에서 i-1을 빼는 것 입니다
		else:
			dist += floors[i-1] - floors[i]
			# i-1이 더 크다면 i-1에서 i를 뻅니다. 왜냐하면 엘레베이터는 음수가 나올 수 없기 때문에
			# 큰 수에서 작은 수를 빼도록 한 것 입니다.
	return dist


floors = [1, 2, 5, 4, 2]
ret = solution(floors)

print("solution 함수의 반환 값은", ret, "입니다.")