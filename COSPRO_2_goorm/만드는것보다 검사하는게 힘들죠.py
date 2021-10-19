def solution(password):
	capital_count, small_count, digit_count = 0, 0, 0
	for p in password:
		if p >= 'A' and p <= 'Z':
		#대문자 A부터 Z까지
			capital_count += 1
		elif p >= 'a' and p <= 'z':
		#소문자 a부터 z까지
			small_count += 1
		elif p >= '00' and p <= '99999999':
		#숫자 00자리 부터 9999999자리 까지..사실 두개이상의 숫자인데 그 방법은 잘 모르겠다
			digit_count += 1
	if capital_count >= 1 and  small_count >= 1 and digit_count >= 2:
		#아주깐깐한 단계를 거치면 비밀번호 완성~
		answer = True
	else:
		answer = False
	return answer

password1 = "helloworld"
ret1 = solution(password1)

print("solution 함수의 반환 값은", ret1, "입니다.")

password2 = "Hello123"
ret2 = solution(password2)

print("solution 함수의 반환 값은", ret2, "입니다.")