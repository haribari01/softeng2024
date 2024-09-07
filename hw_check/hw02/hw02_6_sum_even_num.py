from hw02_1_holzzack import holzzack

def main():
    even_100 = [i for i in range(1,101) if holzzack(i)]
    print(f"1부터 100까지 짝수의 합은 {sum(even_100)}입니다.")

if __name__ == '__main__':
    main()
