from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from github import Github
import os

router = APIRouter(prefix="/github", tags=["GitHub"])

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
if not GITHUB_TOKEN:
    raise Exception("❌ GITHUB_TOKEN não encontrado.")

g = Github(GITHUB_TOKEN)
user = g.get_user()


class RepoCreate(BaseModel):
    name: str
    description: str = ""
    private: bool = True


@router.post("/create-repo")
def create_repo(repo: RepoCreate):
    try:
        repository = user.create_repo(
            name=repo.name,
            description=repo.description,
            private=repo.private
        )
        return {"message": "✅ Repositório criado com sucesso!", "url": repository.html_url}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/list-repos")
def list_repos():
    try:
        repos = user.get_repos()
        return {"repositorios": [repo.name for repo in repos]}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))