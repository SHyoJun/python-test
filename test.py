# 1번문제
def is_odd(a):
    if a%2==0:
        print('짝')
    else:
        print('홀')

is_odd(2)
# 2번문제
def avrege(*b):
    num = 0
    for i in b:
        num += i
    return num/len(b)

print(avrege(1,2,3,4,5,6,7,9))
# 3번문제
input1 = input("첫번째 숫자를 입력하세요:")
input2 = input("두번째 숫자를 입력하세요:")

total = int(input1) + int(input2)
print("두 수의 합은 %s 입니다" % total)