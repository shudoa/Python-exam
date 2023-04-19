#1.구구단 출력
for i in range(2, 10):
    for j in range(1, 10):
        print("{} x {} = {}".format(i, j, i*j))
    print()

# 줄 바꿈 없이 출력
for i in range(2,10):
    for j in range(1,10):
        print(" {} x {}= {} ".format(i,j,i*j),end="")
    print('')

#2.구구단 거꾸로 출력
for i in range(9, 0, -1):
    for j in range(9, 0, -1):
        print(f"{j} x {i} = {i*j}", end="\t")
    print()

#3.짝수 혹은 홀수만 출력
for i in range(2, 10, 2):  # 짝수단 출력
    for j in range(1, 10):
        print(f"{i} x {j} = {i*j}", end="\t")
    print()

print()  # 줄바꿈

for i in range(1, 10, 2):  # 홀수단 출력
    for j in range(1, 10):
        print(f"{i} x {j} = {i*j}", end="\t")
    print()

#4.구구단 결과를 리스트로 저장
gugudan = [[i*j for j in range(1, 10)] for i in range(1, 10)]

# 예시: 5단 곱하기 6은 gugudan[4][5]로 접근할 수 있다.

#5.구구단 결과를 딕셔너리로 저장
gugudan = {}
for i in range(1, 10):
    gugudan[i] = {j: i*j for j in range(1, 10)}
#위 코드는 딕셔너리를 생성하는 코드
# 예시: 5단 곱하기 6은 gugudan[5][6]으로 접근할 수 있다.
#아래 코드는 저장된 값을 출력
gugudan = {}
for i in range(1, 10):
    gugudan[i] = {j: i*j for j in range(1, 10)}

# 2단 출력
print(gugudan[2])

# 4단 6을 곱한 결과 출력
print(gugudan[4][6])

# 전체 구구단 출력
for i in range(1, 10):
    print(f"{i}단")
    for j in range(1, 10):
        print(f"{i} x {j} = {gugudan[i][j]}")
#리스트 구조
my_list = []
for i in range(5):
    num = int(input("정수를 입력하세요: "))
    my_list.append(num)

print("입력한 정수들로 이루어진 리스트:", my_list)

# 2개의 정수를 받아서 첫 번쨰 정수가 두 번쨰 정수로
# x%y=0이 되는 프로그램 작성
x = int(input("정수를 입력하시오: "))
y = int(input("정수를 입력하시오: "))
if x%y ==0:
    print("약수입니다.")
else:
    print("약수가 아닙니다.")
    
# if-else문
# 사용자로부터 3개의 정수를 입력받은 후 if-else를 사용하여 
# 제일 작은 정수는 10입니다.를 출력하라
x, y, z = eval(input("3개의 정수를 입력하시오: "))
if x < y and x < z:
    print("제일 작은 값은 {}입니다.".format(x))
elif y < x and y < z:
    print("제일 작은 값은{}입니다.".format(y))
else:
    print("제일 작은 값은{}입니다".format(z))
    
# 중첩 if문
country = input("배송지(현재는 korea와 us만 가능):")
price = int(input("상품의 가격: "))

if country == "korea":
    if price >=20000:
        shipping_cost=0
    else:
        shipping_cost=3000
else:
    if price >=100000:
        shipping_cost=0
    else:
        shipping_cost=8000
print("배송비 =",shipping_cost)

# 연속 if문
score = int(input("학점 입력: "))
if score >=90:
    print("학점 A")
elif score>=80:
    print("학점 B")
elif score >=70:
    print("학점 C")
elif score >= 60:
    print("학점 D")
else:
    print("학점 F")

# 연속 if문
command = input("문자를 입력하시오: ")
if command == "c, C":
    print("Rectangle")
elif command == "t, T" :
    print("Triangle")
elif command == "c, C":
    print("Circle")
else:
    print("Unknown")

# 조건 연산자
x=10
y=12
max_value = (x if x>y else y)
print("max_value", max_value)

# 조건 연산자2
temp = int(input("온도를 입력하시오: "))
if temp < 0:
    state = "얼음"
    print(state)
else:
    state = "기체"
    print(state)
    
# 조건 연산자2를 간결하게
temp = int(input("온도를 입력하시오: "))
state = "얼음" if temp < 0 else "기체"
print(state)

#



