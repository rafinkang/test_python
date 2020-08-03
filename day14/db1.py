# pip install cx_Oracle 설치(aws연결)
# oracle, python bit가 맞아야함(64)

import cx_Oracle

connection = cx_Oracle.connect("scott", "tigertiger", "orcl.cet8lirw1jgl.ap-northeast-2.rds.amazonaws.com:1521/orcl")
print(connection)

cur = connection.cursor()
query = "select * from dept"

cur.execute(query) # return : tuple

for x in cur:
    print(x)
    
# 반듯이 연결 끊기
connection.close()

