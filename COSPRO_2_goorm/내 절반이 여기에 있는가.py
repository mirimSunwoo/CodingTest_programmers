def solution(arr):
	answer = 0
	for i in arr:
		if i/2 in arr:
        #여기가 if가 아닌 for문으로 되어있었는데
        #for문으로 되어있으면 cannot assign to operator에러가 발생한다
		#이 에러는 구문오류로 arr배열에서 i/2에 넣을 수 없다고 말하는 것 같습니다
			answer += 1
	return answer

arr = [4, 8, 3, 6, 7]
ret = solution(arr)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret, "입니다.")