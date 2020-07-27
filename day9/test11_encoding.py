with open("./day9/msg2.txt", "r", encoding="utf-8") as file:
    data = file.read()
    print(data)

lines = ['안녕하세요\n', '오늘은 금요일\n', '이면 좋겠네요\n']

with open("./day9/msg3.txt", "w", encoding="utf-8") as file:
    file.writelines(lines)

with open("./day9/msg3.txt", "r", encoding="utf-8") as file:
    data = file.readlines()
    print(data)