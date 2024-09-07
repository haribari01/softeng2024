def holzzack(n):
    return n % 2 == 0

def main():
    n = int(input("숫자를 입력하세요."))

    if holzzack(n):
        print(f"{n}은 짝수 입니다.")
    else:
        print(f"{n}은 홀수 입니다.")

if __name__ == '__main__':
    main()
