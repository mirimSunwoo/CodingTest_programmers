# 5의 배수의 개수를 구하는 함수
def func_a(arr):
    count = 0
    for n in arr:
        if n % 5 == 0:
            count += 1
    return count

# 3과 5의 배수의 개수를 구하고 둘중 누가 더 많은지, 혹은 같은지를 판별하는 함수
def func_b(three, five):
    if three > five:
        return "three"
    elif three < five:
        return "five"
    else:
        return "same"

# 3의 배수의 개수를 구하는 함수
def func_c(arr):
    count = 0
    for n in arr:
        if n % 3 == 0:
            count += 1
    return count

def solution(arr):
    #먼저 3과 5 배수의 개수를 센다(순서는 상관없음)
	count_three = func_c(arr)
	count_five = func_a(arr)
    # 그리고 둘중 누가 count개수가 더 큰지 판별해 개수를 알려준다
	answer = func_b(count_three,count_five)
	return answer

arr = [2, 3, 6, 9, 12, 15, 10, 20, 22, 25]
ret = solution(arr)

print("solution 함수의 반환 값은", ret, "입니다.")