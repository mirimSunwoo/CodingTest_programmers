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
arr =  [-1,-2,-3,-4,-5] # input arr
ret = solution(arr)
