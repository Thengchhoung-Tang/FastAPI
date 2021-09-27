# Import
from fastapi import FastAPI

# Instance
app = FastAPI()


# Decorate
@app.get('/')
# Function
def index():
    return {'data': {'name': 'Thengchhoung'}}


@app.get('/about')
def about():
    return {'data':{'about page'}}