#1~number까지 몇번박수를 쳐야하는지 반환
def solution(number):
   count = 0
   for i in range(1, number + 1):  # for(int i=1; i<number+1)
       current = i
       temp = count
       while current != 0:
           if current%10==3 or current%10==6 or current%10==9:
               count += 1
               print("pair", end = '') # 디버깅을 위한 출력(없어도 무관)
           current = current // 10
   return count

#The following is code to output testcase.
number = 40
ret = solution(number)
print(ret)

# for num in range(1,a+1):
#     while num:
#         if num % 10 == 3 or num % 10 == 6 or num % 10 == 9:
#             카운터 += 1
#         num = num//10
#
# print(카운터*'짝')