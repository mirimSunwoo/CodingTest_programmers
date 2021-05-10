# | 등급     | 할인율 |
# |----------|--------|
# | "S" | 5%     |
# | "G"   | 10%    |
# | "V"    | 15%    |


def solution(price, grade):
    reducedPrice = 0
    #elif를 써야하는 이유 : 만약 'S'면 S만 체크하는 것이 아니라 쓸데없는 코드까지 체크해야하기떄문에 효율이 떨어진다.
    if grade == 'S':
        reducedPrice =  price - price*0.05
    elif grade == 'G':
        reducedPrice = price - price*0.1
    elif grade == 'V':
        reducedPrice = price - price*0.15
    return reducedPrice

# testcase를 위한 output
price1 = 2500
grade1 = "V"
ret1 = solution(price1, grade1)

# Press Run button to receive output.
print("Solution: return value of the function is", ret1, ".")

price2 = 96900
grade2 = "S"
ret2 = solution(price2, grade2)

# Press Run button to receive output.
print("Solution: return value of the function is", ret2, ".")
