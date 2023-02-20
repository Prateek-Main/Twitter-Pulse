import fastapi

app = fastapi.FastAPI()

@app.get('/')
def index():
    return {'data':{'name':'parth'}}

@app.get('/about')
def about():
    return {'data':{'about page'}} 