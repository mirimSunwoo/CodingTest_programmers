def solution(floors):
	dist = 0
	length = len(floors)
	for i in range(1,length):
		if floors[i]>floors[i-1]:
			dist += floors[i] - floors[i-1]
		else:
			dist += floors[i-1] - floors[i]
	return dist


floors = [1, 2, 5, 4, 2]
ret = solution(floors)

print("solution 함수의 반환 값은", ret, "입니다.")