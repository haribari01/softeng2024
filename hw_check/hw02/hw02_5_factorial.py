def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)

def main():
    n = int(input("몇 팩토리얼?"))
    print(f"{n}! = {factorial(n)}")

if __name__ == '__main__':
    main()
