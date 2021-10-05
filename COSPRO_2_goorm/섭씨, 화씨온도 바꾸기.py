def solution(value, unit):
	converted = 0
	if unit == "C":
		value = value * 1.8 + 32
	if unit == "F":
		value = (value - 32) / 1.8
        # ()이 없었기 때문에 오류가 났고, ()를 넣어주면 32를 먼저 빼고 1.8를 나루어 정확한 값이 나올 수 있었다
	converted = int(value)
	return converted


value = 527
unit = "C"
ret = solution(value, unit)

print("solution 함수의 반환 값은", ret, "입니다.")

value = 980
unit = "F"
ret = solution(value, unit)

print("solution 함수의 반환 값은", ret, "입니다.")