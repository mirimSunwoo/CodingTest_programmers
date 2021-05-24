#1부터해당하는 숫자는 박수를 총 몇번 쳐야 하는가

a = 7
카운터 = 0 #초기화를 안해주면 어떤 숫자에서 증가하는지 몰라 오류뜸
for num in range(1,a+1):
    while num:
        if num % 10 == 3 or num % 10 == 6 or num % 10 == 9:
            카운터 += 1
        num = num//10

print(카운터*'짝')