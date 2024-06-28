from fastapi import FastAPI
from pydantic import BaseModel
from fastapi import FastAPI, HTTPException
import mysql.connector
# FastAPI本体を生成
app = FastAPI()

#MySQLに接続
mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'ToMoYo4869',
    database = 'school'
)

@app.get("/student")
def rfind_all():
    sql = 'select * from student order by id'
    cursor = mydb.cursor(dictionary=True)
    cursor.execute(sql)
    result = cursor.fetchall()
    return {'student':result}

@app.get("/student/{id}")
def find_id(id:int):
    sql = 'select * from student where id = %s order by id'
    data = [id]
    cursor = mydb.cursor(dictionary=True)
    cursor.execute(sql,data)
    result = cursor.fetchall()
    return {'student':result}