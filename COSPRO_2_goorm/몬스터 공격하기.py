def solution(attack, recovery, hp):
	count = 0
	while(True):
		count += 1
        # 공격을 당할때마다 횟수가 올라가서
        # hp가 0이 되었을때 몇번 공격당해야 죽는지 보여준다
		hp -= 30
        # 한번 공격 당했을때 hp는 30씩 감소된다
		if hp <= 0:
			return count
            # hp가 0보다 작을때 횟수를 반환한다
		hp += 10
        # 공격한번 힐링한번 해야하기 때문에 hp를 10씩 더해준다
	return count

attack = 30
recovery = 10
hp = 60
ret = solution(attack, recovery, hp)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret, "입니다.")