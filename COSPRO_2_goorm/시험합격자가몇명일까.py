def func_a(passed, non_passed):
	return ( passed > 1 and non_passed ==0 )

def func_b(scores):
	answer = 0
	if scores[0] < 40:
		answer += 1
	if scores[1] < 44:
		answer += 1
	if scores[2] < 35:
		answer += 1
	return answer

def func_c(scores):
	answer = 0
	if scores[0] >= 80:
		answer += 1
	if scores[1] >= 88:
		answer += 1
	if scores[2] >= 70:
		answer += 1
	return answer

def solution(scores):
	answer = 0
	for my_score in scores:
		passed = func_c(my_score) #제가 여기서 실수해서 계속 오류났던것이 for문 변수는 my_score인데 계속 못보고 scores로 만 쓰니까 오류가 났습니다..앞으로 변수명잘보기 메모...
        # 먼저 통과학 종목이 몇개인지 셉니다
		non_passed = func_b(my_score)
        # 통과 점수의 반을 넘기지 못한 종목이 몇개인지 셉니다
		answer += func_a(passed, non_passed)
        #통과한 종목이 하나보다 많고 통과 점수의 반을 넘기지 못한 종목이 없으면 통과 인원으로 셉니다
	return answer

scores1 = [[30, 40, 100], [97, 88, 95]]
ret1 = solution(scores1)

print("solution 함수의 반환 값은", ret1, "입니다.")

scores2 = [[90, 88, 70], [85, 90, 90], [100, 100, 70], [30, 90, 80], [40, 10, 20], [83, 88, 80]]
ret2 = solution(scores2)

print("solution 함수의 반환 값은", ret2, "입니다.")