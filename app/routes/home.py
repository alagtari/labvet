from fastapi import APIRouter

router = APIRouter(tags=['test'])




@router.get('/')
def home():
    return 'hello world'