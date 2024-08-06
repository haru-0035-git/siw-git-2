from fastapi import FastAPI, Response, status
from pydantic import BaseModel
from fastapi import FastAPI, HTTPException
import mysql.connector
from datetime import date
# FastAPI本体を生成
app = FastAPI()

class Accountbook(BaseModel):
    id:int = None
    date:date
    bop:int
    breakdown:str
    price:int

#MySQLに接続
mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'ToMoYo4869',
    database = 'accountbook'
)

@app.post("/accountbook/",status_code=201)
def register(accountbook:Accountbook):
    sql = "insert into accountbooks (date,bop,breakdown,price) values (%s,%s,%s,%s)"
    data = [accountbook.date,accountbook.bop,accountbook.breakdown,accountbook.price]
    cursor = mydb.cursor(dictionary=True)
    cursor.execute(sql,data)
    mydb.commit()

    return{"Created"}

@app.get("/accountbook/{date}",status_code=200)
def find_date(date:str,response:Response):
    sql = 'select * from accountbooks where DATE_FORMAT(date,"%Y-%m") = %s order by id'
    data = [date]
    cursor = mydb.cursor(dictionary=True)
    cursor.execute(sql,data)
    result = cursor.fetchall()
    if result != None:
        return {'accountbooks':result}
    else:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"Not Found"}
    
@app.put("/accountbook/",status_code=204)
def update(accountbook:Accountbook,response:Response):
    if is_accountbook_id_exists(accountbook.id):
        sql = "update accountbooks set date = %s,bop = %s ,breakdown = %s ,price = %s where id = %s"
        date = [accountbook.date,accountbook.bop,accountbook.breakdown,accountbook.price,accountbook.id]
        cursor = mydb.cursor(dictionary=True)
        cursor.execute(sql,date)
        mydb.commit()
        return {"Updated"}
    else:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"Not Found"}

@app.delete("/accountbook/{id}",status_code=204)
def delete(id:int,response:Response):
    if is_accountbook_id_exists(id):
        sql = "delete from accountbooks where id = %s"
        date = [id]
        cursor = mydb.cursor(dictionary=True)
        cursor.execute(sql,date)
        mydb.commit()
        return {"Deleted"}
    else:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"Not Found"}

@app.get("/accountbook/find_id/{id}",status_code=200)
def find_id(id:int,response:Response):
    sql = 'select * from accountbooks where id = %s order by id'
    data = (id,)
    cursor = mydb.cursor(dictionary=True)
    cursor.execute(sql,data)
    result = cursor.fetchone()
    if result != None:
        return {'accountbook':result}
    else:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"detail": "Not Found"}

#学生IDの存在チェック
def is_accountbook_id_exists(id):
    sql = 'select * from accountbooks where id = %s'
    data = [id]
    cursor = mydb.cursor(dictionary=True)
    cursor.execute(sql,data)
    result = cursor.fetchone()

    return result != None