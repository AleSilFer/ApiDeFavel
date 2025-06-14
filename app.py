from fastapi import FastAPI
from github_services import router as github_router

app = FastAPI(title='GPT DE FAVELA API')

app.include_router(github_router)

@app.get('/')
def read_root():
    return {'message': '🔥 GPT DE FAVELA API ONLINE 🔥'}