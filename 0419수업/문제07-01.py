#팰린드롬 간단하게 만들어보기
# [0]과 [4]를 비교
# [1]과 [3]를 비교
#둘 다 참이어여만 하죠
#[2]는 비교X

a = "neven"
#모든 조건을 만족해야만이 펠린드롬니다.
if (a[0] == a[4]) and (a[1]==a[3]):
    print("펠린드롬이다")
else:
    print("펠린드롬이 아니다")

for i in range(2):
    if a[i] !=  a[4-i]:
        print("펠린드롬이 아니다")
print("펠린드롬이다")

b = "enevene"
#하나다로 만족하지못하면 펠린드롬이 아니다.(7글자인경우)
if b[0] != b[6]:
    print("펠린드롬이 아니다")
elif b[1] != b[5]:
    print("펠린드롬이 아니다")
elif b[2] != b[4]:
    print("펠린드롬이 아니다")
else:
    print("펠린드롬이 아니다")

for i in range(3):
    if a[i] !=  a[(len(a)-1)-i]:
        print("펠린드롬이 아니다")
print("펠린드롬이다")
