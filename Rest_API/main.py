from http.client import responses

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

#creating new app
app = FastAPI()

items = []

'''
defining path - app decorator defining a path for HTTP GET - in our case
path is / i.e. root directory, so when someone visits root dir, our root
function gets called
'''
@app.get("/")
def root():
    return {"Hello": "World"}

class Item(BaseModel):
    text:str=None
    is_done: bool=False #deleting default makes the value required
'''
Adding routes - defininf different routes app should respond to each showing
different interactions
'''

#end-point1
@app.post("/items")
def create_item(item:Item):
    items.append(item)
    return item

#RESTful vs not?

@app.get("/items/{item_id}", response_model=Item)
def get_item(item_id:int) -> Item:
    if item_id < len(items):
        return items[item_id]
    else:
        raise HTTPException(status_code=404, detail=f"Item {item_id} not found")


@app.get("/items", response_model = Item)
def list_items(limit:int=10):
    return items[0:limit]

#everytime you make a change, server reloads, items list becomes empty


'''
Raising useful error messages instead of "internal server error"

HTTP response codes

100-199 -> informational responses
200-299 -> success
300-399 -> redirection
400-499 -> Client error
500-599 -> Server error

404 - Not found
Sending info tp FastAPI - Request & Path params

FastAPI supports pydantic models which support more complex sorts of data

Modeling input done

Modeling output - response model param

Interactive documentation - http://127.0.0.1:8000/docs
'''



'''
TERMINAL

pip install fastapi
pip install uvicorn - server used to test and run our fastapi apps
uvicorn main:app --reload
SYNTAX: uvicorn file_name:app_name --reload
reload flag automatically refreshes whenever I change file

Let this one run, open new terminal

(.venv) PS C:\Users\shrip\PycharmProjects\PythonProject> curl.exe -X POST "http://127.0.0.1:8000/items?item=squash"
"squash"
7.0.0.1:8000/items?item=mango"
"mango"
(.venv) PS C:\Users\shrip\PycharmProjects\PythonProject> curl.exe -X POST "http://127.0.0.1:8000/items?item=strawberry"
"strawberry"
(.venv) PS C:\Users\shrip\PycharmProjects\PythonProject> curl.exe -X POST "http://127.0.0.1:8000/items?item=watermelon"
"watermelon"
(.venv) PS C:\Users\shrip\PycharmProjects\PythonProject> curl.exe -X GET 'http://127.0.0.1:8000/items?limit=3'
["apple","orange","banana"]
(.venv) PS C:\Users\shrip\PycharmProjects\PythonProject> curl.exe -X POST -H "Content-Type:application/json" -d '{\"text\":\"apple\"}' 'http://127.0.0.1:8000/items'    
{"text":"apple","is_done":false}

'''