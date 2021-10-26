def solution(time_table, n):
	answer = 0
	works = []
	for x in time_table:
		#테이블 x변수에 넣어서 한번 싹 돌리기
		for y in range(0,len(time_table)):
			#y는 x에 n만큼 더하기위해 필요한 변수
			if y+n<=n:
				#이부분이문제를 잘못읽음. index를 넘으면 처음으로다시 돌아가는 거였삼
				works.append(x+(time_table[y+n]))
				#그래도 일단 works에 x에 index로 n만큼 더 간 녀석을 더해줌
			else:
				works.append(x+0)
			answer = max(works)
			#그리고 max함수를 이용해서 최대로많이 일한사람을 찾음
	return answer

time_table1 = [1, 5, 1, 9]
n1 = 3
ret1 = solution(time_table1, n1)

print("solution 함수의 반환 값은", ret1, "입니다.")

time_table2 = [4, 8, 2, 5, 4, 6, 7]
n2 = 4
ret2 = solution(time_table2, n2)

print("solution 함수의 반환 값은", ret2, "입니다.")