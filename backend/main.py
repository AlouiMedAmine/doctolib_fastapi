#import FastAPI
from fastapi import FastAPI
 
#create a FastAPI object
app = FastAPI()
 
#define a Hello World endpoint
@app.get("/")
def hello_world():
    return {"msg":"Hello world"}



@app.get('/property')
def property():
    return 'This is the property page'



@app.get('/movies')
def movies():
    return {'movie list':{'movie 1','movie 2','movie 3'}}
