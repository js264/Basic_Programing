# main.py
import prime_module
num = int(input("숫자 입력: "))

# 소수 판별
if prime_module.is_prime(num):
    print(num, "은 소수입니다.")
else:
    print(num, "은 소수가 아닙니다.")
print()

#2~N까지 소수 출력
print(f'2부터 {num}까지의 소수:')
prime_module.print_primes(num)
