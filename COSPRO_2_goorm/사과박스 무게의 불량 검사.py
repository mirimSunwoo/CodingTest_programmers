def solution(weight, boxes):
	answer = 0
	for x in boxes:
		#boxes배열에서 x에 하나씩넣어준다
		if weight*0.9<= x and x>= weight+(weight-weight*0.9) :
		#만약 weight의 무게 오차가 10% 이상이거나 이하일때
			answer += 1
			#answer의 값을 하나씩 늘려줍니다
	return answer
	#결국 2개의 불량 박스가 나와서 사장님이 슬퍼하셨어요

weight = 600
boxes = [653, 670, 533, 540, 660]
ret = solution(weight, boxes)

print("solution 함수의 반환 값은", ret, "입니다.")