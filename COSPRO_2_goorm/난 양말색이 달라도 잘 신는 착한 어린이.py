def solution(socks):
	answer = 0
	count = [0 for _ in range(10)]
	for s in socks:
		count[s] += 1
	for c in count:
		answer += (c // 2)
		#answer = (c//2)라고 쓰면 마지막 count값을 2로 나눈값이 저장된다
		#그리고 처음 코드가 (c%2)라고 되어있었는데 이것도 안되는것같다
		#왜냐하면 5라고 치자, 이러면 %는 1이 나온다(나머지 값을 구하기 때문)
		#하지만 이 문제는 양말의 짝을 구하는 것이기 떄문에 //을 써주는것과 누적합을 해줘야한다
	return answer

socks = [1, 2, 1, 3, 2, 1]
ret = solution(socks)

print("solution 함수의 반환 값은", ret, "입니다.")