def solution(n, votes):
	answer = 0
	votes_len = len(votes) #총 투표수
	candidate = votes[0]
	count = 1
	for i in range (1, votes_len) : #후보의 투표수를 찾는다(이 코드는 없어도 돌아감)
		if candidate == votes[i] :
			count += 1
		else :
			count -= 1
		if count == 0 :
			candidate = votes[i]
			count = 1

	test_count = 0 #테스트 코드
	for i in range(0, votes_len) :
		if votes[i] == candidate :
			test_count += 1
			#배열의 수와 candidate가 같으므로 count에 1씩 누적합을 해주는것이 맞다

	if test_count > votes_len // 2 : #과반수를 득표한 후보자의 번호를 반환함(절반이 넘는수)
		answer = candidate
	else :
		answer = -1

	return answer

n1 = 3
votes1 = [1, 2, 1, 3, 1, 2, 1]
ret1 = solution(n1, votes1)

print("solution 함수의 반환 값은", ret1, "입니다.")

n2 = 2
votes2 = [2, 1, 2, 1, 2, 2, 1]
ret2 = solution(n2, votes2)

print("solution 함수의 반환 값은", ret2, "입니다.")