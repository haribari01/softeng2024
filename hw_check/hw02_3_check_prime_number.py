def is_prime(num):
    if num < 2:
        return False
    for i in range(2, num):    #1과 자기 자신은 범위에서 제외
        if num % i == 0:
            return False       #break를 쓸 필요가 없음.
    return True

def main():
    num = int(input("숫자를 입력하세요."))

    if is_prime(num):
        print(f"{num}은 소수입니다.")
    else:
        print(f"{num}은 소수가 아닙니다.")

if __name__ == '__main__':
    main()