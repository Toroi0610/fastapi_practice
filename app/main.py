from fastapi import FastAPI, File, UploadFile
from .processing import add

app = FastAPI()

def read_file(file : UploadFile = File(...)):
    filename = file.filename
    fileobj = file.file
    print(filename)
    print(fileobj)


@app.get("/")
async def route_page():
    return {"Hello", "World!!"}

@app.post("/files/")
async def create_file(file: bytes = File(...)):
    print(file.decode("utf-8"))
#    return {"file_size": len(file)}
    return add(file.decode("utf-8"))

@app.post("/processing-add/")
async def processing_add(file: bytes = File(...)):
#    return {"file_size": len(file)}
    return add(file.decode("utf-8"))

@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile = File(...)):
#    return {"filename": file.filename}
    return add(file)
