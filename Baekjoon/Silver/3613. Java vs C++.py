# 3613. Java vs C++
# https://www.acmicpc.net/problem/3613

import sys
input = sys.stdin.readline

name = input().rstrip()
n = len(name)

# 올바른 변수명인지 확인
is_valid = False

ans = ''

# 만약 밑줄('_')이 포함되어 있다면
# C++ 형식의 변수명이라 가정하고
# Java 형식의 변수명으로 바꿔줌
if '_' in name:

    # C++ 형식의 변수명은
    # '_', 소문자로만 구성되어 있어야 함

    for i in range(n):

        # 첫 글자일 경우 소문자여야 하므로
        # 소문자이면 ans에 해당 글자를 붙여줌
        if not i:
            if name[i].islower():
                ans += name[i]

            # 소문자가 아니라면 올바른 C++ 형식의
            # 변수명이 아니므로 변수명을 바꾸는 것을 종료
            else:
                break
        
        # 마지막 글자일 경우 소문자여야 하므로
        # 소문자가 맞는지 확인
        elif i == n-1:
            if name[i].islower():

                # 해당 글자가 소문자이고 그 앞 글자가
                # '_'이라면 대문자로 바꿔 ans에 붙여줌
                if name[i-1] == '_':
                    ans += name[i].upper()

                # 해당 글자가 소문자이고 그 앞 글자가
                # '_'가 아니라면 소문자라는 의미이므로
                # 그대로 ans에 붙여줌
                else:
                    ans += name[i]

            # 소문자가 아니라면 올바른 C++ 형식의
            # 변수명이 아니므로 변수명을 바꾸는 것을 종료
            else:
                break
        
        # 그 외는 '_'인지 소문자인지 확인
        else:

            # 만약 '_'이라면 그 앞 글자가 소문자인지 확인 
            # 소문자가 아니라면 올바른 C++ 형식의
            # 변수명이 아니므로 변수명을 바꾸는 것을 종료
            if name[i] == '_':
                if not name[i-1].islower():
                    break
            
            # 만약 소문자라면 그 앞 글자가 무엇인지 확인
            elif name[i].islower():

                # '_'이라면 대문자로 바꿔 ans에 붙여줌
                if name[i-1] == '_':
                    ans += name[i].upper()

                # '_'가 아니라면 소문자라는 의미이므로
                # 그대로 ans에 붙여줌
                else:
                    ans+= name[i]
            
            # '_'도 소문자도 아니라면
            # 올바른 C++ 형식의 변수명이 아니므로
            # 변수명을 바꾸는 것을 종료
            else:
                break

    # 도중에 종료되지 않았다면
    # 올바른 C++ 형식의 변수명이라
    # Java 형식의 변수명으로 다 바꿨다는 의미이므로
    # is_valid를 True로 갱신
    else:
        is_valid = True

# 아니라면 Java 형식의 변수명이라 가정하고
# C++ 형식의 변수명으로 바꿔줌
else:

    # Java 형식의 변수명은
    # 소문자, 대문자로만 구성되어 있어야 함

    for i in range(n):

        # 첫 글자일 경우 소문자여야 하므로
        # 소문자이면 ans에 해당 글자를 붙여줌
        if not i:
            if name[i].islower():
                ans += name[i]

            # 소문자가 아니라면 올바른 Java 형식의
            # 변수명이 아니므로 변수명을 바꾸는 것을 종료
            else:
                break

        # 그 외는 소문자인지 대문자인지 확인
        else:

            # 소문자라면 그대로 ans에 붙여줌
            if name[i].islower():
                ans += name[i]

            # 대문자라면 C++ 형식에 맞게
            # 앞에 '_'을 붙여주고 소문자로 바꿔 ans에 붙여줌
            elif name[i].isupper():
                ans += '_' + name[i].lower()

            # 소문자도 대문자도 아니라면
            # 올바른 Java 형식의 변수명이 아니므로
            # 변수명을 바꾸는 것을 종료
            else:
                break

    # 도중에 종료되지 않았다면
    # 올바른 Java 형식의 변수명이라
    # C++ 형식의 변수명으로 다 바꿨다는 의미이므로
    # is_valid를 True로 갱신
    else:
        is_valid = True

# 변수명이 있고 그 변수명이
# 올바른 변수명이라면 바뀐 변수명 출력
if n and is_valid:
    print(ans)

# 아니라면 출력 예시에 맞게 Error! 출력
else:
    print('Error!')