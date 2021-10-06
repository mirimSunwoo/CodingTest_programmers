def solution(votes, N, K):
	counter = [0 for _ in range(N + 1)]
	for x in votes:
		counter[x] += 1
	answer = 0
	# answer = -1
	# 0으로 초기화 해야 K와 같을때 1씩 누적합을 할 수 있다.
	for c in counter:
		if c == K:
			answer += 1
	return answer

votes = [2, 5, 3, 4, 1, 5, 1, 5, 5, 3]
N = 5
K = 2
ret = solution(votes, N, K)

print("solution 함수의 반환 값은", ret, "입니다.")