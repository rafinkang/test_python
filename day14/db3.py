# 1. 10번 부서 사원의 사번, 이름, JOB, DEPTNO를 출력하는 python 코드를 작성하세요
import cx_Oracle

connection = cx_Oracle.connect("scott", "tigertiger", "orcl.cet8lirw1jgl.ap-northeast-2.rds.amazonaws.com:1521/orcl")

cur = connection.cursor()
query = "select empno, ename, job, deptno from emp where deptno = 10"
cur.execute(query)

for empno, ename, job, deptno in cur:
    print("empno:", empno, "\tename:", ename, "\tjob:", job, "\tdeptno:", deptno)
    
connection.close()
