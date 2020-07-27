# 열 쓰 닫
# with open("파일명", 파일모드) as 파일객체명
#   코드 ------> 열고 쓰고나면 자동으로 닫아줌

# with open("./day9/msg.txt", "w") as file:
#     file.write("오늘은 여기까지... ㅅㄱㄹ \n")
with open("./day9/msg.txt", "r") as file:
    full_text = file.read()
    # print(full_text, type(full_text))
    text_list = full_text.split()
    # print(text_list)
    cnt = 0
    for texts in text_list:
        if texts.find("카카오") >= 0:
            cnt+=1
    print(cnt)
