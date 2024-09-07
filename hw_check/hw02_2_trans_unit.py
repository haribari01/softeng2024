#온도(섭씨=>화씨)
def c2f(temp_c):
    return temp_c * 9 / 5 + 32

#길이
def in_to_cm(inch):
    return inch * 2.54

#열 에너지
def heat_J(cal):
    return cal * 4.1868

def main():
    temp_c = float(input("섭씨온도를 입력하세요.(정수~소수 2자리)"))
    print(f"{temp_c:.2f}℃ => {c2f(temp_c):.2f}℉")

    inch = int(input("inch를 입력하세요. (정수)"))
    print(f"{inch}inch는 {in_to_cm(inch)}cm 입니다.")

    cal = int(input("물 몇g? (정수)"))
    print(f"물{cal}g을 1℃ 올리는데 필요한 열 에너지는 {heat_J(cal):.4f}J입니다.")

if __name__ == '__main__':
    main()