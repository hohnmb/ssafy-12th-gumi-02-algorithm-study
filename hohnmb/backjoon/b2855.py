# 세자리수 x 세자리수 곱셈이다.
# a와 b 둘중 하나는 문자열로 납둬야 할 필요가 있다.
a = int(input())
b = input()
# 문자열로 놔둔 이유는 정수형 곱하기 정수형은 중간 과정을 출력할 수 없으므로
# 둘 중 하나를 문자열로 바꾸면 각 자릿수를 곱하는 과정을 출력할수있다.
print(a*int(b[2]))
print(a*int(b[1]))
print(a*int(b[0]))
print(a*int(b))
