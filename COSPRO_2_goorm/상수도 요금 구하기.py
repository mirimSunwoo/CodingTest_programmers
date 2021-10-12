def solution(usage):
	answer = 0
	if usage > 30:
		answer = 20 * 430 + 10 * 570 + (usage - 30) * 840
        #총 35톤을 사용하고 여기서는 31톤 이상을 사용한 값을 내면됩니다
        #그렇기때문에 30전은 빼주기 위해 usage에서 30을 빼주는것이 맞습니다
        #그렇게 뺀값에 20을 초과하여더해주고(2단계) 10을 초과해서 더해주고(1단계) 마지막으로 3단계를 더해주게 되면 상수도 요금을 구할 수 있습니다
	elif usage > 20:
		answer = 20 * 430 + (usage - 20) * 570
	else:
		answer = usage * 430
	return answer

usage = 35
ret = solution(usage)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret, "입니다.")