#다음과 같이 import를 사용할 수 있습니다.
#import math

def solution(scores):
   #여기에 코드를 작성해주세요.
   answer = 0
   #최댓값과 최소값을 뺀 다른 수들을 모두 더한다
   #전체 갯수-2 만큼 나눈다(나머지 제거)
   return (sum(scores) - max(scores) - min(scores)) // (len(scores) - 2)

#아래는 테스트케이스 출력을 해보기 위한 코드입니다.
scores1 = [35, 28, 98, 34, 20, 50, 85, 74, 71, 7]
ret1 = solution(scores1)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret1, "입니다.")

scores2 = [1, 1, 1, 1, 1]
ret2 = solution(scores2)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret2, "입니다.")