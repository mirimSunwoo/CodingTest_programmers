# for x in range(0,3): #0,1,2
#     print(x)
#
# for x in range(3) : #0,1,2
#     print(x)

def solution(arr):
   left, right = 0, len(arr)-1
   while len(arr):
       arr[left], arr[right] = arr[right], arr[left]
       left += 1
       right -= 1
   return arr

#The following is code to output testcase.
#arr =  [-1,-2,-3,-4,-5] # input arr
#ret = solution(arr)

arr = [2,3,7,1]
#최솟값 구하기
현재_최솟값 = arr[0]
for x in arr:
    if x < 현재_최솟값: #key_point
        현재_최솟값 = x
print(현재_최솟값)

#최댓값 구하기
현재_최댓값 = arr[0]
for x in arr:
    if x > 현재_최댓값: #key_point
        현재_최댓값 = x
print(현재_최댓값)

#역순구하기
print(list(reversed(arr)))#간단한 방법
#알고리즘
reversed_arr = [0] * len(arr)
length = len(arr)

for i in range(length):
    reversed_arr[length-(i+1)] = arr[i]
print(reversed_arr)

#역순[맥스-1] = arr[0]
#역순[맥스-2] = arr[1]
#       ...