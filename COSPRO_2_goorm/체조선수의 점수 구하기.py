def solution(scores):
    answer = 0

    # return (sum(scores)-max(scores)-min(scores))//(len(scores)-2) 이런 방법(정보를 안바꿀 수 있음)
    # 	최대값과 최소값을 뺸다
    scores.remove(max(scores))
    scores.remove(min(scores))
    #   나머지 값의 평균을 구한다
    # answer = int(sum(scores)/len(scores))
    answer = int(sum(scores) // len(scores))

    # score = sorted(scores)
    # for x in range (score[1],score[-1]):
    # 	add += x
    # 	# count += 1
    # answer = add/count
    return answer

scores1 = [35, 28, 98, 34, 20, 50, 85, 74, 71, 7]
ret1 = solution(scores1)

print("solution 함수의 반환 값은", ret1, "입니다.")

scores2 = [1, 1, 1, 1, 1]
ret2 = solution(scores2)

print("solution 함수의 반환 값은", ret2, "입니다.")