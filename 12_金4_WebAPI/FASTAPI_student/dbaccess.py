import sys
sys.dont_write_bytecode = True
from fastapi import FastAPI, Response, status
from pydantic import BaseModel
from fastapi import FastAPI, HTTPException
import mysql.connector
import datetime
# FastAPI本体を生成
app = FastAPI()

class Student(BaseModel):
    id:int = None
    name:str
    birthday: datetime.date
    cls:str = None


mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'ToMoYo4869',
    database = 'school'
)

@app.get("/students")
def find_all():
    sql = 'select * from student order by id'
    cursor = mydb.cursor(dictionary=True)
    cursor.execute(sql)
    result = cursor.fetchall()
    return {'students':result}

@app.get("/students/{id}")
def find_id(id:int,response:Response):
    sql = 'select * from student where id = %s order by id'
    data = [id]
    cursor = mydb.cursor(dictionary=True)
    cursor.execute(sql,data)
    result = cursor.fetchone()
    if result != None:
        return {'students':result}
    else:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"Not Found"}
        


#学生登録API
@app.post("/students/",status_code=201)
def register(studnet:Student):
    sql = "insert into student (id,name,birthday,class) values (%s,%s,%s,%s)"
    date = [studnet.id,studnet.name,studnet.birthday,studnet.cls]
    cursor = mydb.cursor(dictionary=True)
    cursor.execute(sql,date)
    mydb.commit()

    return {"Created"}

#学生更新API
@app.put("/students/",status_code=204)
def register(name:str,id:int,response:Response):
    if is_student_id_exists(id):
        sql = "update student set name = %s where id = %s"
        date = [name,id]
        cursor = mydb.cursor(dictionary=True)
        cursor.execute(sql,date)
        mydb.commit()
        return {"Updated"}
    else:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"Not Found"}


#学生削除API
@app.delete("/students/",status_code=204)
def register(id:int,response:Response):
    if is_student_id_exists(id):
        sql = "delete from student where id = %s"
        date = [id]
        cursor = mydb.cursor(dictionary=True)
        cursor.execute(sql,date)
        mydb.commit()
        return {"Deleted"}
    else:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"Not Found"}


#学生IDの存在チェック
def is_student_id_exists(id):
    sql = 'select * from student where id = %s'
    data = [id]
    cursor = mydb.cursor(dictionary=True)
    cursor.execute(sql,data)
    result = cursor.fetchone()

    return result != None