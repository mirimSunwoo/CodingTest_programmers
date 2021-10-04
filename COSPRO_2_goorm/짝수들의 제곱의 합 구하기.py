def solution(N, M):
	answer = 0
	count = 0
	# N부터 M까지 for문을 돌려준다.(4,5,6,7)
	for x in range(N,M+1):
		# 4부터 돌아가면서 짝수일때 if문에 걸린다
		if x%2 == 0:
			# answer에 짝수의 제곱을 누적합 해준다
			# answer = x*x이렇게 하면 최종적으로 6이짝수로 남아서 4는 더해지지 못한다
			answer += x*x
	return answer

N = 4
M = 7
ret = solution(N, M)

print("solution 함수의 반환 값은", ret, "입니다.")