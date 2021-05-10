def 보조함수_a(arr):
   counter = [0]*1001
   for x in arr:
       counter[x] += 1
   return counter

def 보조함수_b(arr):
   ret = 0
   for x in arr:
       if ret < x:
           ret = x
   return ret

def 보조함수_c(arr):
   INF = 1001
   ret = INF
   for x in arr:
       if x != 0 and ret > x:#0을 포함하지 않는것
           ret = x
   return ret

def solution(arr):
    #1단계. 리스트에 들어있는 각 자연수의 개수를 셉니다.
   counter = 보조함수_a(arr)
    #2단계.가장 많이 등장하는 수의 개수를 구합니다.
   max_cnt = 보조함수_b(counter)
    #3단계.가장 적게 등장하는 수의 개수를 구합니다.
   min_cnt = 보조함수_c(counter)
    #4단계.가장 많이 등장하는 수가 가장 적게 등장하는 수보다 몇배 더 많은지 구합니다.
   return max_cnt // min_cnt

#The following is code to output testcase.
arr = [1, 2, 3, 3, 1, 3, 3, 2, 3, 2]
ret = solution(arr)

#Press Run button to receive output.
print("Solution: return value of the function is", ret, ".")