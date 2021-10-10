def solution(speed, cars):
	answer = 0
	for x in cars:
		if x >= speed * 11/10 and x < speed * 12/10:
			answer += 3
		elif x >= speed * 1.2 and x < speed * 1.3:
        #위에 있는 if를 참고해서 21/10(20km)을 넣어주었고, 31/10(30km)을 넣어주었다.
			answer += 5
		elif x >= speed * 1.3:
        # 위에서와 같이 31/10보다 높은 것 30km 이상인것을 선별하는 if문 입니다
			answer += 7
	return answer

speed = 100
cars = [110, 98, 125, 148, 120, 112, 89]
ret = solution(speed, cars)

print("solution 함수의 반환 값은", ret, "입니다.")