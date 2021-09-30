def solution(shirt_size):
	answer = [0,0,0,0,0,0]
	# while문으로 돌려야 빠지는 수 없이 돌아가는줄 알았는데
	# 배열 순차적으로 for문으로 돌리면 된다는걸 알았다
	# 이것보다 좋은 방법이 있을텐데 좀 더 연구해봐야겠다
	# while len(shirt_size):
	for x in shirt_size:
		if(x == 'XS'):
			answer[0] += 1
		elif(x == 'S'):
			answer[1] += 1
		elif(x == 'M'):
			answer[2] += 1
		elif(x == 'L'):
			answer[3] += 1
		elif(x == 'XL'):
			answer[4] += 1
		elif(x == 'XXL'):
			answer[5] += 1
	return answer

shirt_size = ["XS", "S", "L", "L", "XL", "S"]
ret = solution(shirt_size);

print("solution 함수의 반환 값은", ret, "입니다.")

