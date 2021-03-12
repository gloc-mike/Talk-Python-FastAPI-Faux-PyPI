import fastapi
import uvicorn
import fastapi_chameleon
from fastapi_chameleon import template

app = fastapi.FastAPI()

fastapi_chameleon.global_init('../templates')


@app.get("/")
@template(template_file='index.html')
def index(user='anonymous'):
    return {
        'user_name': user
    }


@app.get('/about')
def about():
    return {}


@app.get('/account')
def index():
    return {}


@app.get('/account/register')
def register():
    return {}


@app.get('/account/login')
def about():
    return {}


@app.get('/account/logout')
def about():
    return {}

if __name__ == '__main__':
    uvicorn.run(app)
