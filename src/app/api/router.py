from fastapi import APIRouter
from api.issue.routes import router as issue_router


router = APIRouter(prefix='/api')
router.include_router(issue_router)


@router.get('/issues')
async def get_issues() -> list[dict]:
    pass
