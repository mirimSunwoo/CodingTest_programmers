#현재 상황보고
#일단 time_table에서 교대 근무 방식은 짬
#하지만 if문에 넣거나 list에 넣으려고 할 때 오류남
#x+n을 하는과정에서 Array를 벗어나서 오류가 남

def solution(time_table, n):
	answer = []
	for x in range(len(time_table)):
		# answer.append( + time_table[x])
		# # if(n>=len(time_table)):
			# answer += time_table[x]+time_table[x+n]
			return time_table[x]+time_table[x+n]
	return answer

time_table1 = [1, 5, 1, 9]
n1 = 3
ret1 = solution(time_table1, n1)

print("solution 함수의 반환 값은", ret1, "입니다.")

time_table2 = [4, 8, 2, 5, 4, 6, 7]
n2 = 4
ret2 = solution(time_table2, n2)

print("solution 함수의 반환 값은", ret2, "입니다.")