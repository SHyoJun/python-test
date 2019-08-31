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
# input1 = input("첫번째 숫자를 입력하세요:")
# input2 = input("두번째 숫자를 입력하세요:")
#
# total = int(input1) + int(input2)
# print("두 수의 합은 %s 입니다" % total)
# 4번문제
# print("you", "need", "python")
# #5번문제
# f1 = open("test1.txt", 'w')
# f1.write("Life is too short")
# f1.close()
# f2 = open("test1.txt", 'r')
# print(f2.read())
# f2.close()
# 6번문제
# with open("test2.txt", 'a') as f:
#     f.write(input("입력바랍니다 :")+"\n")
# 7번문제
with open("test.txt", 'r') as f:
    line = f.readlines()
    for i in range(0,len(line)):
        line[i] = line[i].replace("java", "python")

with open("test.txt", 'w') as f:
    for i in line:
        f.writelines(i)