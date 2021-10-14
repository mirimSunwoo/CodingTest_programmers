def solution(arr):
	left, right = 0, len(arr)-1
	#예시 대로라면 arr의 길이 4에서 1을 뺀 3이 right가 된다
	#1을 뺀 이유는 index가 0부터 시작하기 때문이라고 생각한다
	while left<right:
		arr[left], arr[right] = arr[right], arr[left]
		left += 1
		right -= 1
		#index 0과 3을 바꾼다(left =1, right=2)
		#index 1과 2를 바꾼다(lift =2 rihgt =2)
		#left와 rihgt가 같아졌기 때문에 while문에서 빠져나온다
	return arr

arr = [1, 4, 2, 3]
ret = solution(arr)

print("solution 함수의 반환 값은", ret, "입니다.")