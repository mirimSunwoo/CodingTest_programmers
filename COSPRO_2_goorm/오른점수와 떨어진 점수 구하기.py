def func_a(scores1, scores2):
    answer = 0
    for score1, score2 in zip(scores1, scores2):
        answer = max(answer, score2 - score1)
    return answer


def func_b(scores1, scores2):
    answer = 0
    for score1, score2 in zip(scores1, scores2):
        answer = min(answer, score1 - score2)
    return answer

def solution(mid_scores, final_scores):
	up = func_a(mid_scores, final_scores)
	down = func_b(final_scores, mid_scores)
    #최솟값을 구하기 위해서는 기말고사 점수에서 중간고사 점수를 빼야하는데
    #교묘하게 func_b에서는 score1-score2를 빼고있습니다
    #그렇기 때문에 두개의 인수의 자리를 바꿔주는 것이 맞습니다.
	answer = [up, down]
	return answer
mid_scores = [20, 50, 40]
final_scores = [10, 50, 70]
ret = solution(mid_scores, final_scores)

print("solution 함수의 반환 값은", ret, "입니다.")