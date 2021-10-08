def solution(point):
	if point < 1000:
		return 0
	return (point // 100) * 100
    # return point *100 //100 이렇게 되면 소수에서 100을 더해 100으로 나누기 때문에 2323의 값이 나오게 됩니다
    # 100의 자리 숫자까지 빼버리고 싶다면 100으로 먼저 나누어서 그 값을 100으로 곱하는 것이 맞습니다.
    # ()가 없어도 실행이 되지만 가독성으 위해 넣어주었습니다

point = 2323
ret = solution(point)

print("solution 함수의 반환 값은", ret, "입니다.")