# 리스트
# 순서 0 중복 0 변경 0

a = [1,2,3]
print(a, type(a))

b = [10, a, True, '문자열']
print(b[1])
print(b[1][2])

c = [[1,2], [3,4,5], [6,7,8,9]]
print(c)
print(c[2][2])

print("----------------------------------------")
# 동물
pet = ['강아지', '고양이', '거북이', '고슴도치']
print(pet)
pet.append('열대어') #맨뒤에 삽입
print(pet)
pet.remove('거북이') #해당열 제거
print(pet)
pet.insert(0, "이구아나") #insert(index, object) 해당인덱스에 삽입
print(pet)
pet.extend(["토끼", "햄스터"]) #list + list 뒤에 삽입
print(pet)
pet += ["돼지"]
print(pet)

print(len(pet))
# 고슴도치를 제거하라
# pet.remove("고슴도치")
# del pet[3]
print(pet.pop(3))
print(pet)


animal = pet
print("animal: ", animal)
print("pet :", pet)

pet[0] = "멍멍이"
print("-----------------------------------------")
print("animal: ", animal)
print("pet :", pet)

print(id(animal), id(pet)) #같은 대상을 참조











