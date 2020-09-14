# 정석풀이
## print("", end='') end기능을 통해 뒤에 어떤 문자가 올지 지정해줄 수 있다.

a, b = map(int, input().strip().split(' '))
answer=""
ina = []
for i in range(b):
    for j in range(a):
        print("*", end='')
    print()

# 연산자 풀이
a, b = map(int, input().strip().split(' '))
answer=("*"*a + "\n")*b
print(answer)