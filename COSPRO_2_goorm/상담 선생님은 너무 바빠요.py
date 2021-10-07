def solution(schedule):
	answer = []
	for idx, i in enumerate(schedule):#enumerate몇번째 반복문인지 알려줌
		if i == 'X':
            #선생님께서 자리에 없다는 'X'표시일때
			answer.append(idx+1)
            #answer배열에 idx + 1(왜냐하면 0부터 시작해서 결과가 다르게 나온다)
	return answer

schedule = ["O", "X", "X", "O", "O", "O", "X", "O", "X", "X"]
ret = solution(schedule)

print("solution 함수의 반환 값은", ret, "입니다.")