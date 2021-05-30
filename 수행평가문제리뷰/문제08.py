#연속으로 중복되는 문자는 제외
def solution(characters):
   result = ""
   result += characters[0]
   for i in range(1,len(characters)):
       if characters[i - 1] != characters[i]:
           result += characters[i+1]
   return result

#The following is code to output test case. The code below is correct and you shall correct solution function.
characters = "senteeeencccccceeee"
ret = solution(characters)

#Press Run button to receive output.
print("Solution: return value of the function is", ret, ".")
#
#
# arr = "abcdefg"
# # print(arr[len(arr)]) : 에러
# print(arr[3])
# print(arr[6])
# print(arr[0])
# print(arr[-1])

