def is_odd(a):
    if a%2==0:
        print('짝')
    else:
        print('홀')

is_odd(2)
def avrege(*b):
    num = 0
    for i in b:
        num += i
    return num/len(b)

print(avrege(1,2,3,4,5,6,7,9))