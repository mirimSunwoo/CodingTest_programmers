#4일장과 6일장이 동시에 만나는 날은 언제인가?(공배수 구하기)
def solution(a,b):
    answer = 0
    for i in range(1,b+1):
        if(a * i) % b == 0:
            answer = b * i
            break
    return answer

#테스트케이스
a = 4
b = 6
ret = solution(a,b)

print("solution 함수의 반환값은",ret,"입니다.")