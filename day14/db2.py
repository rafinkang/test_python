import cx_Oracle

connection = cx_Oracle.connect("scott", "tigertiger", "orcl.cet8lirw1jgl.ap-northeast-2.rds.amazonaws.com:1521/orcl")
print(connection)

cur = connection.cursor()
query = "select empno, ename, sal from emp where ename = :txt" # :txt - 바인드 변수
cur.execute(query, txt = "SCOTT") # :txt에 전달

for empno, ename, sal in cur:
    print("{} \t {} \t {}".format(empno, ename, sal))


    
connection.close()

