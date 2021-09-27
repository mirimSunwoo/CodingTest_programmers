# 0의 개수가 아닌 수업을 중심으로 남는 공강시간을 구함
def func_a(time_table):
	answer = 0
	for i, t in reversed(list(enumerate(time_table))):
		if t == 1:
			answer = i
			break
	return answer

def func_b(time_table, class1, class2):
	answer = 0
	for i in range(class1, class2):
		if time_table[i] == 0:
			answer += 1
	return answer

def func_c(time_table):
	answer = 0
	for i, t in enumerate(time_table):
		if t == 1:
			answer = i
			break
	return answer

def solution(time_table):
	answer = 0
	first_class = func_c(time_table)
	last_class = func_a(time_table) #enumerate한 값을 reversed한거임
	answer = func_b(time_table,first_class,last_class)
	return answer

time_table = [1, 1, 0, 0, 1, 0, 1, 0, 0, 0]
ret = solution(time_table)

print("solution 함수의 반환 값은", ret, "입니다.")