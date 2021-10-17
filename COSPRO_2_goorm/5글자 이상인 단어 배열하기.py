def solution(words):
	answer = ''
	for x in words:
		if(len(x)>=5):
			answer += x
    #여기서 if문을 앞으로 땡겨줘야 반복을 벗어날 수 있다
	if(len(answer)<1):
    #앞에서 구한 answer이 1이하 즉 5개인 글자가 하나도 없을때 'empty'를 출력한다
		answer = 'empty'
	return answer

words1 = ["my", "favorite", "color", "is", "violet"]
ret1 = solution(words1);

print("solution 함수의 반환 값은", ret1, "입니다.")

words2 = ["yes", "i", "am"]
ret2 = solution(words2);

print("solution 함수의 반환 값은", ret2, "입니다.")