from hw02_3_check_prime_number import is_prime

def main():
    n = int(input('숫자를 입력하세요.'))

    print(f"1부터 {n}중에 소수는 {[i for i in range(2, n+1) if is_prime(i)]}입니다.")

if __name__ == '__main__':
    main()
