def solution(papers, K):
	length = len(papers)
	for i, paper in enumerate(papers):
		K -= paper
		if K <= 0:
			# length = i-1
			return i
            #나는 정답을 length = i-1이라고 썼다.
            #왜냐하면 if문을 실행하는 과정에도 i가 증가하여 이렇게 되었을거라 생각했기 때문이다
            #내가 푼 방식이 맞는지는 모르겠지만 return i 정답이 훨씬 좋아 보이는건 사실이다
            #return i로 함수를 빠져나오게 되면 0보다 작아지는 순간 바로 반환하여 오차가 없어진다
            #이렇게 쉬운 방법을 두고 뭘 했는지 모르겠다.오늘의 수확 return을 잘 활용하자
	return length

papers1 = [2, 4, 2, 3, 1]
K1 = 10
ret1 = solution(papers1, K1)

print("solution 함수의 반환 값은", ret1, "입니다.")

papers2 = [2, 4, 2, 3, 1]
K2 = 14
ret2 = solution(papers2, K2)
