import cx_Oracle

connection = cx_Oracle.connect("scott", "tigertiger", "aws")
print(connection)

cur = connection.cursor()
query1 = """
    insert into dept 
    values (:deptno, :dname, :loc)
    """

query2 = """
    insert into dept(deptno, loc) 
    values (:deptno, :loc)
    """
# cur.execute(query1, [1,"SALESMAN", "SEOUL"])
# cur.execute(query1, [2, "", "BUSAN"]) # null 넣기
# cur.execute(query1, [2, None, "BUSAN"]) # null 넣기
cur.execute(query2, [3, "INCHEON"]) # null 넣기
connection.commit()
    
connection.close()

