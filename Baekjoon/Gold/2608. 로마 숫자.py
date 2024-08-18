# 2608. 로마 숫자
# https://www.acmicpc.net/problem/2608

import sys
input = sys.stdin.readline

# 로마 숫자를 아라비아 숫자로 바꾸기 위한 딕셔너리
ro_ara = {
    'I':1, 'IV':4, 'IX':9, 'V':5,
    'X':10, 'XL':40, 'XC':90, 'L':50,
    'C':100, 'CD':400, 'CM':900, 'D':500, 'M':1000
}

# 아라비아 숫자를 로마 숫자로 바꾸기 위한 딕셔너리
ara_ro = {
    0: '', 1: 'I', 2: 'II', 3: 'III', 4: 'IV', 5: 'V',
    6: 'VI', 7: 'VII', 8: 'VIII', 9: 'IX', 10: 'X',
    20: 'XX', 30: 'XXX', 40: 'XL', 50: 'L', 60: 'LX',
    70: 'LXX', 80: 'LXXX', 90: 'XC', 100: 'C', 200: 'CC',
    300: 'CCC', 400: 'CD', 500: 'D', 600: 'DC', 700: 'DCC',
    800: 'DCCC', 900: 'CM', 1000: 'M', 2000: 'MM', 3000: 'MMM'
}

# 로마 숫자를 아라비아 숫자로 바꿔주는 함수
def roman_to_arabic(roman):
    idx = 0
    arabic = 0

    # 주어진 로마 숫자를 끝까지 탐색
    while idx < len(roman):

        # 해당 기호가 나온 수를 확인
        cnt = 1

        # I, X, C, M는 다른 기호와 결합해서 수를 표현하거나
        # 연속해서 3번까지 사용할 수 있으므로 해당 경우를 분기처리
        if roman[idx]=='I' or roman[idx]=='X' or roman[idx]=='C' or roman[idx]=='M':

            # 해당 기호에 다른 기호가 있으면서 그 기호까지 합했을 때
            # 해당하는 아라비아 숫자가 있다면 그 수를 더해주고
            # 인덱스에 1을 더해 다음으로 이동
            if idx+1 < len(roman) and ro_ara.get(roman[idx:idx+2]):
                arabic += ro_ara[roman[idx:idx+2]]
                idx += 1

            # 해당 기호에 다른 기호가 있다면
            # 그 기호가 해당 기호와 같은지 확인
            # 달라질 때까지 인덱스를 이동하면서
            # 같은 기호가 나온 수를 계산
            else:
                while idx+1 < len(roman) and roman[idx] == roman[idx+1]:
                    cnt += 1
                    idx += 1
                
                # 해당 기호에 해당하는 아라비아 숫자를 찾고
                # 해당 기호가 나온 수만큼 곱해 더해줌
                arabic += ro_ara[roman[idx]] * cnt

        # 만약 하나의 기호만 써야 한다면
        # 해당 기호에 해당하는 아라비아 숫자를 찾아 더해줌
        else:
            arabic += ro_ara[roman[idx]]

        # 인덱스에 1을 더해 다음으로 이동
        idx += 1

    # 바꾼 아라비아 숫자를 반환
    return arabic


# 아라비아 숫자를 로마 숫자로 바꿔주는 함수
def arabic_to_roman(arabic):

    # 각 자릿수에 있는 아라비아 숫자를
    # 로마 숫자로 바꾸기 위해 문자열로 형변환
    arabic = str(arabic)
    roman = ''

    # 해당 아라비아 숫자에 자릿수를 곱해주고
    # 계산된 아라비아 숫자에 해당되는 로마 숫자를 찾아 더해줌
    # 왼쪽부터 계산해야 하므로 순차적으로 계산
    for i in range(len(arabic)):
        roman += ara_ro[int(arabic[i]) * 10**(len(arabic)-i-1)]

    # 바꾼 로마 숫자를 반환
    return roman


num1 = input().rstrip()
num2 = input().rstrip()

arabic = roman_to_arabic(num1) + roman_to_arabic(num2)
roman = arabic_to_roman(arabic)

print(arabic)
print(roman)