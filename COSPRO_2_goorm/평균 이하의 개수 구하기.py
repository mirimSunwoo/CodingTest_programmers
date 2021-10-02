def solution(data):
	total = sum(data)
	average = total / len(data)
    # average = len(data) / total 이줄을 바꾼이유는 나누는 대상이 틀렸기 때문이다
	cnt = 0
	for d in data:
		if d < average:
        # if d > average : 이 줄을 바꾼이유는 평균보다 큰 수를 구하려고 했기 때문이다
			cnt += 1
            # cnt = 1 평균보다 작은 수'들'을 구해야하기 때문에 평균보다 작다면 1씩 더해줘야하기 때문에 바꿨다.
	return cnt

data1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
ret1 = solution(data1)

print("solution 함수의 반환 값은", ret1, "입니다.")

data2 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 10]
ret2 = solution(data2)

print("solution 함수의 반환 값은", ret2, "입니다.")