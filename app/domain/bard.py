from fastapi import APIRouter


router = APIRouter()

@router.post("/bard")
def playBard():
    return 