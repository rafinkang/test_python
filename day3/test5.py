# while expression:
#     pass
# else:
#     pass
a = 1
while a != 5:
    print(a)
    a += 1

# for target_list in expression_list:
#     pass

# k = 1
# while True:
#     k+=1
#     print("무한반복", k)

print("-----------------------------------")
for i in range(5):
    for j in range(3):
        print("i:",i,"j:",j)
print("-----------------------------------")
# i의 값 1~9 까지 출력
for dan in range(1, 10):
    for i in range(1,10):
        print(dan, "* "+str(i) + " = " + str(dan*i))
    print("-----------------------------------")

# 1
# 12
# 123
# 1234
# 반복문을 사용해서 출력
w = '';
for i in range(1,5):
    w += str(i)
    print(w)

# 11111
print('--------------------------------------')
print("1"*5);
# 22222
for i in range(5):
    print("2", end="")
print()
# 33333
for i in range(5):
    print("3", end="")
print()
# 44444
for i in range(5):
    print("4", end="")
print()
# 55555
for i in range(5):
    print("5", end="")
print()
print('--------------------------------------')
for j in range(1,6):
    for i in range(5):
        print(j, end="")
    print()
print('--------------------------------------')

