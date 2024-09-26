from typing import Annotated
from fastapi import FastAPI, File, UploadFile
import os
import random

#from datetime import datetime
#from pytz import timezone
#import pymysql.cursors
#
#import uuid
#from mnist.db import get_conn, select, dml

app = FastAPI()

@app.post("/files/")
async def create_file(file: Annotated[bytes, File()]):
    return {"file_size": len(file)}

#@app.post("/uploadfile/")
#async def create_upload_file(file: UploadFile): # async 비동기 ??? -> 이거 좀 알아보자
#    ts = datetime.now(timezone('Asia/Seoul')).strftime('%Y-%m-%d %H:%M:%S')
#    # 이미지 파일 서버에 저장
#    img = await file.read()
#    file_name = file.filename
#    file_label = file_name.split('.')[0].split('_')[0]
#    file_ext = file.content_type.split('/')[-1] # content_type = image/png 형식으로 출력됨
#
#    upload_dir = os.getenv('UPLOAD_DIR', "/home/kimpass189/code/mnist/photo")
#    file_full_path = os.path.join(upload_dir, f'{uuid.uuid4()}.{file_ext}')
#    os.makedirs(os.path.dirname(file_full_path), exist_ok = True)
#    with open(file_full_path, 'wb') as f:
#        f.write(img)
#
#    # 이미지 파일 저장 경로를 DB에 insert
#    # 컬럼정보 : 파일이름, 파일경로, 요청시간(초기 insert), 요청 사용자(n??) # not null
#    # 컬럼정보 : 예측모델, 예측결과, 요청시간, 예측시간(추후 업뎃) # null
#    # DB insert
##    connection = pymysql.connect(host=os.getenv("DB_IP", "localhost"),
##                             user='mnist',
##                             password='1234',
##                             database='mnistdb',
##                             port=int(os.getenv("MY_PORT", 53306)),
##                             cursorclass=pymysql.cursors.DictCursor)
#    connection = get_conn()
#    sql = "INSERT INTO `image_processing`(file_name, label, file_path, request_time, request_user) VALUES (%s, %s, %s, %s, %s)"
#    with connection:
#        with connection.cursor() as cursor:
#            cursor.execute(sql,(file_name, file_label, file_full_path, ts, "n18"))
#        connection.commit()
#
#    return {
#            "filename": file_name,
#            "filelabel" : file_label,
#            "content_type" : file.content_type,
#            "file_full_path" : file_full_path,
#            "request_time" : ts 
#            }
@app.get("/predict/")
def pred(num:int = 10):
    result = random.randint(0,num)
    return result
#print(pred())
